# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:02:22 2018

@author: AlexWang
"""
#%%
import ast
import nltk
from nltk.corpus import stopwords

list_tuple = []
with open("processed.txt", 'r', encoding='utf-8') as file:
    for line in file:
        a = ast.literal_eval(line)
        list_tuple.append(a)
        
        
def generate_feature(sentence):
    features = {}
    features["keyword_appearance(criminal legislation)"] = 0
    features["keyword_appearance(regulatiom compliance)"] = 0
    features["keyword_appearance(cirt)"] = 0
    features["keyword_appearance(standards)"] = 0
    features["keyword_appearance(certification)"] = 0
    features["keyword_appearance(policy)"] = 0
    features["keyword_appearance(roadmap)"] = 0
    features["keyword_appearance(responsible_agency)"] = 0
    features["keyword_appearance(national_benchmarking)"] = 0
    features["keyword_appearance(standardisation development)"] = 0
    features["keyword_appearance(manpower development)"] = 0
    features["keyword_appearance(professional certification)"] = 0
    features["keyword_appearance(agency certification)"] = 0
    features["keyword_appearance(intra-state cooperation)"] = 0
    features["keyword_appearance(intra-agency cooperation)"] = 0
    features["keyword_appearance(public sector partnership)"] = 0
    features["keyword_appearance(international cooperation)"] = 0
    features["keyword_appearance(national legislation)"] = 0
    features["keyword_appearance(un convention and protocal)"] = 0
    features["keyword_appearance(institutional support)"] = 0
    features["keyword_appearance(reporting mechanism)"] = 0
    
    
    sentence_l = word_stemming(sentence)
    
    for word in sentence_l:
        if word in "criminal legislation":
             features["keyword_appearance(criminal legislation)"] += 1
        elif word in "regulation compliance":
             features["keyword_appearance(regulatiom compliance)"] += 1
        elif word in "cirt":
             features["keyword_appearance(cirt)"] += 1
        elif word in "standards":
             features["keyword_appearance(standards)"] += 1
        elif word in "certification":
             features["keyword_appearance(certification)"] += 1
        elif word in "policy":
            features["keyword_appearance(policy)"] += 1
        elif word in "roadmap for governance":
            features["keyword_appearance(roadmap)"] += 1
        elif word in "responsible agency":
            features["keyword_appearance(responsible_agency)"] += 1
        elif word in "national benchmarking":
            features["keyword_appearance(national_benchmarking)"] += 1
        elif word in "standardisation development":
            features["keyword_appearance(standardisation development)"] += 1
        elif word in "manpower development":
            features["keyword_appearance(manpower development)"] += 1
        elif word in "professional certification":
            features["keyword_appearance(professional certification)"] += 1
        elif word in "agency certification":
            features["keyword_appearance(agency certification)"] += 1
        elif word in "intra-state cooperation":
            features["keyword_appearance(intra-state cooperation)"] += 1
        elif word in "intra-agency cooperation":
            features["keyword_appearance(intra-agency cooperation)"] += 1
        elif word in "public sector partnership":
            features["keyword_appearance(public sector partnership)"] += 1
        elif word in "international cooperation":
            features["keyword_appearance(international cooperation)"] += 1
        elif word in "national legislation":
            features["keyword_appearance(national legislation)"] += 1
        elif word in "un convention and protocal":
            features["keyword_appearance(un convention and protocal)"] += 1
        elif word in "institutional support":
            features["keyword_appearance(institutional support)"] += 1
        elif word in "reporting mechanism":
            features["keyword_appearance(reporting mechanism)"] += 1
##more need to be implemented 
     
    return features
    
    
    
def word_stemming(sentence):
    sentence = sentence.replace('\n','')
    tokens = nltk.word_tokenize(sentence)
    swords = stopwords.words('english')
    words = [w.lower() for w in tokens if w.isalpha() if w.lower() not in swords]
    
    p = nltk.PorterStemmer()
    result = [p.stem(w) for w in words]
    
    return result



featuresets = [(generate_feature(sentence), category) for (sentence, category) in list_tuple]
train_set,test_set = featuresets[3093:], featuresets[:1000]
classifier = nltk.NaiveBayesClassifier.train(train_set)


classifier.classify(generate_feature('The following principle shall apply: “Self-commitment if possible, regulation if necessary."'))
#print(nltk.classify.accuracy(classifier, test_set))

