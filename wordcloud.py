"""
Created on Thu Jul 23 22:02:38 2020

@author: harinee
"""


!pip install wordcloud
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import sys



def calculate_frequencies(file_contents):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    
    text=file_contents
    text=text.lower()
    words_dict={}
    
    for punctuation in punctuations:
        text=text.replace(punctuation,"")
        
    words_list=text.split()    
    for word in words_list:
        if(word.isalpha() and word not in uninteresting_words):
            if(word not in words_dict):
                words_dict[word]=1
            else:
                words_dict[word]+=1
        
           
                
                
            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_dict )
    return cloud.to_array()

text='''Avul Pakir Jainulabdeen Abdul Kalam was an Indian aerospace 
scientist and politician who served as the 11th President of India 
from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu 
and studied physics and aerospace engineering.He spent the next four decades as a scientist 
and science administrator, mainly at the Defence Research and Development Organisation (DRDO) 
and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian 
space programme and military missile development efforts.He thus came to be known 
as the Missile Man of India for his work on the development of ballistic missile and launch 
vehicle technology.He also played a pivotal organisational, technical, and political role 
in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.'''
myimage = calculate_frequencies(text)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
