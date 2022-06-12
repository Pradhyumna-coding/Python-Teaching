description = {
    "football" : "Football is a sport in which the ball is played by kicking the ball with the foot and that is why it is called football."+
                 " It is an outdoor game played between two rival teams.",
    "cricket" : "Cricket is a bat-and-ball game played between two teams of eleven players",
    "tennis" : "Tennis game is a ball-played game between 2 teams where the ball is passed using from each court",
    "volleyball" : "Volleyball is a team sport in which two teams of six players are separated by a net.",
    "hockey" : "Hockey is a game where the ball is passed using a stick to make a goal."
}

game = input("Which game do you want to know about?:").lower()
if game in description.keys():
    print(description[game])
else:
    print("Sorry we don't have the description in our database.")