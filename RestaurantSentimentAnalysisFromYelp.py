#Get 20 of the restaurants from a city of your choice. 
#Download the reviews for each one (yelp only gives one review per restaurant from the API).
#Calculate the Polarity and Sentiment for each review and create a Line Graph.

import pip
pip.main(["install","yelp"])
pip.main(["install","textblob"])
from textblob import TextBlob

#use appropriate values
ckey = ""
csecret = ""
token = ""
tokensecret = ""

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd

auth = Oauth1Authenticator(
    consumer_key=ckey,
    consumer_secret=csecret,
    token=token,
    token_secret=tokensecret
)

api = Client(auth)

#initialize the parameters for search
params2 = {"term":"sushi","lang":"en","limit":20,"offset":0,"sort":1}
val2 = api.search("New York, NY",params2)

df2 = pd.DataFrame()

#get name and review for businesses and calculate polarity and subjectivity
for v in val2.businesses:
    wiki = TextBlob(v.snippet_text)
    r =pd.Series([v.name,v.snippet_text,wiki.polarity,wiki.subjectivity])
    df2 = df2.append(r, ignore_index=True)

#plot line graph of subjectivity and polarity
df2.columns = ('name','review','polarity','sub')
df2
df2.plot.line(x='name',y=['polarity','sub'],rot = 90)


