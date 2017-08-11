# Data-Analytics
FiveDayStockReturn.py - Create a matrix using some stocks.  Using the try and catch, calculate the 5 day return for each stock that has stock data for that period.  Then create a matrix that has the same size columns and rows as the number of 5-day returns you calculated.  Proceed to place a value of 1, -1, or 0 in each cell according to these rules:
  1) if the row's ticker's 5-day return is positive (for example 2%), then if the column's 5-day's return is equal or greater (for example 3%), place a 1 in the cell.  If the column's 5-day return is the negative value of the row's 5-day return or less (for example -2% or less) then place a -1 in the cell.  Other wise place a 0
  2) if the row's ticker's 5-day return is negative (for example -2%), then if the column's 5-day's return is equal or less  (for example -3%), place a 1 in the cell.  If the column's 5-day return is the positive value of the row's 5-day return or greater (for example 2% or greater) then place a -1 in the cell.  Other wise place a 0

RecommendationSystem.py - Using LightFM get the top movie (first one) recommended for all the users, 
and then count up how many times a single movie was recommended as the top movie.  Graph the results in a bar graph.

RecommendationSystem2.py - Using LightFM: For every User where, "Raiders of the Lost Ark", "God Father Part 1" and "Glory" had a minimum rating of 4, what was the frequency of the movies that were highly recommended? Create a bar graph

RestaurantSentimentAnalysisFromYelp.py - Perform Sentiment Analysis on restaurant review data collected from Yelp.
Get 20 of the restaurants from a city of your choice. 
Download the reviews for each one (yelp only gives one review per restaurant from the API).
Calculate the Polarity and Sentiment for each review and create a Line Graph.

RestaurantSentimentAnalysisFromYelp2.py - Get 60 restaurants by looping through the API by incrementing the offset parameter by 20 (0,20,40). Calculate the polarity and subjectivity for each one and display in a bar graph.

TwitterSentimentAnalysis.py - Twitter Data Sentiment Analysis
Get screen names of users with high and low polarity tweets about 'tsla'

TwitterSentimentAnalysis2.py - Search for a stock by name and find the highest and lowest polarity value texts and 
find out how many times the stock name was tweeted by those users

TwitterTopTrends.py - Find top 20 trends for New York and Nashville and plot a bar graph



