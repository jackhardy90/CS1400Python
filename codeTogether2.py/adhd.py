print ("Rate the following activities on a scale from 1 to 5 on how your child does with the following activities 5 being very well, 1 being not well at all.")

score = 0

score += int(input("Timely in doing and turning in homework: "))
score += int(input("Manages sequential tasks: "))
score += int(input("Organizes their time effectively: "))
score += int(input("Keeps room organized: "))
score += int(input("Attention to detail: "))

print(score)

if score < 15:
    print ("your child may have mild ADHD tendencies")
else:
    print ("Your child is in the normal range")