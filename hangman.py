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
    slice_wrd=word[:]
    n= slice_wrd.count(userIp)
    index_list=[]
    for i in range (n):
        index=slice_wrd.index(userIp)
        index_list.append(index)
        slice_wrd[index]='@'
        
        
    return  index_list
    

def unmask(word,g_wrd,index_list):
    for i in index_list:
        g_wrd[i]=word[i]

    return g_wrd



def main(str_word=get_secret_word()):
    tries=10
    word=list(str_word)
    
    init_msk_str=mask_secret_word(str_word)
    mskd_list=list(init_msk_str)
    
    wrng_g=''
    g_str=''.join(mskd_list)
    
   # print(word)
    
    while tries:
        
        print(f"\n {g_str} \n")
        print(f"Number of tries left: {tries}")
        print(f"Wrong guesses so far: {wrng_g}")
        
        usr_input=input("Enter your guess:  ")
        
        if len(usr_input)!=1:
            print("Enter one Char. only!")
            continue
        
        if usr_input in word:
            
            index_list=check(word,usr_input)
            mskd_list=unmask(word,mskd_list,index_list)
            g_str=''.join(mskd_list)
            
            print(g_str)
            
            
        else:
            
            print("Wrong Guess:")
            wrng_g=wrng_g+usr_input
            
            
            tries=tries-1
            
        if str_word==g_str:
            
            print("Congratulations! You WON.")
            break
            
        if tries == 0:
            
            print(f"Too bad! The secret word was {str_word}")
                
                
if __name__=='__main__':
    main()
