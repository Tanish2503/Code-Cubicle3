
def game():
    import random
    yscore = 0
    cscore = 0
    playing = True

    while playing:
        computer = random.choice([1,0,-1])
        youstr = input("Enter your input (s for Snake, g for Gun, w for Water): ")
        youDict = {"s": 1, "g": 0, "w": -1}
        reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}
        you = youDict[youstr]

        print(f"You Chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

        if computer == you:
            print("DRAW")
        else:
            if (computer - you) == -1 or (computer - you) == 2:
                print("YOU LOSE")
                cscore += 1
            else:
                print("YOU WIN")
                yscore += 1

        print(f"Your Score: {yscore}")
        print(f"Opponents Score : {cscore}")

        with open("highscore.txt") as f:
            highscore = f.read()
            if (highscore != ""):
                highscore = int(highscore)
            else:
                highscore = 0

        if yscore > highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(yscore))
            print("NEW HIGHSCORE ACHIEVED")

        continue_playing = input("Do you want to continue playing? (yes/no): ")
        if continue_playing.lower() != "yes":
            playing = False

game()
