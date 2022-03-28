import random
n = random.randint(1,100)
guess = int(input('Enter an integer from 1 to 100: '))
while n!='guess':
  if guess < n:
    print ('guess is LOW')
    guess = int(input('Enter another guess:'))
  elif guess > n:
    print ('guess is HIGH')
    guess = int(input('Enter another guess:'))
  else:
    print('You guessed it!')
    break
