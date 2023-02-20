costEstimator = 0
guestsUnder3 = 0
jumpingGuests = 0
seasonPasses = " "
numOfSeasonPassesJumper = 0
regularSeasonPasses = 0


print ("Welcome to the kangaroo zoo calculator!")
print ("What would you like to do?")

while costEstimator != 2:
    costEstimator = (input("1. Cost Estimator 2.Exit "))
    if costEstimator == "1":
        guestsUnder3 = int (input("How many guests are 3 and under? "))
        if guestsUnder3 >= 1:
            guestsUnder3 = guestsUnder3 * 6
        jumpingGuests = int (input("How many guests other guests will be jumping? "))
        if jumpingGuests >= 1:
            jumpingGuests = jumpingGuests * 12
        seasonPasses = input("Would you like to buy additional season passes? Y/N ")
        if seasonPasses == "Y" or seasonPasses == "y":
            numOfSeasonPassesJumper = int (input("How many passes for jumpers 3 and under? "))
            if numOfSeasonPassesJumper >= 1:
                numOfSeasonPassesJumper = numOfSeasonPassesJumper * 45
            regularSeasonPasses = int(input("How many regular passes? "))
            if regularSeasonPasses >= 1:
                regularSeasonPasses = regularSeasonPasses + 80
                totalWithPasses = guestsUnder3 + jumpingGuests + numOfSeasonPassesJumper + regularSeasonPasses
                print ("Cost estimation:$",totalWithPasses)
        elif seasonPasses == "N" or "n":
            totalNoPasses = guestsUnder3 + jumpingGuests
            print ("Cost estimation:$",totalNoPasses)
    elif costEstimator == "2":
        print("Thanks for using the cost estimator!")   
    