import random

options = ["Stone","Paper","Scissor"]

uPoints = 0
compPoints = 0

while True:
    for i in range(3):
        print(str(i+1)+"."+options[i])

    uSelect = int(input("Enter the no. of selected item:"))

    comSelect = random.randint(1,3)

    print("The computer chose "+options[comSelect-1])

    if uSelect == 1 and comSelect == 2:
        print("So the computer wins")
        compPoints+=1
    elif uSelect == 1 and comSelect == 3:
        print("So you win")
        uPoints+=1
    elif uSelect == 2 and comSelect == 1:
        print("So you win")
        uPoints+=1
    elif uSelect == 2 and comSelect == 3:
        print("So computer wins")
        compPoints+=1
    elif uSelect == 3 and comSelect == 1:
        print("So computer wins")
        compPoints+=1
    elif uSelect == 3 and comSelect == 2:
        print("So you win")
        uPoints+=1
    else:
        print("So, it is a tie")
        uPoints+=1
        compPoints+=1

    con = input("Do you want to continue(y/n):").lower()

    if con == "n":
        break

print("You got "+str(uPoints)+" points")
print("The computer got "+str(compPoints)+" points")
if uPoints>compPoints:
    print("So you win the match")
elif uPoints<compPoints:
    print("So the computer wins the match")
else:
    print("So it is a tie")