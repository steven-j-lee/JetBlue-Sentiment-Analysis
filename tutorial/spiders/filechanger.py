import json
import re
import os
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

a=[]
with open('Wordreview.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a.append(row)
    posbag=a[1]
    negbag=a[0]

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
y=[0 for i in range(len(reviews))]
sat=0
sati=[["Date", "Reception"]]
_sati=[["",0] for i in range(60)]
sati+=_sati
p=1
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
            y[k]=1
            change+=1
            sat+=(1/change)
p=1
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
            y[k]-=1
            change+=1
            sat-=(1/change)
#print(sati)
with open('JetBlue-Data.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sati)
posrev={}
negrev={}

for i in range(len(reviews)):
    reviews[i]=re.sub(r'[^\w\s]', '', reviews[i])
    tokens = nltk.word_tokenize(reviews[i])
    tagged = nltk.pos_tag(tokens)
    tagged = [str(i[0]).lower() for i in tagged if i[1] in ['JJP', 'JJR', 'JJ']]
    if y[i]==-1:
        for j in tagged:
            if negrev.get(j):
                negrev[j]+=1
            else:
                negrev[j]=1
    elif y[i]==1:
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
os.remove("Wordreview.csv")
with open('Wordreview.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(negbag)
    writer.writerow(posbag)
