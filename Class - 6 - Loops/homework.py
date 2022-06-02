
u1Points = 0
u2Points = 0

while True:
    u1Chances = 0
    u2Chances = 0
    #User 1
    u1No = int(input("User 1 , Enter the no:"))

    while True:
        u2Chances += 1
        u2Guess = int(input("User 2, Guess the no:"))
        if u2Guess == u1No:
            print("Correct Guess")
            print("You took "+str(u2Chances))
            break
    #User 2
    u2No = int(input("User 2 , Enter the no:"))

    while True:
        u1Chances += 1
        u1Guess = int(input("User 1, Guess the no:"))
        if u1Guess == u2No:
            print("Correct Guess")
            print("You took " + str(u1Chances))
            break

    if u1Chances>u2Chances:
        print("User 2 Wins")
        u2Points+=1
    elif u2Chances>u1Chances:
        print("User 1 Wins")
        u1Points+=1
    else:
        print('It is a tie')

    c = input("Do you want to continue(y/n)?").lower()
    if c == "n":
        break

print("User 1 Points : "+str(u1Points))
print("User 2 Points : "+str(u2Points))