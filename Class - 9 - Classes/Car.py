class Car:
    speed = 0

    def __init__(self,topSpeed,brandName):
        self.topSpeed = topSpeed
        self.brandName = brandName

    def applyBrakes(self):
        self.speed = 0

    def accelearate(self,speedToAccelearate):
        if self.speed+speedToAccelearate<=self.topSpeed:
            self.speed = self.speed+speedToAccelearate
        else:
            print("Cannot accelerate")