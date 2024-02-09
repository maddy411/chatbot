import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
nltk.download('popular', quiet=True)

import pandas as pd
data =pd.read_csv('microsoft.csv')
question =data['Question'].tolist()
answer =data['Answer'].tolist()

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up" ,"hey" ,"how are you")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


GI = ("how are you")
GR = ["i'm fine" ,"good,how can i help you!"]
def greet(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_I:
            return random.choice(GREETING_R)

def responses(user):
    response =''
    question.append(user)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(question)
    val = cosine_similarity(tfidf[-1], tfidf)

    id1 =val.argsort()[0][-2]
    flat = val.flatten()
    flat.sort()
    req = flat[-2]


    for word in response.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

    if(response =='how are you'):
        return random.choice(GREETING_R)

    for word in response.split():
        if word.lower() in ["nice" ,"good" ,"good job" ,"okay" ,"cool" ,"great"]:
            return "smile.."

    if(req==0):
        response =response +"I am sorry! I don't understand you"
        return response
    else:
        response = response +answer[id1]
        question.remove(user)
        return response
command =1
while(command):
    v = input("Enter your value: ")
    if( v=="exit"):
        command =0
    else:
        print(responses(str(v)))
