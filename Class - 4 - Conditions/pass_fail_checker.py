marks = int(input("How many marks you got?:"))
total = int(input("Out of how many marks?:"))

perc = (marks/total)*100
print("Your percentage is "+str(perc))

if perc>35:
    print("\nCongratulations you pass :)")
    print("Keep it up.")
else:
    print("\nSorry you fail :(")
    print("Better luck next time.")