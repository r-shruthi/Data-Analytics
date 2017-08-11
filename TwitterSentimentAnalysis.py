#Twitter Data Sentiment Analysis
#get screen names of users with high and low polarity tweets
import pip
pip.main(["install","twitter"])
pip.main(["install","textblob"])
from textblob import TextBlob

import json
from twitter import Twitter 
from twitter import OAuth 
from twitter import TwitterHTTPError 
from twitter import TwitterStream 
from pandas.io.json import json_normalize

#use appropriate values
AccessToken = ''
AccessTokenSecret = ''
ConsumerKey = ''
ConsumerSecret = ''
oauth = OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret)

#create Twitter object
api = Twitter(auth=oauth)

q1='tsla'
search_results1 = api.search.tweets(q=q1,count = 100)
statuses1 = json_normalize(search_results1, 'statuses')
polarity1 = []

#loop through text to get sentiment analysis
for str in statuses1.text:
    wiki = TextBlob(str)
    p = wiki.polarity
    polarity1.append(p)

#add polarity column to dataframe
statuses1['polarity'] = polarity1

#get statuses with high polarity
hi_pol = statuses1[statuses1['polarity'] >= 0.7]
#hi_sn_1 = json_normalize(hi_pol_1['entities'],'user_mentions')

#get screen names of users with high polarity tweets
hi_users = hi_pol['user'].reset_index()
hi_sn = json_normalize(hi_users['user']).screen_name
print(hi_sn)

#get statuses with low polarity
lo_pol = statuses1[statuses1['polarity'] <= -0.7]
#lo_sn_1 = json_normalize(lo_pol_1['entities'],'user_mentions')

#get screen names of users with low polarity tweets
lo_users = lo_pol['user'].reset_index()
lo_sn = json_normalize(lo_users['user']).screen_name
print(lo_sn)

