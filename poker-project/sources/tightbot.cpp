#include "tightbot.h"
#include "gamemanager.h"

TightBot::TightBot(const std::string& name, int chips, double tightness, double aggressiveness, int position)
    : Player(name, chips, position),
    _tightness(tightness),
    _aggressiveness(aggressiveness),
    _bluffFrequency(0.2) {
}

PlayerAction TightBot::makeDecision(const Gamestate& gameState, GameManager* gameManager) {

    double handStrength = evaluateHandStrength(gameState);

    if (handStrength < _tightness) {
        return PlayerAction(Action::fold);
    }

    if (shouldBeAggressive(gameState)) {
        return chooseAggressiveAction(gameState, gameManager);
    } else {
        return choosePassiveAction(gameState, gameManager);
    }
}

bool TightBot::shouldBeAggressive(const Gamestate& gameState) {
    double randomRoll = (std::rand() % 100) / 100.0;

    if (randomRoll < _aggressiveness) {
        return true;
    }
    return false;
}

PlayerAction TightBot::chooseAggressiveAction(const Gamestate& gameState, GameManager* gameManager) {
    auto legalActions = gameManager->getLegalActions(gameState.getCurrentPlayerIndex());
    int currentBet = gameState.getCurrentBet();
    double handStrength = evaluateHandStrength(gameState);


    if (currentBet == 0) {
        for (const auto& action : legalActions) {
            if (action.action == Action::bet) {
                int betSize = calculateBetSize(handStrength, gameState);
                return PlayerAction(Action::bet, betSize);
            }
        }
        return PlayerAction(Action::check);
    }

    double raiseChance = _aggressiveness * handStrength;

    double randomRoll = (rand() % 100) / 100.0;

    if (randomRoll < raiseChance) {
        for (const auto& action : legalActions) {
            if (action.action == Action::raise) {
                int raiseSize = calculateRaiseSize(currentBet, handStrength, gameState);
                return PlayerAction(Action::raise, raiseSize);
            }
        }
    }

    double callThreshold = getCallThreshold();

    if (handStrength > callThreshold) {
        for (const auto& action : legalActions) {
            if (action.action == Action::call) {
                return action;
            }
        }
    }

    return PlayerAction(Action::fold);
}

PlayerAction TightBot::choosePassiveAction(const Gamestate& gameState, GameManager* gameManager) {
    auto legalActions = gameManager->getLegalActions(gameState.getCurrentPlayerIndex());
    int currentBet = gameState.getCurrentBet();

    // if there is an option to check always check as the preferred passive action
    for (const auto& action : legalActions) {
        if (action.action == Action::check) {
            return action;
        }
    }

    double handStrength = evaluateHandStrength(gameState);
    double callThreshold = getCallThreshold();

    if (handStrength > callThreshold) {
        for (const auto& action : legalActions) {
            if (action.action == Action::call) {
                return action;
            }
        }
    }
    return PlayerAction(Action::fold);
}

double TightBot::getBaseStrength(int handRank) {
    switch(handRank) {
    case STRAIGHT_FLUSH: return 0.95;
    case FOUR_OF_A_KIND: return 0.90;
    case FULL_HOUSE: return 0.85;
    case FLUSH: return 0.75;
    case STRAIGHT: return 0.65;
    case THREE_OF_A_KIND: return 0.55;
    case TWO_PAIR: return 0.45;
    case ONE_PAIR: return 0.30;
    case HIGH_CARD: return 0.15;
    default: return 0.10;
    }
}


double TightBot::getCallThreshold() {
    double tightnessComponent = 0.2 + (_tightness * 0.5);
    double aggressivenessAdjustment = _aggressiveness * 0.1;

    return tightnessComponent - aggressivenessAdjustment;
}

double TightBot::evaluateHandStrength(const Gamestate& gameState) {
    Hand myHand = this->getHand();
    int handRank = myHand.getHandRank();
    auto kickers = myHand.getKickers();

    double baseStrength = getBaseStrength(handRank);
    double kickerBonus = 0.0;

    if (!kickers.empty()) {
        kickerBonus = (kickers[0] / 12.0) * 0.1;
    }

    return std::min(0.95, baseStrength + kickerBonus);
}

int TightBot::calculateBetSize(double handStrength, const GameState& gameState) {
    int potSize = gameState.getTotalPotValue();

    if (handStrength > 0.8) {

        return potSize;
    } else if (handStrength > 0.6) {

        return potSize * 0.6;
    } else if (handStrength > 0.4) {

        return potSize * 0.3;
    } else {
        double bluffRoll = (rand() % 100) / 100.0;
        if (bluffRoll < _bluffFrequency) {
            return potSize * 0.4;
        }
        return 0;
    }
}

int TightBot::calculateRaiseSize(int currentBet, double handStrength, const GameState& gameState) {
    if (handStrength > 0.8) {
        return currentBet * 3;
    } else if (handStrength > 0.6) {
        return currentBet * 2;
    } else {
        double bluffRoll = (rand() % 100) / 100.0;
        if (bluffRoll < _bluffFrequency) {
            return currentBet * 2;
        }
        return 0;
    }
}
