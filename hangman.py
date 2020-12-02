# hangman game
import random
import collections

words = ['code', 'display', 'network', 'rotate',
         'dictionary', 'python']
hangman_body = ['head', 'torso', 'right arm',
                'left arm', 'right leg', 'left leg']


print('Selecting word...')
# select a random word from word and turn into list
w = random.choice(words)
word = list(w)
print('The game has begun! Hidden word has', len(word), 'letters in it.')
# count how many times each letter is repeated in word
results = collections.Counter(word)
# empty list to store guesses made my user
guesses = []
# hidden list replaced each letter in the word with '_' to present to user
hidden = ['_' for i in range(len(word))]
repeats = []


def play_game():
    # ask for a letter
    print("Currently guessed letters:", guesses)
    choice = input('Guess a letter... to quit, press the spacebar\n')
    if choice == ' ':
        end_game()
    else:
        if len(choice) > 1: 
            print('Only input one letter at a time.')
            play_game()
        else:
            if choice in guesses:
                repeat_guess(choice)
            else:
                if choice not in word:
                    wrong_guess(choice)
                else:
                    correct_guess(choice)

                           
def correct_guess(choice):
    print('Correct', choice, 'is in the hidden word.')
    print(choice, 'appears', results[choice], 'times.')
    guesses.append(choice)
    # replace '-' in hidden word with the choice, do this with each time letter appears in word
    repeats.append(choice)
    for i in repeats:
        while i in word:
            # count every time letter appears in word and replace it
            ind = word.index(i)
            word[ind] = '-'
            repeats.append(i)
            hidden[ind] = i
    print(' '.join(hidden))
    if '_' not in hidden:
        winner = True
        end_game(winner)
    else:
        play_game()


def wrong_guess(choice):
    guesses.append(choice)
    print('False', choice, 'is not in the hidden word.')
    print('Drawing', hangman_body[0], '...')
    hangman_body.remove(hangman_body[0])
    if len(hangman_body) == 0:
        winner = False
        end_game(winner)
    else:
        play_game()


def repeat_guess(choice):
    print(f'You already guessed {choice}...try again.')
    play_game()


def end_game(winner):
    if winner == False:
        print("Oh no! You've guessed incorrectly too many times! Hangman is complete.")
        print("The hidden word was: ", w)
    elif winner == True:
        print('You guessed the word! Congrats!')
    else:
        print('Thanks for playing!')


play_game()






