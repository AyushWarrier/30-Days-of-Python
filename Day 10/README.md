# Mini Project - Rock Paper Scissors Gane

A simple command-line implementation of the classic Rock, Paper, Scissors game. This was my first Python mini project after learning the basics, and it helped me practice user input, conditionals, loops, and using Python’s `random` module.

## What I used:
- `input()` function to take input of user (rock, paper or scissor).
- `while` loop for continuous play.
- `if-else` conditional statements to decide on next step (for example: if user didn't correctly input then to throw an error).
- `random.choice()` to randomize computer decisions.

## How it Works?
- The user types 'rock', 'paper', or 'scissors' to play a round.
- The computer randomly picks one of the three options.
- The winner is decided using standard Rock-Paper-Scissors rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- The game continues until the user types 'quit'.
- At the end, the total score and rounds played are displayed.
