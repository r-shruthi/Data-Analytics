#For every User where, "Raiders of the Lost Ark", "God Father Part 1" and "Glory" had a minimum rating of 4.  
#What was the frequency of the movies that were highly recommended.  
#create a bar graph

import pip
pip.main(['install','lightfm'])
import numpy as np
import pandas as pd
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4)
model=LightFM(loss='warp')
model.fit(data['train'],epochs=30,num_threads=2)
n_users, n_items=data['train'].shape

movie1 = 'Godfather, The (1972)'
movie2 = 'Raiders of the Lost Ark (1981)'
movie3 = 'Glory (1989)'

#Get users who have rated any of the three movies
top_users = np.empty(0)
for p in  np.arange(n_users):
    pos = data['item_labels'][data['train'].tocsr()[p].indices]
    for z in pos:
        if((z == movie1) | (z == movie2) | (z == movie3 )):
            top_users = np.append(top_users,p)

#Get the unique users in the list of users and also the count of how many times 
# each user is repeated
top_users, count = np.unique(top_users, return_counts = True)  

#Get the indices of all return_counts with value = 3
k =[]
j=0
for i in count:
    if i == 3:
        k.append(j)
    j= j+1

#top_users[k] gives all users who have rated all three movies i.e having return_count=3
#predict movies for users in top_users[k]
top_items = np.empty(0)
for user_id in top_users[k]:
    scores = model.predict(user_id, np.arange(n_items))
    top_items = np.append(top_items,data['item_labels'][np.argsort(-scores)[0]])

top_ser = pd.Series(top_items)
top_ser.value_counts().plot(kind='bar')
        
