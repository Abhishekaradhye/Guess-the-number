# Guess the number 

import random

def guess(num):
  random_number = random.randint(1,num)
  a = 0
  while a != random_number:
    try:
      guess = int(input(f'Please enter any number from 1 to {num} here : '))
      if guess < random_number:
        print('You guessed TOO LOW. Guess again')
      elif guess > random_number:
        print('You guessed TOO HIGH. Guess again')
      else:
        print(f'Oh yess, you have guessed the correct number {random_number}, congrats !!')
        break
    except ValueError as e:
      print("You did not enter a valid number.")
    
random_number1 = random.randint(5,10)
b = 2
while b !=  random_number1:
  wish = input('Ready to play ?(y/n) : ')
  try:
    if wish.lower() == 'y':
      num1 = int(input('Enter the limit number here : '))
      print(guess(num1))
    else:
      print('...Thank you...')
      break
  except ValueError as e:
      print("You did not enter a valid number.")
