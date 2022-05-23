import random
no = random.randint(1,11)
userNo = 0
chances = 0

while True:
    userNo = int(input("Guess the number:"))
    if userNo!=no:
        print("Sorry, Guess again")
        chances+=1
        if chances == 5:
            print("Sorry you lost your chances")
            break
    else:
        break
print("\nThe number was "+str(no))
print("Thank you")