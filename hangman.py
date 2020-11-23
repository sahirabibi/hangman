# hangman game 
import random 

word_box = ['cat', 'bat', 'hat', 'display', 'network', 'rotate', 'dictionary']

def select_word(word_list):
    return random.choice(word_list)


print(select_word(word_box)) 






