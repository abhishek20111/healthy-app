# hi this game is scissor , paper & rock

list=["S","P","R"]
import random
ras=random.choice(list)
#print(f"computer make - {ras}")

tatt=10
hatt=0
cp=0
hp=0



while tatt   > hatt:
    sua = input("enter your choice \nScissor-S\nPaper-P\nRock-R   \n")
    hun = sua.capitalize()

    if hun=="S" and ras=="P":
        print(f"You Won \nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt-hatt}")
        hp=hp+1

    elif hun=="S" and ras=="R":
        print(f"You Loss\nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt-hatt}")
        cp=cp+1

    elif hun=="P" and ras=="R":
        print(f"You Won \nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt-hatt}")
        hp = hp + 1

    elif hun=="R" and ras=="S":
        print(f"You Won \nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt-hatt}")
        hp = hp + 1

    elif hun == "P" and ras == "S":
        print(f"You Loss\nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt - hatt}")
        cp = cp + 1

    elif hun == "R" and ras == "P":
        print(f"You Loss\nAs Computer choice {ras}")
        print(f"The Number of attemed left {tatt - hatt}")
        cp = cp + 1

    # elif hun == S and ras == S:
    #     print(f"No Point , both are same\nAs Computer choice {ras}")
    #     print(f"The Number of attemed left {tatt - hatt}")
    #
    # elif hun == R and ras == R:
    #     print(f"No Point , bouth are same\nAs Computer choice {ras}")
    #     print(f"The Number of attemed left {tatt - hatt}")
    #
    # elif hun == P and ras == P:
    #     print(f"No Point , bouth are same\nAs Computer choice {ras}")
    #     print(f"The Number of attemed left {tatt - hatt}")

    elif hun==ras:
        print("Tie Same choice")
        print(f"The Number of attemed left {tatt - hatt}")

    else:
        print("Any invalide inpute")
        continue

    hatt=hatt+1
    print(f"No of chance left -  {tatt-hatt} ")


if cp>hp:
    print("Computer Win -- You Loss")

elif hp>cp:
    print("You Win -- Computer Loss")

else:
    print("the match is tie")


print(f"Your Point is {hp}\nComputer Point {cp}\n")

print("Game over")


print("for any suggestion say to whitecoder")