import time

class Dog:
    sitState = "Standing"

    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

        self.introduce()

    def run(self):
        print("Running..")
        time.sleep(2)
        print("Finished running")
    def sit(self):
        if self.sitState == "Sitting":
            print("I am already sitting")
            return
        print("Sitting")
        self.sitState = "Sitting"
    def stand(self):
        if self.sitState == "Standing":
            print("I am already standing")
            return
        print("Standing")
        self.sitState = "Standing"

    def introduce(self):
        print("My name is "+self.name)
        print("I am of breed "+self.breed)
        print("I am "+self.sitState)