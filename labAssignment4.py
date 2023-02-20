import math
import random

randX = random.randint(1, 10)
randY = random.randint(1, 10)
missiles = 0



for i in range (10):
    missiles += 1
    x = int(input("Please input a number for X "))
    y = int(input("Please input a number for Y "))
    userX = x
    userY = y
    calculateX = [userX, userY]
    calculateY = [randX, randY]
    if x == randX and y == randY:
        print("You sunk the ship! You Win!")
        break
    elif x != randX and y == randY:
        print("You missed! Try Again!")
        print ("You were", math.dist(calculateX, calculateY), "meters away!")
    elif x == randX and y != randY:
        print("You missed! Try again!")
        print ("You were", math.dist(calculateX, calculateY), "meters away!")
    elif missiles == 10:
        print("You ran out of missiles! GAME OVER")
        break
    elif x != randX and y != randY:
        print ("You Missed! Try Again!")
        print ("You were", math.dist(calculateX, calculateY), "meters away!")
