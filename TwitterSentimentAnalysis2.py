#Search for a stock by name and find the highest and lowest polarity value texts and 
#find out how many times the stock name was tweeted by those users


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

#Use appropriate values
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

#get statuses with low polarity
lo_pol = statuses1[statuses1['polarity'] <= -0.7]

import numpy
#get max and min polarity
most_positive = hi_pol[hi_pol['polarity'] == hi_pol['polarity'].max()]
most_negative = lo_pol[lo_pol['polarity'] == lo_pol['polarity'].min()]

#get max polarity user
most_positive_user = most_positive['user'].reset_index()
most_positive_sn = json_normalize(most_positive_user['user']).screen_name

#get min polarity user
most_negative_user = most_negative['user'].reset_index()
most_negative_sn = json_normalize(most_negative_user['user']).screen_name

#most_positive_sn = json_normalize(hi_pol_1['entities'],'user_mentions')
#most_negative_sn = json_normalize(lo_pol_1['entities'],'user_mentions')

#get tweets of max polarity user
search_hi = api.statuses.user_timeline(screen_name = most_positive_sn[0])
status_hi = json_normalize(search_hi)

#split all words from text and store into series
se = pd.Series(' '.join(status_hi['text']).lower().split(" "))

#get sum of times tsla is tweeted by max polarity user
maxSum = se.str.contains(r'tsla').sum()
print("No.of times tsla is tweeted by max polarity user:")
print(maxSum)

#get tweets of min polarity user
search_lo = api.statuses.user_timeline(screen_name = most_negative_sn[0])
status_lo = json_normalize(search_lo)

#split all words from text and store into series
se2 = pd.Series(' '.join(status_lo['text']).lower().split(" "))

#get sum of times tsla is tweeted by min polarity user
minSum = se2.str.contains(r'tsla').sum()
print("No.of times tsla is tweeted by min polarity user:")
print(minSum)
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
