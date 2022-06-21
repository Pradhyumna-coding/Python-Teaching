from Dog import Dog
import time

class GermanShepard(Dog):

    def __init__(self,name):
        super().__init__(name,"German Shepard")

    def jump(self,height):
        print("Jumping "+str(height)+" m")
        self.sitState = "Jumping"
        time.sleep(height/3)
        self.sitState = "Standing"
