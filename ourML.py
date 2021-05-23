# ----------------- Machine Learning imports -----------------------

import nltk                                     #pip install nltk
from nltk.stem import WordNetLemmatizer
nltk.download("stopwords")
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
lemmatizer=WordNetLemmatizer()
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
tokenizer=RegexpTokenizer(r'\w+')
from sklearn.pipeline import Pipeline
import joblib                                   #pip install joblib
from sklearn import linear_model
import random

#-----------------------------------------------------------------

loaded_model_1 = joblib.load('Final_logistic_regression.sav')         #loads the model
#loaded_model_2 = joblib.load('Final_passive_aggressive.sav')           #loads second model

# -------------------  All the functions for preprocessing  -----------------------

stop_words = stopwords.words('english')

#DATA PREPROCESSING
def preprocessing(text):
    text=text.lower()
    text=tokenizer.tokenize(text)
    text=remove_stopwords(text)
    text=lemmatize_sentence(text)
    return text

def remove_stopwords(text):
    words=[w for w in text if  not w in stop_words]#to remove stop word such as is,an etc
    return words

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag((sentence))  
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:        
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

# ----------------------------------------------------------------------------------

def our_model_1(text):

    prediction_array=loaded_model_1.predict([text])#This gives the value  0 is real and 1 is fake

    prediction_proba_array = loaded_model_1.predict_proba([text])     #This gives the probability of 0 and 1 respectivel
    fake_proba = prediction_proba_array[0]
    real_proba = prediction_proba_array[0]
    fake = fake_proba.tolist()                                      #converting array to list
    real = real_proba.tolist()

    #       ***************************************************
    #Final prediction on given text
    if(prediction_array[0]==0):
        statement = "REAL " + str( fake[0]*100 )
            
    else:
        statement = "FAKE " + str( real[1]*100 )

    return statement


# def our_model_2(text):
#     model2_prediction = loaded_model_2.predict([text]).tolist()       #this variable is 0[REAL] or 1[FAKE]
    
#     if(model2_prediction[0]==0):
#         statement = "REAL " #+ str(float(random.randrange(30001, 79999))/10000)
#     else:
#         statement = "FAKE " #+ str(float(random.randrange(30001, 79999))/10000)

#     return statement