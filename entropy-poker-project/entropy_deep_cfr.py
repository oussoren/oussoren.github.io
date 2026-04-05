import numpy as np
import torch
import torch.nn as nn

from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver


class EntropyDeepCFRSolver(DeepCFRSolver):

    def __init__(self, *args, alpha: float = 0.0, entropy_eps: float = 1e-8, **kwargs):
        super().__init__(*args, **kwargs)
        self.alpha = float(alpha)
        self.entropy_eps = float(entropy_eps)

    @staticmethod
    def _safe_row_normalize(x: torch.Tensor, eps: float):
        z = x.sum(dim=-1, keepdim=True).clamp_min(eps)
        return x / z

    def _masked_entropy_from_probs(self, probs: torch.Tensor, target_probs: torch.Tensor) -> torch.Tensor:
        mask = (target_probs > 0).to(probs.dtype)

        row_has_any = (mask.sum(dim=-1, keepdim=True) > 0).to(probs.dtype)
        mask = mask * row_has_any + (1.0 - row_has_any) * torch.ones_like(mask)

        masked = probs * mask
        masked = self._safe_row_normalize(masked, self.entropy_eps)
        masked = masked.clamp_min(self.entropy_eps)

        ent = -(masked * masked.log()).sum(dim=-1)  # (B,)
        return ent

    def _learn_strategy_network(self):
        for _ in range(self._policy_network_train_steps):
            if self._batch_size_strategy:
                if self._batch_size_strategy > len(self._strategy_memories):
                    return None
                samples = self._strategy_memories.sample(self._batch_size_strategy)
            else:
                samples = self._strategy_memories

            info_states = []
            action_probs = []
            iterations = []
            for s in samples:
                info_states.append(s.info_state)
                action_probs.append(s.strategy_action_probs)
                iterations.append([s.iteration])

            self._optimizer_policy.zero_grad()

            iters = torch.FloatTensor(np.sqrt(np.array(iterations)))

            ac_probs = torch.FloatTensor(np.array(action_probs)).reshape(len(action_probs), -1)

            logits = self._policy_network(torch.FloatTensor(np.array(info_states)))
            outputs = self._policy_sm(logits)

            loss_strategy = self._loss_policy(iters * outputs, iters * ac_probs)

            if self.alpha != 0.0:
                ent_per = self._masked_entropy_from_probs(outputs, ac_probs)

                ent_weighted = ((iters.squeeze(-1) ** 2) * ent_per).mean()

                if not hasattr(self, "_printed_scale"):
                    self._printed_scale = True
                    print(
                        f"[scale] loss_mse={loss_strategy.detach().item():.6f} "
                        f"ent_w={ent_weighted.detach().item():.6f} "
                        f"alpha={self.alpha}"
                    )

                loss_total = loss_strategy - self.alpha * ent_weighted
            else:
                loss_total = loss_strategy

            loss_total.backward()
            self._optimizer_policy.step()

        return loss_strategy.detach().numpy()