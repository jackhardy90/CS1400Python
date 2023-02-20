import math

aSide = 0
bSide = 0
cSide = 0

print ("Welcome to the Hypotenuse calculator!")
aSide = int(input("What number is side A?"))
bSide = int(input("What number is side B?"))


cSide = (aSide * aSide) + (bSide * bSide)

print ("The Hypotenuse is", math.sqrt(cSide))