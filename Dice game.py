import random

while True:
    user_input = input("Guess a number on a six-sided dice ")

    # string.isnumeric(): tells you if a string is comprised purely of numbers or not
    if not user_input.isnumeric():

        # let the user know they made a mistake
        print("This isn't a number!")

        # return to the beginning of the while loop
        continue

    # convert the user_input to an integer for easy comparison
    guess_rolled = int(user_input)

    dice_rolled = random.randint(1, 6)

    # if guess_rolled == dice_rolled, the won variable will be True.
    won = guess_rolled == dice_rolled

    # this is a tenary operator. great for one-liners
    outcome = "You win" if won else "You lose"

    # this is a f-string. great for substitution
    print(f"The dice landed on {dice_rolled}. {outcome}")