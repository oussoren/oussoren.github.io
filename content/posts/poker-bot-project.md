---
title: "Poker Bot Project"
date: 2025-08-14
draft: false
tags: ["programming"]
---

# Poker Bot

Built an Object-Oriented Poker Environment that tracks everything from player action history to hand strength and runs smoothly in all three standard rulesets. Created standard bots of all playstyles(from loose and aggressive to tight and defensive) based off of standard heuristics. Currently working on implementing a ML Entity to be trained off of public player action history and a collection of game data from professional poker matches.

## Features

- **Hand Evaluation**: Accurately ranks poker hands from high card to royal flush
- **Pot Odds Calculation**: Determines the mathematical probability of winning
- **Betting Strategy**: Makes optimal betting decisions based on game theory
- **User Interface**: Clean Qt-based interface for interaction

## Technical Details

The bot is written in C++ for performance and uses the Qt framework for the GUI. The core algorithms handle:
- Card parsing and hand evaluation
- Probability calculations
- Decision tree analysis for betting strategies(currently implementing)

## Source Code

The complete source code is available in my [GitHub repository](https://github.com/oussoren/oussoren.github.io/tree/main/poker-project).
