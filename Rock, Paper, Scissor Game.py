# Make a rock, paper, scissor game

import random as r
while (True):
    c = r.choice(['rock', 'paper', 'scissor'])
    y = input("Enter your choice for 'rock, paper, scissor': ")
    if ((c=='rock' and y=='paper') or (c=='paper' and y=='scissor') or (c=='scissor' and y=='rock')):
        print("You won")
        print("Computer choice was:", c)
    elif (y == c):
        print("Match draw")
        print("Computer choice was:", c)
    else:
        print("You Lose")
        print("Computer choice was:", c)
    print("\n")
    print("Enter y for continue and n for exist")
    choice = input("Enter your choice: ")
    if (choice == 'y'):
        continue
    else:
        break
