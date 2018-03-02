import random

def guess_a_number():
    secret_number = random.randint(1, 10)
    guess = ""
    guessTimes = 5
    print("I am thinking of a number between 1 and 10.")
    while guessTimes > 0:
        try:
            print("You have {} guesses left.".format(guessTimes))
            guess = int(input("What's the number? "))
        except:
            print("Number only, please!")
        else:
            if guess < secret_number:
                print("{} is too low.".format(guess))
                guessTimes -= 1
            elif guess > secret_number:
                print("{} is too high".format(guess))
                guessTimes -= 1
            else:
                break
    if guessTimes > 0:
        print("Yes! You win!")
    else:
        print("You ran out of guesses!")
    answer = ""
    while answer not in ["Y", "N"]:
        answer = input("Do you want to play again (Y or N)? ").upper()
    if answer == "Y":
        guess_a_number()
    else:
        print("Bye!")
        
guess_a_number()