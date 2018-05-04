# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:11:04 2018

@author: AlexWang
"""
#%%
import nltk
import uuid
import json

infile = open("UN test.txt", 'r')
text = infile.read()
my_list = []

sent_text = nltk.sent_tokenize(text)
for i in range(len(sent_text)):
    new_dic = {}
    sent_text[i] = sent_text[i].replace('\n', ' ')
    new_dic['ID'] = str(uuid.uuid4())
    new_dic['Text'] = sent_text[i]
    
    my_list.append(new_dic)

with open('output.json', 'w') as fp:    
    for i in my_list:
        json.dump(i, fp)
        fp.write('\n')
    
    


