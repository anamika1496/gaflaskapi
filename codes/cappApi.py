# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import flask
import json
from nltk import word_tokenize
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

class WordPreprocess:
    
    def __init__(self):
        self.num_of_words = 2
    
    def top_words(self, text):
        
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word)>2]
        text_df = pd.DataFrame ({'words':word_tokens})
        count_dict = dict(text_df.words.value_counts())
        top_words = list(count_dict.keys())[:self.num_of_words]
        return top_words
    
    def last_words(self, text):
        
        word_tokens = word_tokenize(text)
        word_tokens = [word for word in word_tokens if len(word)>2]
        text_df = pd.DataFrame ({'words':word_tokens})
        count_dict = dict(text_df.words.value_counts())
        last_words = list(count_dict.keys())[-self.num_of_words:]
        return last_words
    
#if __name__=='__main__':
#    word_process_obj = WordPreprocess()
#    word_process_obj.num_of_words = 3
#    text = """Amazon.com, Inc., is an American multinational technology company based in Seattle, Washington, that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is considered one of the Big Four technology companies along with Google, Apple, and Facebook"""
#    top_words = word_process_obj.top_words(text)