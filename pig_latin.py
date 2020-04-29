#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PIG LATIN
#If word starts with a vowel, add 'ay' to end
# apple --> appleay
#If word does not start with a vowel, put first letter at the end and add 'ay'
# word --> ordway

def pig_latin(word):
    '''
    This function returns a pig latin word
    If word starts with vowel, add 'ay' to end. 
        E.g. apple --> appleay
    If word does not start with a vowel, put the first letter at the end and add 'ay'
        E.g banana --> ananabay
    
    return string
    '''
    
    #get the first letter
    first_letter = word[0]
    
    if first_letter.lower() in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word

print(pig_latin('Hello'))
print(pig_latin('Bear'))
print(pig_latin('oranges'))


# In[ ]:




