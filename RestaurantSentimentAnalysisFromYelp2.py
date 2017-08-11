#Get 60 restaurants by looping through the API by incrementing the offset parameter by 20 (0,20,40).
#Calculate the polarity and subjectivity for each one and display in a bar graph.
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

#initialize the parameters for search for offset 0
params2 = {"term":"sushi","lang":"en","limit":20,"offset":0,"sort":1}
val2 = api.search("New York, NY",params2)

#initialize the parameters for search for offset 20
params3 = {"term":"sushi","lang":"en","limit":20,"offset":20,"sort":1}
val3 = api.search("New York, NY",params3)

#initialize the parameters for search for offset 40
params4 = {"term":"sushi","lang":"en","limit":20,"offset":40,"sort":1}
val4 = api.search("New York, NY",params4)

df2 = pd.DataFrame()

#get name and review for 0-19 businesses and calculate polarity and subjectivity
for v in val2.businesses:
    wiki = TextBlob(v.snippet_text)
    r =pd.Series([v.name,v.snippet_text,wiki.polarity,wiki.subjectivity])
    df2 = df2.append(r, ignore_index=True)

#get name and review for 20-39 businesses and calculate polarity and subjectivity
for v in val3.businesses:
    wiki = TextBlob(v.snippet_text)
    r =pd.Series([v.name,v.snippet_text,wiki.polarity,wiki.subjectivity])
    df2 = df2.append(r, ignore_index=True)

#get name and review for 40-59 businesses and calculate polarity and subjectivity    
for v in val4.businesses:
    wiki = TextBlob(v.snippet_text)
    r =pd.Series([v.name,v.snippet_text,wiki.polarity,wiki.subjectivity])
    df2 = df2.append(r, ignore_index=True)

#plot graph for polarity and subjectivity
df2.columns = ('name','review','polarity','sub')
df2.plot.bar(x='name', y='polarity')
df2.plot.bar(x='name', y='sub')
