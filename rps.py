import random

choices = ["rock", "paper", "scissors"]


computerMove = random.choice(choices)
result = ""

myMove = input("Chose rock, paper or scissors: ").lower()

while myMove not in choices:

    myMove = input("Chose rock, paper or scissors: ").lower()

if myMove == "rock" and computerMove == "paper":
    result = "you lose."
elif myMove == "rock" and computerMove == "scissors":
    result = "you win."

elif myMove == "paper" and computerMove == "rock":
    result = "you win"
elif myMove == "paper" and computerMove == "scissors":
    result = "you lose"

elif myMove == "scissors" and computerMove == "rock":
    result = "you lose"
elif myMove =="scissors" and computerMove == "paper":
    result = "you win"

print("You choose " + myMove + ", computer choose " + computerMove + ", " + result)