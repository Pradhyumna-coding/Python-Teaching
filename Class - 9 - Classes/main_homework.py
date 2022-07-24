from Car import Car
from AudiCar import AudiCar

car1 = Car(150 , "Audi")
car1.accelearate(50)
print("Speed is "+str(car1.speed))
car1.accelearate(150)

car2 = AudiCar()
car2.accelearate(45)
print("Speed is "+str(car2.speed))
car2.applyBrakes()
print("Speed is "+str(car2.speed))