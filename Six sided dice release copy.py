import random



while 1==1:
 n = random.randint(1, 6)
 c = input("Guess a number on a six sided dice ")
 g = int(c)
 if int(g) in range(7, 9000000000):
    print("Whoops you didnt put a number that is on a 6 sided dice")
 if n == 1 and g == 1:
  print("The dice landed on 1. You win")
 if n == 2 and g == 2:
  print("The dice landed on 2. You win")
 if n == 2 and g == 3:
  print("The dice landed on 2. You lose")
 if n == 4 and g == 6:
  print("The dice landed on 4. You lose")
 if n == 4 and g == 5:
  print("The dice landed on 4. You lose")
 if n == 5 and g == 6:
  print("The dice landed on 5. You lose")
 if n == 3 and g == 3:
  print("The dice landed on 3. You win")
 if n == 4 and g == 4:
  print("The dice landed on 4. You win")
 if n == 5 and g == 5:
  print("The dice landed on 5. You win")
 if n == 6 and g == 6:
  print("The dice landed on 6. You win")
 if n == 2 and g == 1:
  print("The dice landed on 2. You lose")
 if n == 5 and g == 4:
  print("The dice landed on 5. You lose")
 if n == 5 and g == 3:
  print("The dice landed on 5. You lose")
 if n == 5 and g == 2:
  print("The dice landed on 5. You lose")
 if n == 5 and g == 1:
  print("The dice landed on 5. You lose")
 if n == 2 and g == 4:
  print("The dice landed on 2. You lose")
 if n == 2 and g == 5:
  print("The dice landed on 2. You lose")
 if n == 2 and g == 6:
  print("The dice landed on 2. You lose")
 if n == 3 and g == 1:
  print("The dice landed on 3. You lose")
 if n == 3 and g == 2:
  print("The dice landed on 3. You lose")
 if n == 3 and g == 4:
  print("The dice landed on 3. You lose")
 if n == 3 and g == 5:
  print("The dice landed on 3. You lose")
 if n == 3 and g == 6:
  print("The dice landed on 3. You lose")
 if n == 4 and g == 1:
  print("The dice landed on 4. You lose")
 if n == 4 and g == 2:
  print("The dice landed on 4. You lose")
 if n == 4 and g == 3:
  print("The dice landed on 4. You lose")
 if n == 6 and g == 1:
  print("The dice landed on 6. You lose")
 if n == 6 and g == 2:
  print("The dice landed on 6. You lose")
 if n == 6 and g == 3:
  print("The dice landed on 6. You lose")
 if n == 6 and g == 4:
  print("The dice landed on 6. You lose")
 if n == 6 and g == 5:
  print("The dice landed on 6. You lose")
 if n == 1 and g == 2:
  print("The dice landed on 1. You lose")
 if n == 1 and g == 3:
  print("The dice landed on 1. You lose")
 if n == 1 and g == 4:
  print("The dice landed on 1. You lose")
 if n == 1 and g == 5:
  print("The dice landed on 1. You lose")
 if n == 1 and g == 6:
  print("The dice landed on 1. You lose")      