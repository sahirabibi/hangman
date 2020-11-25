# hangman game 
import random 
import collections

words = ['code', 'display','network', 'rotate', 
            'dictionary','python']


def hangman(word_list):   
    hangman_body = ['head', 'torso', 'right arm', 'left arm', 'right leg', 'left leg'] 
    print('Selecting word...')
    w = random.choice(word_list)
    word = list(w) 
    results = collections.Counter(word)   
    print('The game has begun! Hidden word has', len(word), 'letters in it.')
# game play
    guesses = []
    correct_needed = len(word)
    correct_guessed = 0
    hidden = ['_' for i in range(len(word))]
    new_list = []
    while len(hangman_body) != 0:
        choice = input('Guess a letter...')
        print("Guessed letters:", guesses)
        if choice in guesses:
            print("You've already guessed", choice, "try again...")
            continue
        elif choice in word:
            correct_guessed += 1   
            print('Correct', choice, 'is in the hidden word.')
            print(choice, 'appears', results[choice], 'times.')
            guesses.append(choice)
            new_list.append(choice)
            for i in new_list:
                while i in word:
                    ind = word.index(i)
                    word[ind] = '-'
                    new_list.append(i)
                    hidden[ind] = i
            print(' '.join(hidden))
            if correct_guessed == correct_needed:
                print('You guessed the word!')
                print(' '.join(hidden))
                break
            else:
                continue
        elif choice not in word:
            if choice in guesses:
                print('You already guessed that...')
            else:
                print('False', choice, 'is not in the hidden word.')      
                print('Drawing', hangman_body[0],'...')
                hangman_body.remove(hangman_body[0])
                if len(hangman_body) == 0:
                    print("Oh no! You've guessed incorrectly too many times! Hangman is complete.")
                    print("The hidden word was: ", w)
                    break
                else:
                    continue
        continue
    print("Thank you for playing!")


hangman(words)





