import random
generatedno = random.randint(0,10)

while generatedno:
    user_guess = int(input("Enter your guess : "))
    if user_guess==generatedno:
        print("You guessed the no., it is " , generatedno)
        print("Thank you for playing.")
        quit()
    else:
        print("Incorrect guess")