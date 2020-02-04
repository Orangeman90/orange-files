import random
from random import randint
import time
t = ["Rock", "Paper", "Scissors"]

comp = t[randint(0,2)]

player = False

while player == False:
    print("Do you want to play Rock, Paper, Scissors?")
    c = input()
    if c == "no":
        print("Oh well we'll play again some other day!")
        break
    elif c == "yes":
        print("ok")
        time.sleep(1)
        print("Rock")
        time.sleep(1)
        print("Paper")
        time.sleep(1)
        print("Scissors")
        time.sleep(1)
        print("SHOOT!")
        player = input()
        if comp == "Paper":
            if player == "Scissors":
                print("You Win " + player + " cuts " + comp)
            elif player == "Rock":
                print("You lose " + comp + " covers " + player)
        if comp == "Rock":
            if player == "Paper":
                print("You win " + player + " covers " + comp)
            elif player == "Scissors":
                print("You lose " + comp + " smashes " + player)
        if comp == "Scissors":
            if player == "Rock":
                print("You win " + player + " smashes " + comp)
            elif player == "Paper":
                print("You lose " + comp + " cuts " + player)









