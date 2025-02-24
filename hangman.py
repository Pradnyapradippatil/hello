import random
 
def making_a_guess(guess, chosen_word, blank_list):
    correct_guess = False
    for x in range(len(chosen_word)):
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
    if not correct_guess:
        print(f"There is no {guess}, sorry.")
        return False  
    return True  
 
HANGMANPICS = [''' 
  +---+
  |   |
      |
      |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
chosen_word = list(random.choice(word_list))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0

#-----------------c-----------------------------------------------------------------------------

print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{''.join(blank_list)}\nMake a guess? ")
if making_a_guess(guess, chosen_word, blank_list):
    print(''.join(blank_list))
else:
    update_display += 1

print(HANGMANPICS[update_display])
while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    if making_a_guess(guess, chosen_word, blank_list):
        print(''.join(blank_list))
    else:
        update_display += 1
        print(HANGMANPICS[update_display])

if update_display == 6:
    print("GAME OVER.")
