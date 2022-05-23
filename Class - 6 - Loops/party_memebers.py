members = ["abc","def","ghi","jkl"]
print("The members who were present were:-")
for member in members:
    print(str(members.index(member)+1)+"."+member,end=" , ")
