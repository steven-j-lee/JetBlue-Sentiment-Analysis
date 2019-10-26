import json
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


sia = SIA()
result = []

with open('quotes.json', 'r') as json_file:
    json_data = json.load(json_file)

data_length = len(json_data)

#test for json
print (json_data[0])


#sia.all_words(json_data)
for review in json_data:
    opinions = sia.polarity_scores(review)
    opinions['text'] = review
    results.append(opinions)
    print (review['text'])

#pprint (results[:3], width = 500)
#sentences=["You guys suck!"]

#for sentence in sentences:
#    ss = sia.polarity_scores(sentence)
#    result.append(ss)

#pprint(result[:1],width=100)
