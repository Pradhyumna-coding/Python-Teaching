no = int(input("How many people are there:?"))

if no == 1:
    print("We suggest you to buy single pack")
elif no<4:
    print("We suggest you to buy regular pack")
elif no<6:
    print("We suggest you to buy family pack")
else:
    print("We suggest you to buy Large pack")