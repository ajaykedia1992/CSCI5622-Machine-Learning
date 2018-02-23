import pickle
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import requests
import urllib.request

kGENRE_FIELD = 'genre'
kTARGET_FIELD = 'spoiler'
with open("train.pickle", 'rb') as fifty_f:
    dfTrain = pickle.load(fifty_f)


list = dfTrain[kGENRE_FIELD]
genre_list = []
for g in list:
    str = g.split(',')
    if str[0] == '':
        str[0] = 'None'
    genre_list.append(str[0])

dfTrain[kGENRE_FIELD] = genre_list
spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 1]
non_spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 0]

genre_group_spoiler = spoiler_list.groupby(kGENRE_FIELD).size()
genre_group_nonspoiler = non_spoiler_list.groupby(kGENRE_FIELD).size()

genre_group_spoiler = genre_group_spoiler.sort_values(ascending=False)
genre_group_nonspoiler = genre_group_nonspoiler.sort_values(ascending=False)

plt.xticks(rotation='vertical')
plt.gca().set_xticklabels(genre_group_spoiler.index)
l1, = plt.plot(genre_group_spoiler[0:50].values, label='Spoiler', marker='.')
l2, = plt.plot(genre_group_spoiler[genre_group_nonspoiler[0:50].index].values, label='Not Spoiler', marker='.')
plt.legend(handles=[l1, l2])
plt.tight_layout()
plt.title('Top Spoiler Genre!')
plt.show()


plt.xticks(rotation='vertical')
plt.gca().set_xticklabels(genre_group_nonspoiler.index)
l1, = plt.plot(genre_group_nonspoiler[0:50].values, label='Non Spoiler', marker='.')
l2, = plt.plot(genre_group_nonspoiler[genre_group_spoiler[0:50].index].values, label='Spoiler', marker='.')
plt.legend(handles=[l1, l2])
plt.tight_layout()
plt.title('Top Non Spoiler Genre')
plt.show()
