import time

password = 123456
loggedIn = False

while True:
    for i in range(0,5):
        uPassword = int(input("Enter the password:"))
        if uPassword == password:
            loggedIn = True
            print("You have logged in")
            break
        else:
            print("Enter correct password")
    if loggedIn:
        break
    else:
        time.sleep(5)