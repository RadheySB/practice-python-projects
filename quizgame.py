print('Welcome to my computer quiz')
playing = input('Do you wanna play the game? ')
if playing.lower() != 'yes':
    quit()
print("Okay! Let's play the game <3..")
score = 0
answer = input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
answer1 = input('What does UPS stand for? ')
if answer1.lower() == "uninterrupted power supply ":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
answer2 = input('What does GPU stand for? ')
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
answer3 = input('What does RAM stand for? ')
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")
print("You got "+str(score)+" questions correct.")
print("You got "+str((score/4)*100)+"% questions correct.")
