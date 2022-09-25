# Hangman Game

import random   

words = [ 'python', 'programming', 'teacher', 'humble', 'deerwalk', 'institute']  # a list of words is defined from which the game is played(P.S. we can list thousand of words into it using a online dictionary but the game will be more complex)

random_word = random.choice(words)                                                # selecting a random word
length_random_word = len(random_word)                                            

correct_character = ['_'] * length_random_word                                    # a list is defined to store the correct characters entered by user. now it just a list containing '_' as it's items(eg: ['_', '_', '_', '_'......])
used_correct_character = []                                                       # a list is initalized that stores correct characters already used by the user in the game
wrong_character = []                                                              # a list is initalized that stores wrong characters entered by user                      

print('I have chosen a {} letters word'.format(length_random_word))               # informing user the length of word the game(computer) chose

def update():                                                                     # a function is defined that will print the items of list(correct_character) in a single line as the parameter end() is assigned as space character(' ')
  for character in correct_character:
    print(character , end = ' ' )
  print('')                                                                       # this is to create output in a new line. print() here itself is empty but has end() parameter set as \n by default

update()                                                                          # invoking the function

while True:                                                                       # a infinite loop is run which will break when either when the user has won or when user entered 6 incorrect value
  guess_character = input("\nGuess the character:")                               # prompting user for guessing the character           

# if character guessed by user is present in the word  
  
  if guess_character in random_word:                                             
    index = 0                                                                     # initalizing the value of index which will help in updating the list(correct_character)
    
    for character in random_word:                                                 # the correct character guessed by user is then checked with all characters from the word
      if character == guess_character:                                            # if the character matches, the correct_character(list) is then assigned that character  
        correct_character[index] = guess_character
      index += 1                                                                  # increasing the value of index by 1
    
    update()                                                                      # invoking the fucntion 

    if '_' not in correct_character:                                              # while looping if there are no more '_' characters to be filled in the list, it means the user has won
      print('You Won!')
      break                                                                       # the loop is then broken and game has finished
    
    if guess_character in used_correct_character:                                 # if the user entered the correct character more than once, he/she is then informed that the character has already been entered
      print('Correct letter already used')
    else:
      used_correct_character.append(guess_character)                              # if user entered guessed the correct charcter, it is also stored in the list(used_correct_character). this will help us in informing the user when he/she enters the same character again

# if character guessed by user is not present in the word    
  
  else:
    
    if guess_character not in wrong_character:                                    # if the user enters wrong character, it is stored in a list called(wrong_character)
      wrong_character.append(guess_character)
      print('Wrong!')                                            
    else:                                                                         # if the user enters the same wrong character again, he/she is informed that they have already tried this wrong one 
      print('You already tried this one. It\'s wrong')
      
    
    if len(wrong_character) > 6:                                                  # if user enters wrong character more than 6 times, they will loose automatically 
      print('You loose')
      break
