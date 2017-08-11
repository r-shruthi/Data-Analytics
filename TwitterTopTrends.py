#Find top 20 trends for New York and Nashville and plot a bar graph
import json
from twitter import Twitter 
from twitter import OAuth 
from twitter import TwitterHTTPError 
from twitter import TwitterStream 
from pandas.io.json import json_normalize

AccessToken = ''
AccessTokenSecret = ''
ConsumerKey = ''
ConsumerSecret = ''
oauth = OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret)

#create Twitter object
twitter = Twitter(auth=oauth)

#get woeids
world_trends = twitter.trends.available(_woeid=1)

#normalize to json format
wt = json_normalize(world_trends)

#get woeid for New York and Nashville
ny_id = wt[wt.name == 'New York'].iloc[0]['woeid']
nash_id = wt[wt.name == 'Nashville'].iloc[0]['woeid']

twitter.trends.place(_id = 1)

#get twitter trends for NewYork and Nashville
ny_trends = twitter.trends.place(_id = ny_id)
nashville_trends = twitter.trends.place(_id = nash_id)

#Normalize trends for New York and Nashville
ny_trends_json = json_normalize(ny_trends,'trends')
nash_trends_json = json_normalize(nashville_trends,'trends')

#get columns names from normalized trends 
ny_trends_json.columns

#plot bar graph for top 20 trends for new york
ny_plot = ny_trends_json.sort('tweet_volume',ascending=False).head(20)
ny_plot.plot('name','tweet_volume',kind='bar')

#plot bar graph for top 20 trends for nashville
nash_trends_json.columns
nash_plot = nash_trends_json.sort('tweet_volume',ascending=False).head(20)
nash_plot.plot('name','tweet_volume',kind='bar')

#merge top 20 NY plot and Nashville plot 
merged_plot = pd.merge(nash_plot,ny_plot,on=['name','tweet_volume'])
merged_plot.plot('name','tweet_volume',kind='bar')

