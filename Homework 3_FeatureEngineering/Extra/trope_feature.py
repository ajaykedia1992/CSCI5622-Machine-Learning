import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

dfTrain = pd.read_csv("data/spoilers/train.csv")

train_true = dfTrain.loc[dfTrain['spoiler'] == 1]
train_false = dfTrain.loc[dfTrain['spoiler'] == 0]


page_group_spoiler = train_true.groupby('trope').size()
page_group_notspoiler = train_false.groupby('trope').size()

page_group_spoiler = page_group_spoiler.sort_values(ascending=False)
page_group_notspoiler = page_group_notspoiler.sort_values(ascending=False)


print(page_group_spoiler)
print(page_group_notspoiler)