# hangman game 
import random 

word_box = ['cat', 'bat', 'hat', 'display', 'network', 'rotate', 'dictionary']

def select_word(word_list):
    word = random.choice(word_list)
    print('A word has been selected')
    return word 



print(select_word(word_box)) 






