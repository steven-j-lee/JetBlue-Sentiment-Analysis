import json
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize


sia = SentimentIntensityAnalyzer()
result = []

with open('quotes.json', 'r') as json_file:
    json_data = json.load(json_file)

data_length = len(json_data)

#test for json
#print (json_data[0])

for review in json_data:
#    opinions = sia.polarity_scores(review)
#    opinions['text'] = review
    opinions = sia.polarity_scores(review['text'])
    opinions['review'] = review
    result.append(opinions)
# result.append(sia.polarity_scores(review['text']))
#    print (review['text'])

#for sentence in sentences:
#    ss = sia.polarity_scores(sentence)
#    result.append(ss)

#pprint(result[:1],width=100)

#tokenize
for line in json_data:
    for parameters in line:
        tokens = word_tokenize(parameters)
