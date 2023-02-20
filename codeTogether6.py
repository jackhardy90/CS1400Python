import random

names = []
guesses = []

name = 'start'
print ("Try and guess how much candy is in the jar!")
candyInJar = random.randint(1, 100)

#cheat code
print (candyInJar)

while name.lower() != 'q':
    name = input("What is your name or q to quit: ")
    if name == 'q':
        break
    names.append(name)
    guess = int(input("Enter your guess: "))
    guesses.append(guess)


winners = []
winners.append(names[0])
winningDist = abs(guesses[0] - candyInJar)

for i in range(1, len(guesses)):
    dist = abs(guesses[i] - candyInJar)
    if dist == winningDist:
        winners.clear()
        winningDist = dist
        winners.append(names[i])
print ("Candies in jar: ", candyInJar)
print ("Winners: ", winners)
for x in winners:
    print (x)
print ("Distance off: ", winningDist)
