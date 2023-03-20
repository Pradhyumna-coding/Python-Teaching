import random

class Riddle:
    def __init__(self,question,answer):
        self.q = question
        self.a = answer

    def checkAnswer(self,userAnswer):
        if userAnswer.lower() == self.a.lower():
            return True
        else:
            return False

riddlesFile = open("Riddles.txt","r")

riddleGen = (line for line in riddlesFile.readlines())

riddles = []

for i in range(20):
    r = Riddle(next(riddleGen).removesuffix("\n"),next(riddleGen).removesuffix("\n").split(": ")[1])
    riddles.append(r)
    next(riddleGen)

print("Welcome to Riddle Game")



while True:
    points = 0

    print("Let's begin this game")
    random.shuffle(riddles)
    riddlesS = riddles[:10]
    for riddle in riddlesS:
        print(riddle.q)
        userAnswer = input()
        if riddle.checkAnswer(userAnswer):
            print("Correct Answer")
            points+=1
        else:
            print("Wrong Answer, Better luck next time.")

    print("\nPoints = "+str(points))
    print("Do you want to continue(y/n):")
    c = input()
    if c.lower() == "y":
        continue
    else:
        break