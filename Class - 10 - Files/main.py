class UserDetails:
    def __init__(self,name,number,city):
        self.name = name
        self.number = number
        self.city = city

userFilename = "userDetails.txt"

firstTime = False
try:
    userFile = open(userFilename,"r")
except:
    firstTime = True
    userFileC = open(userFilename,"w")

    userDetails = UserDetails("","","")

    userDetails.name = input("What is your name?:")
    userDetails.number = input("What is your number?:")
    userDetails.city = input("Whats is your city name?:")

    userFileC.write(userDetails.name+"\n"+userDetails.number+"\n"+userDetails.city)

    print("Thank you")

"""
Name
Number
City
"""

if not firstTime:
    userString = userFile.read()
    userDetails = UserDetails("","","")

    userList = userString.split("\n")
    #["name","number","city"]
    userDetails.name = userList[0]
    userDetails.number = userList[1]
    userDetails.city = userList[2]

    print("Name : "+userDetails.name)
    print("Number : "+userDetails.number)
    print("City : "+userDetails.city)