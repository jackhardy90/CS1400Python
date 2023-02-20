import math

yesScore = 0
answer = ""

print ("How strong is your password?")
print ("Does your password contain ....")

answer = (input("at least 9 characters in length? y/n :"))

if (answer == "y" or answer == "Y"):
    yesScore += 1
elif (answer == "n" or answer == "N"):
    yesScore -= 1


answer = (input("a mixture of letters and numbers? y/n :"))

if (answer == "y" or answer == "Y"):
    yesScore += 1
elif (answer == "n" or answer == "N"):
    yesScore -= 1
    
answer = (input("a mixture of upper case and lower case letters? y/n :"))


if (answer == "y" or answer == "Y"):
    yesScore += 1
elif (answer == "n" or answer == "N"):
    yesScore -= 1

answer = (input("at least 1 symbol? y/n :"))

if (answer == "y" or answer == "Y"):
    yesScore += 1
elif (answer == "n" or answer == "N"):
    yesScore -= 1
    
if (yesScore <= 1):
    print("Very weak password")
elif (yesScore == 2):
    print("Weak password")
elif (yesScore == 3):
    print("Strong password")
elif (yesScore == 4):
    print("Very strong password")
