# Day 10: Mini Project - Rock Paper Scissors Game

import random # `random` is a built-in Python module, which helps generate a random selection (in our case, the computer picking rock, paper, or scissors in the game).

print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

choices = ['rock', 'paper', 'scissors']
rounds_played = 0
user_score = 0
computer_score = 0

while True:
    user_choice = input("Your choice: ").lower()
    if user_choice == 'quit':
        break
    if user_choice not in choices:
        print("Invalid choice. Try again!\n")
        continue

    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!\n")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!\n")
        user_score += 1
    else:
        print("You lose!\n")
        computer_score += 1

    rounds_played += 1

print("Game Over!")
print(f"You: {user_score} | Computer: {computer_score} | Rounds Played: {rounds_played}")
print("Thanks for playing!")
