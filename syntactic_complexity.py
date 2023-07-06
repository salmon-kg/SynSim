#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:57:20 2022

@author: salman
"""

import os
from spacy.lang.en import English
import spacy
import nltk.corpus
import nltk.stem.snowball
import string
from spacy.pipeline import DependencyParser
import csv

path = os.path.expanduser('PATH')
ssents=0
TS=0.05
VS=0.3
CS=0.4
threshold=1.25

nlp = spacy.load('en_core_web_sm')
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def tkn_proc(sent):
    tokens = [token.lower().strip(string.punctuation) for token in tokenize(sent) \
                if token.lower().strip(string.punctuation) not in stopwords]
    return(tokens)

def tkntag(token):
    print(token.text, "->", token.dep_)
    
def set_custom_boundaries(doc):
    pattern_a = ['no', 'num']
    for token in doc[:-1]:
        if token.text in pattern_a and doc[token.i + 1].text == '.':
            doc[token.i + 2].is_sent_start = False
    return doc

def getSentences(text):
    nlp = English()
    nlp.add_pipe('sentencizer')
    document = nlp(text)
    return [sent.text.strip() for sent in document.sents]

def tknpos(token):
    print(token.text, "->", token.pos_)
    
def complexity_dep_sent(text):
   # print("Running Dependency Based Syntactic Complexity Measurement for Sentence.")
    TKN=0
    VRB=0
    CNJ=0
    TKN = len(tkn_proc(text))
    tokens = nlp(text)
    for token in tokens:
        #tkntag(token)
        if "ROOT" in token.dep_:
            VRB+=1
        elif "attr" in token.dep_:
            VRB+=1
        elif "conj" in token.dep_:
            VRB+=1
        elif "punct" in token.dep_ and token.text!=".":
             CNJ+=1
        elif "cc" in token.dep_:
            CNJ+=1
        else:
            continue
            
    #print('Verbs:',VRB, ' Tokens:',TKN, '& Conjunctions:',CNJ)
    
    cmplexity = ((TKN*TS)+(VRB*VS)+(CNJ*CS))
    
    # if cmplexity<threshold:
    #     print('Sentence:',text)
    #     print('Verbs:',VRB, ' Tokens:',TKN, '& Conjunctions:',CNJ)
    #print('Total Complexity of Sentence:', cmplexity)
    return(cmplexity)


def complexity_pos_sent(text):
   # print("Running POS Based Syntactic Complexity Measurement for Sentence.")
    TKN=0
    VRB=0
    CNJ=0
    TKN = len(tkn_proc(text))
    tokens = nlp(text)
    for token in tokens:
        #tknpos(token)
        if "VERB" in token.pos_:
            VRB+=1
        elif "CCONJ" in token.pos_:
            CNJ+=1
        elif "SCONJ" in token.pos_:
            CNJ+=1
        elif "PUNCT" in token.pos_:
            if "," in token.text:
                CNJ+=1
        else:
            continue
         
    cmplexity = ((TKN*TS)+(VRB*VS)+(CNJ*CS))
    
    # if cmplexity<threshold:
    #     #print('Sentence:',text)
    #     print('Verbs:',VRB, ' Tokens:',TKN, '& Conjunctions:',CNJ)
    #print('Total Complexity of Sentence:', cmplexity)
    return(cmplexity)
        
        
def complexity_pos_par(doc):
   # print("Running POS Based Syntactic Complexity Measurement for Paragraph.")
    DS=0
    cmplexity=0
    sentences = getSentences(doc)
    #print(sentences)
    for sentence in sentences:
        TKN=0
        VRB=0
        CNJ=0
        TKN = len(tkn_proc(sentence))
        tokens = nlp(sentence)
        for token in tokens:
            #tknpos(token)
            if "VERB" in token.pos_:
                VRB+=1
            elif "CCONJ" in token.pos_:
                CNJ+=1
            elif "SCONJ" in token.pos_:
                CNJ+=1
            #elif "PUNCT" in token.pos_:
             #   if "," in token.text:
              #      CNJ+=1
            else:
                continue
             
        cmplexity = (TKN*TS)+(VRB*VS)+(CNJ*CS)
        DS+=1
    #print('Total Complexity:',cmplexity,' In Total',DS, 'Sentences of Document')
    cmplexity = cmplexity/DS
    return(cmplexity)

ssents=0
def complexity_dep_par(doc):   
    #print("Running Dependency Based Syntactic Complexity Measurement for Paragraph.")
    DS=0
    cmplexity=0
    sentences = getSentences(doc)
    #print(sentences)
    for sentence in sentences:
        TKN=0
        VRB=0
        CNJ=0
        TKN = len(tkn_proc(sentence))
        tokens = nlp(sentence)
        for token in tokens:
            #tkntag(token)
            if "ROOT" in token.dep_:
                #print(token)
                #print('Verb Found')
                VRB+=1
            elif "conj" in token.dep_:
                VRB+=1
            elif "cc" in token.dep_:
                #print('Conjunction Found')
                CNJ+=1
            else:
                continue
             
        cmplexity = ((TKN*TS)+(VRB*VS)+(CNJ*CS))
        DS+=1
    #print('Total Complexity:',cmplexity,' In Total',DS, 'Sentences of Document')
    cmplexity = cmplexity/DS
    return(cmplexity)


# inp = ('Mantell was born in Bridgwater, Somerset. Mantell studied at the University of Bath.')
# compx = complexity_par(inp)
# print('Total Complexity Level of Sentence:',compx)


with open(path+'sim/gptoutsim.csv') as csv_file:    
    sents = 0
    total_complexity=0
    complex_sent=0
    simple_sent=0
    total_complexity_pos=0
    complex_sent_pos=0
    simple_sent_pos=0

    
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(sents)
        compx = complexity_dep_sent(row[1])
        total_complexity+=compx
        if compx>threshold:
            complex_sent+=1
        else:
            #print(row[0],':',compx)
            simple_sent+=1
   
        compxp = complexity_pos_sent(row[1])
        total_complexity_pos+=compxp
        if compxp>threshold:
            complex_sent_pos+=1
        else:
            #print(row[0],':',compx)
            simple_sent_pos+=1
        sents += 1
    print("--------------------------------------------------")
    print(f'Algorithm WEIGHTS:\t Token={TS} \t Verb={VS} \t Conjunction={CS}')
    print("--------------------------------------------------")
    print(f'Total Compound & Complex Sentences: {sents}')
    print("--------------------------------------------------")
    print("Dependency Based Syntactic Complexity Measurement for Complex Sentences.")
    print(f'Average Syntactic Complexity Per Sentence= {total_complexity/sents}')
    print(f'IDENTIFIED: Complex Sentences = {complex_sent} and Simple Sentences = {simple_sent}')
    print(f'Accuracy = {(complex_sent/sents)*100}%')
    
    print("--------------------------------------------------")
    print("POS Based Syntactic Complexity Measurement for Complex Sentences.")
    print(f'Average Syntactic Complexity Per Sentence= {total_complexity_pos/sents}')
    print(f'IDENTIFIED: Complex Sentences = {complex_sent_pos} and Simple Sentences = {simple_sent_pos}')
    print(f'Accuracy = {(complex_sent_pos/sents)*100}%')
    print("--------------------------------------------------")

with open(path+'sim/gpt-sents-cs-sim.csv') as csv_file:    
    sents = 0
    total_complexity=0
    complex_sent=0
    simple_sent=0
    total_complexity_pos=0
    complex_sent_pos=0
    simple_sent_pos=0
    ssents=0
    depcomp = []
    poscomp = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(sents)
        #ssentences = getSentences(row[1])
        ssents+=1
        compx=0
        compxp=0

        compx = complexity_dep_sent(row[4])
        total_complexity+=compx
        if compx>threshold:
            #print(row[5])
            odep =str(f"{row[0]}:{row[4]}")
            complex_sent+=1
            with open(path + 'sim/depcmplxGPT.txt', 'a') as file1:
                file1.write(odep)
                file1.write("\n")
        else:
            #print(row[0],':',compx)
            simple_sent+=1
   
        compxp = complexity_pos_sent(row[4])
        total_complexity_pos+=compxp

        if compxp>threshold:
            complex_sent_pos+=1
            opos = str(f"{row[0]}:{row[4]}")
            with open(path + 'sim/poscmplxGPT.txt', 'a') as file2:
                file2.write(opos)
                file2.write("\n")
        else:
            #print(row[0],':',compx)
            simple_sent_pos+=1
        sents += 1


    

                

    print("**************************************************")
    print("--------------------------------------------------")
    print(f'Total Simplified Sentences = {ssents}')
    print("--------------------------------------------------")
    print("Dependency Based Syntactic Complexity Measurement for Simplified Sentences.")
    print(f'Average Syntactic Complexity Per Sentence= {total_complexity/ssents}')
    print(f'IDENTIFIED: Complex Sentences = {complex_sent} and Simple Sentences = {simple_sent}')
    print(f'Accuracy = {(simple_sent/ssents)*100}%')
    
    print("--------------------------------------------------")
    print("POS Based Syntactic Complexity Measurement for Simplified Sentences.")
    print(f'Average Syntactic Complexity Per Sentence= {total_complexity_pos/ssents}')
    print(f'IDENTIFIED: Complex Sentences = {complex_sent_pos} and Simple Sentences = {simple_sent_pos}')
    print(f'Accuracy = {(simple_sent_pos/ssents)*100}%')
    print("--------------------------------------------------")



