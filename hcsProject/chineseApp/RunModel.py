# Import approximately 1 million packages lol
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
nltk.download('punkt')
#from tqdm import tqdm
#import seaborn as sns
import pandas as pd
import numpy as np
import pickle
import joblib
import json
import nltk
import nltk
import csv
import re
import os



def trainModel():

    # Load the data
    df = pd.read_csv('/home/heatherbaier/hcsProject/chineseApp/DataClean.csv')

    # Drop null values
    df['beer/style'].dropna(inplace=True)
    df['review/text'].dropna(inplace=True)
    df = df[0:10000]

    # Encode the beer styles for training
    le = LabelEncoder()
    y = le.fit_transform(df[['beer/style']])
    xtrain, xval, ytrain, yval = train_test_split(df['review/text'], y, test_size=0.2, random_state=1693)

    # vectorize
    vectorizer = CountVectorizer(decode_error = "replace")
    vec_train = vectorizer.fit_transform(xtrain)

    # return the two models
    return [vectorizer, le]


# Function to predict beer styles from the user input 
def predictInput(wordList):

    # Read in trained models
    vectorizer = trainModel()[0]
    le = trainModel()[1]
    model = joblib.load('/home/heatherbaier/hcsProject/chineseApp/model.sav')  

    # create a join list string of the users inputted adjectives
    wordList = [" ".join(wordList)]

    # predict the users inputed adjectives
    adj = vectorizer.transform(wordList)
    probs = model.predict_proba(adj)
    best_n = np.argsort(probs, axis=1)[:,-5:]
    best_n = best_n.reshape((5,1))
    toReturn = le.inverse_transform(best_n)

    # return the list of predicted beer styles 
    return toReturn


# Function to get the best review of the recommended beer
def getReviews(style):

    # Read in the csv, subset it to the recommended style and sort so the best reviews are on the top of the dataframe
    df = pd.read_csv('/home/heatherbaier/hcsProject/chineseApp/DataClean.csv')
    df = df[df['beer/style'] == style]
    df = df.sort_values(by = 'review/taste', ascending = False)
    
    # Convert to the reviews to a list
    reviews = df['review/text'].to_list()

    # Form a string for to print for the beer review and return it
    toReturn = 'Customer Review: "' + str(reviews[0]) + '"'

    return toReturn

