burgerCost = 45
pizzaCost = 90
iceCost = 20

noPerson = int(input("How many people are there:"))
noBurger = int(input("No. of burgers:"))
noPizza = int(input("No. of pizzas:"))
noIce = int(input("No. of Ice Creams:"))

burgerTotal = noBurger*burgerCost
pizzaTotal = noPizza*pizzaCost
iceTotal = noIce*iceCost

total = burgerTotal+pizzaTotal+iceTotal
print("The total is "+str(total))
average = total//noPerson
print("Each person has to pay "+str(average))
rem = total%noPerson
print("The remainder is "+str(rem))