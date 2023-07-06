#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:19:14 2022

@author: salman
"""

import os
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string
import csv
from spacy.lang.en import English

path = os.path.expanduser(PATH)

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def is_ci_token_stopword_set_match(a, b):
    
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    #print('Similarity:',ratio)
    return (ratio)

def getSentences(text):
    nlp = English()
    nlp.add_pipe('sentencizer')
    document = nlp(text)
    return [sent.text.strip() for sent in document.sents]


def cosine_simialarity(a, b):
    
    l1 =[]
    l2 =[]

    tokens_a = [token.lower().strip(string.punctuation) for token in tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    
    rvector = set(tokens_a).union(tokens_b)
    for w in rvector:
        if w in tokens_a: l1.append(1) # create a vector
        else: l1.append(0)
        if w in tokens_b: l2.append(1)
        else: l2.append(0)
    
    c = 0
    for i in range(len(rvector)):
        c+= l1[i]*l2[i]
        
    x = float((sum(l1)*sum(l2))**0.5)
    
    if x!=0:
        cosine = c/x
    else:
        cosine = 0
    #print("similarity: ", cosine)

    return (cosine)

Simlarity_Cosine=0
Simlarity_Jaccard = 0
line_n=1
ssents=0
with open(path+'output_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        s1 = row[0]
        s2 = row[1]
        Jsim = is_ci_token_stopword_set_match(s1,s2)
        #print('S1:',s1,' and S2:',s2)
        #print(line_n,':Similarity:',Jsim)
        Simlarity_Jaccard+=Jsim
        
        Csim = cosine_simialarity(s1,s2)
        #print(line_n,':Cosine Similarity:',Csim)
        Simlarity_Cosine+=Csim
        line_n+=1
        ssentences = getSentences(s1)
        for s in ssentences:
            ssents+=1
# print('Sentence 1:',a)
# print('Sentence 2:',b)
# Jsim = is_ci_token_stopword_set_match(a, b)



print("**************************************************")
print("PERFORMANCE OF MODEL")
print("--------------------------------------------------")
print("Total Compared Sentence Sets: 720")
print(f'Total Sentences Compared: 2171 VS {ssents}')
print("--------------------------------------------------")
print('Jaccard Similarity:', Simlarity_Jaccard/720)
print("--------------------------------------------------")
print('Cosine Similarity:', Simlarity_Cosine/720)
print("--------------------------------------------------")
