#sum = 0
#
#for i in range(1, 20, 2):
#    sum =+ i
#    print(sum)

play = " "
beachorJungle = " "
jungleAnswer = " "
beachAnswer = " "

play = input("Do you want to go on an adventure? Y/N ")

if play == "y" or play == "Y":
    print("Welcome to the game")
    beachorJungle = input("Would you like to play in the jungle or on the beach? B=beach, J=jungle " )
    if beachorJungle == "J" or beachorJungle == "j":
        jungleAnswer = input("You come face to face with a giant leapard. What do you do? R=run, F=fight " )
        if jungleAnswer == "r" or jungleAnswer == "R":
            print ("You were able to escape, but with one leg missing....")
        elif jungleAnswer == "F" or jungleAnswer == "f":
            print ("You fight corageously and defeat the leapard, and manage to escape the jungle alive")
    elif beachorJungle == "B" or beachorJungle == "b":
        beachAnswer = input("You find yourself in a hungry canabalistic tribe. What do you do? E=eat with them  F=fight them all until death ")
        if beachAnswer == "e" or beachAnswer == "E":
            print ("You were able to blend in, assimilate and forget your past self. Becoming a canabal yourself....")
        elif beachAnswer == "f" or beachAnswer == "F":
            print ("You fight couragously and defeat many canabals, but in the end you were eaten by the tribe")
elif play == "N" or play == "n":
    print("You're no fun...")


