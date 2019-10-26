import json
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer

#sia = SIA()
result = []

with open('quotes.json', 'r') as json_file:
    json_data = json.load(json_file)

data_length = len(json_data)

#test for json
print (json_data[0])
