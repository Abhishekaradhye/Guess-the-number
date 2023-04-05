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
    
def play_with_computer():
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

def let_computer_play(num):
  low = 1
  high = num  
  while True:
    guess = random.randint(low,high)
    print("Computer's guess : ",guess)
    feedback = input(f"\nDid computer guess too low 'l', too high 'h' or correct 'c' ? : ").lower()
    if feedback =='h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
    else:
      print(f"Yay, Computer guessed that number {guess} correctly !!!")
      break
    
def main():
  print('How would you like to play ?\n1. Play with computer    or\n2. Let computer play to guess your number.')
  ch = input("Enter your choice '1' or '2' : ")
  if ch == '1':
    print(play_with_computer())
  elif ch == '2':
    num2 = int(input('Give computer a limit number here : '))
    print(let_computer_play(num2))
main()
