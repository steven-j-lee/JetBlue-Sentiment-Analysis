import json
import re
#from nltk.classify import NaiveBayesClassifier
#from nltk.sentiment import SentimentAnalyzer
#from nltk.sentiment.util import *
import nltk
from nltk.corpus import subjectivity
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from pprint import pprint
import csv

result = []
posrev={}
negrev={}
posbag=[]
negbag=[]

with open('aquote.json', 'r') as json_file:
    json_data = json.load(json_file)

data_length = len(json_data)

#test for json

for i in range(len(json_data)):
    y=str(json_data[i])[12]
    y=y=='y'
    json_data[i]=str(json_data[i])[26:-2]
    while True:
        if str(json_data[i][0])==" " or str(json_data[i][0])=="|" or str(json_data[i][0])=="\"" or str(json_data[i][0])=="\'":
            json_data[i]=json_data[i][1:]
        else:
            break
    json_data[i]=re.sub(r'[^\w\s]', '', json_data[i])
    tokens = nltk.word_tokenize(json_data[i])
    tagged = nltk.pos_tag(tokens)
    tagged = [str(i[0]).lower() for i in tagged if i[1] in ['JJP', 'JJR', 'JJ']]
    if y==0:
        for j in tagged:
            if negrev.get(j):
                negrev[j]+=1
            else:
                negrev[j]=1
    else:
        for j in tagged:
            if posrev.get(j):
                posrev[j]+=1
            else:
                posrev[j]=1

for i in negrev.items():
    if i[1]>=len(negrev)**0.35 and (posrev.get(i[0])==None or posrev.get(i[0])<len(posrev)**0.30):
        negbag.append(i[0])
for i in posrev.items():
    if i[1]>=len(posrev)**0.35 and (negrev.get(i[0])==None or negrev.get(i[0])<len(negrev)**0.30):
        posbag.append(i[0])

date=[]
reviews=[]
with open('test-cases.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            date.append(row[3])
            reviews.append(row[10])
            line_count += 1
sat=0
sati=[["",0] for i in range(60)]
p=0
mprev=date[0][5:7]
for k in range(len(reviews)):
    l=date[k]
    m=l[5:7]
    if m!=mprev:
        sati[p][0]=m+"-"+l[0:4]
        sati[p][1]+=sat
        sat=0
        p+=1
    mprev=m
    i=reviews[k]
    change=0
    for j in posbag:
        if j in i:
            change+=1
            sat+=(1/change)
p=0
sat=0
mprev=date[0][5:7]
for k in range(len(reviews)):
    l=date[k]
    m=l[5:7]
    if m!=mprev:
        sati[p][0]=m+"-"+l[0:4]
        sati[p][1]+=sat
        sat=0
        p+=1
    mprev=m
    i=reviews[k]
    change=0
    for j in negbag:
        if j in i:
            change+=1
            sat-=(1/change)
print(sati)
