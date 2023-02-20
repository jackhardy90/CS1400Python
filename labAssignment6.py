strScores = input("What were your bowling scores? (Seperate your bowling scores with commas): ").split(",")
scores = []

for i in strScores:
    scores.append(int(i))
print (scores)

totalScore = 0
scoreIndex = 0

for frame in range(10):  
    if scores[scoreIndex] == 10:
        totalScore += scores[scoreIndex] + scores[scoreIndex + 1] + scores[scoreIndex + 2]
        scoreIndex += 1
    elif scores[scoreIndex] + scores[scoreIndex + 1] == 10:
        totalScore += scores[scoreIndex] + scores[scoreIndex + 1] + scores[scoreIndex + 2]
        scoreIndex += 2
    else:
        totalScore += scores[scoreIndex] + scores[scoreIndex + 1]
        scoreIndex += 2
print (totalScore)





#    while counter < 10:
#        counter = 0
#        counter = counter = 1
#    if input == 10:
#        totalScore += input
#    elif input < 10:
#        break