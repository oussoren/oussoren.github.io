import numpy as np
import torch

from open_spiel.python.pytorch.deep_cfr import DeepCFRSolver


class SoftRegretMatchingDeepCFRSolver(DeepCFRSolver):

    def __init__(self, *args, rm_lambda: float = 1.0, rm_eps: float = 1e-12, **kwargs):
        super().__init__(*args, **kwargs)
        self.rm_lambda = float(rm_lambda)
        self.rm_eps = float(rm_eps)

    def _sample_action_from_advantage(self, state, player):
        info_state = state.information_state_tensor(player)
        legal_actions = state.legal_actions(player)

        with torch.no_grad():
            state_tensor = torch.FloatTensor(np.expand_dims(info_state, axis=0))
            raw_advantages = self._advantage_networks[player](state_tensor)[0].numpy()

        r_pos = np.maximum(raw_advantages, 0.0)

        matched = np.zeros(self._num_actions, dtype=np.float64)

        mass = float(np.sum([r_pos[a] for a in legal_actions]))
        if mass <= self.rm_eps:
            best = max(legal_actions, key=lambda a: raw_advantages[a])
            matched[best] = 1.0
            return r_pos.tolist(), matched

        lam = self.rm_lambda
        vals = np.array([lam * r_pos[a] for a in legal_actions], dtype=np.float64)
        m = float(np.max(vals))
        exps = np.exp(vals - m)
        Z = float(np.sum(exps)) + self.rm_eps
        probs = exps / Z

        for a, p in zip(legal_actions, probs):
            matched[a] = float(p)

        return r_pos.tolist(), matched