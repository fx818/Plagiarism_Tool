from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

def cosine_similarity(a1,a2):
    from math import sqrt
    sum = 0
    sum1 = 0
    sum2 = 0
    for i , j in zip(a1,a2):
        sum += i*j
        sum1 += i*i
        sum2 += j*j

    cs = sum / (sqrt(sum1) * sqrt(sum2))
    return cs

x = stopwords.words('english')

sent1 = input("Enter the first sentence : ").split()
sent1 = [b.lower() for b in sent1]

sent2 = input("Enter the second sentence : ").split()
sent2 = [b.lower() for b in sent2]

# StopWord removal
word1 = [ww for ww in sent1 if ww not in x]
word2 = [ww for ww in sent2 if ww not in x]

# Stemming for smooth and better performance
stemmer = PorterStemmer()
word1 = [stemmer.stem(word) for word in word1]
word2 = [stemmer.stem(word) for word in word2]

# Joining the sentence back
word1 = ' '.join(word1)
word2 = ' '.join(word2)


document = [word1,word2]


vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(document)
row = bow_model.toarray()

row = bow_model.toarray().T
column = vectorizer.get_feature_names_out()


y={}

for i in range(len(column)):
    y[column[i]] = row[i]

row = bow_model.toarray()

q1 = cosine_similarity(row[0], row[1])
print(f"The similarity between the sentence is given in form of cosine similarity as : {q1}")

print()

print("The bag of word model for the same is given here : ")
pd.DataFrame(y , index = ['correct answer' , 'Submitted Answer'])
