""" -1 for water
0 for gun
1 for snake 
"""
import random

computer = random.choice([1,0,-1])
youstr = input("Enter your input :")
youDict = {"s":1,"g":0,"w":-1}
reverseDict = {1:"Snake",0:"Gun",-1:"Water"}
you = youDict[youstr]

print(f"You Chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("DRAW")
else:
    if((computer - you) == -1 or (computer - you)== 2):
        print("YOU LOSE")
    else:
        print("YOU WIN")
    # if computer == 1 and you == 0:          1
    #     print("YOU WIN")
    # elif computer == 1 and you == -1:       2
    #     print("YOU LOSE")
    # elif computer == 0 and you == 1:       -1
    #     print("YOU LOSE")
    # elif computer == 0 and you == -1:       1
    #     print("YOU WIN")
    # elif computer == -1 and you == 0:      -1
    #     print("YOU LOSE")
    # elif computer == -1 and you == 1:      -2
    #     print("YOU WIN")
    # else:
    #     print("Something went wrong")
