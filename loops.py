# Mantej Lamba, ITP 116
# 2259394598
# Mon, Wed 11 - 11:50

import random

# Please complete the code in the follwoing function.
def guess():
    # asking for lower and upper bounds
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    # displaying the upper and lower bounds
    print ("I'm thinking of a number between " + str(lower) + " and " + str(upper))
    # finding random number between the two bounds
    num = random.randint(lower, upper)
    # setting guess to False to run through loop
    guess = False
    # while guess is not True then proceed
    while guess != True:
        # getting guess input
        guessNum = int(input("Guess a number: "))
        # checking conditionals and displaying the necessary output
        if (guessNum < num):
            print(str(guessNum) + " is too low")
        elif (guessNum > num):
            print(str(guessNum) + " is too high")
        elif (guessNum > upper or guessNum < lower):
            print(str(guessNum) + " is outside the range of possible values.")
        # once the number is guessed, change guess to True to break the loop
        elif (guessNum == num):
            guess = True
            print("You guessed it!")




def main():
    guess()

    answer = input("Do you want to play again? Enter y for yes.")
    while answer == "y":
        guess()
        answer = input("Do you want to play again? Enter y for yes.")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()