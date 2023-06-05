import random

while True:
 user_input = input("Guess a number on a D20 ")

 if not user_input.isnumeric():

  print("This isn't a number!") 

  continue

 guess_rolled = int(user_input)

 dice_rolled = random.randint(1, 20)

 won = guess_rolled == dice_rolled

 outcome = "You win" if won else "You lose"

 print(f"The dice landed on {dice_rolled}. {outcome}")