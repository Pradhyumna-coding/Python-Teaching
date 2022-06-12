def findFactors(number):
    factors = []
    for no in range(1,number+1):
        if number%no == 0:
            factors.append(no)
    return factors

def isPrime(number):
    factors = findFactors(number)
    if len(factors) == 2:
        return True
    return False

def displayList(listU):
    for item in listU :
        print(item,end=",")
    print()

no = int(input("Enter the number:"))

factors = findFactors(no)

print("The factors are:")
displayList(factors)
if isPrime(no):
    print("It is a prime number")
else:
    print("It is a composite number")