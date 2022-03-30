import time
import string
import random

#welcome user
name = input('Hello! What is your name? ')
print('Hello, '+ name +'! Lets play Hangman!')
print(' ')

#wait 1 second
time.sleep(1)
print('You can guess one letter at a time. Start guessing...')

#define word that will be guessed
def hangman():
  #set list of words
  words_list = ['yellow', 'sun', 'moon', 'strawberry']
  #choose random word from list above
  word = random.choice(words_list).lower()
  # save letters of the chosen random word
  word_letters = set(word) 
  # define letters
  alphabet = set(string.ascii_lowercase)
  # keep track of what the user has guessed
  used_letters = set() 
  # set number of tries (lives)
  lives = 7
  
  # LOOP CONDITION
  while len(word_letters) > 0 and lives > 0:
  # Keep track of used letters, create list where every single letter is shown and letters that were not guessed are dashes
  #what current word is (i.e.: W_RD)
    word_list = [letter if letter in used_letters else '_'   for letter in word]
    print('Current word: ',' '.join(word_list))
    print('You have', lives, ' lives left. You have already used these letters: ', ' '.join(used_letters))
    #get user input
    user_letter = input('Guess a letter: ').lower()
      #TO KEEP TRACK OF LETTERS ENTERED BY USER
      #if this is a valid letter not used yet, add in the used letters set
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      #if the letter is in the word, remove from used letters
      if user_letter in word_letters:
          word_letters.remove(user_letter)
      #if user attempts incorrect letter, he loses 1 life
      else:
        lives = lives - 1
        print('Letter is not in the word.')
      #if letter is in used letters, it is invalid because he just used it
    elif user_letter in word_letters:
        print('You have already used this letter. Try again')
    else:
        print('Incorrect character. Try again.')

  if lives == 0:
    print('You could not guess the word ',word.upper(),'.You died.')
  else:
    print('Congratulations! You have guessed the word ',word.upper(),'!')
    
if __name__ == '__main__':
    hangman()
