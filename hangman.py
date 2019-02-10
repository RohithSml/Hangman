# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)

def mask_secret_word(word):
    length=len(word)
    masked_wrd=''
    for i in range (length):
        masked_wrd+='*'

    return masked_wrd

def check(word,userIp):
    n=word.count(userIp)
    index_list=[]

    for i in range (n):
        index=word.index(userIp)
        index_list.append(index)
        
    return  index_list
    


    
