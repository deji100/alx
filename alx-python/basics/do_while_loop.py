number = 4

while True:

    try:
        guess = input("Guess a number between 1 and 10: ")
        if int(guess) == number:
            print("You guessed right.")
            break
    except ValueError:
        print("U didn't enter a number.")
