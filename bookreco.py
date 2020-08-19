import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
import re
import string
import random
import sqlite3
import nltk
import pickle as pkl
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('stopwords')


con = sqlite3.connect("C:\\Users\\ss727\\Downloads\\db.sqlite3")

# Load the data into a DataFrame
df2 = pd.read_sql_query("SELECT * from catalog_book", con)
# Function for removing NonAscii characters
def _removeNonAscii(s):
    return "".join(i for i in s if  ord(i)<128)
# Function for converting into lower case
def make_lower_case(text):
    return text.lower()
# Function for removing stop words
def remove_stop_words(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text
# Function for removing punctuation
def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text
#Function for removing the html tags
def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)
# Applying all the functions in description and storing as a cleaned_desc
df2['cleaned_desc'] = df2['summary'].apply(_removeNonAscii)
df2['cleaned_desc'] = df2.cleaned_desc.apply(func = make_lower_case)
df2['cleaned_desc'] = df2.cleaned_desc.apply(func = remove_stop_words)
df2['cleaned_desc'] = df2.cleaned_desc.apply(func=remove_punctuation)
df2['cleaned_desc'] = df2.cleaned_desc.apply(func=remove_html)

def train(df):
    indices = pd.Series(df.index, index = df['title'])
    with open('ind','wb') as f: pkl.dump(indices,f)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['cleaned_desc'])
    sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
    with open('filename','wb') as f: pkl.dump(sg, f)


def recommend3(title):
    with open('ind','rb') as f: indices2 = pkl.load(f)
    with open('filename','rb') as f: arrayname1 = pkl.load(f)
    idx=indices2[title]
    sig = list(enumerate(arrayname1[idx]))
    sig = sorted(sig, key=lambda x: x[1], reverse=True)
    sig = sig[1:6]
    book_indices = [i[0] for i in sig]
    rec = indices2.iloc[book_indices]
    return list(rec.index)


#train(df2)
#print(list(recommend3('Scion of Ikshvaku').index))
print('-'*50)
print(recommend3('The Doomsday Conspiracy'))