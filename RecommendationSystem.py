#Get the top movie (first one) recommended for all the users, 
#and then count up how many times a single movie was recommended as the top movie. 
#Graph the results in a bar graph

import pip
pip.main(['install','lightfm'])
import numpy as np
import pandas as pd
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=3)
model=LightFM(loss='warp')
model.fit(data['train'],epochs=30,num_threads=2)
n_users, n_items=data['train'].shape

top_items = np.ndarray(0)
for user_id in np.arange(n_users):
    scores = model.predict(user_id, np.arange(n_items))
    top_items = np.append(top_items,data['item_labels'][np.argsort(-scores)[0]])

top_ser = pd.Series(top_items)
top_ser.value_counts().plot(kind='bar')