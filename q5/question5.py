#!/usr/bin/env python
# coding: utf-8

# In[6]:


def reverse_words(sentence):
    words_list = sentence.split()
    
    reversed_list = words_list[::-1]
    
    reversed_sentence = " ".join(reversed_list)
    
    return reversed_sentence

if __name__ == "__main__":
    sentence1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    reversed_sentence1 = reverse_words(sentence1)
    print("첫번째 문장 결과 :\n",reversed_sentence1)
    print()

    sentence2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    reversed_sentence2 = reverse_words(sentence2)
    print("두번째 문장 결과 :\n",reversed_sentence2)


# In[ ]:




