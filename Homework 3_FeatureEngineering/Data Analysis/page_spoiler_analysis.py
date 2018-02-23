import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
kTARGET_FIELD = 'spoiler'
kPAGE_FIELD = 'page'
dfTrain = pd.read_csv("data/spoilers/train.csv")

spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 1]
non_spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 0]


page_group_spoiler = spoiler_list.groupby(kPAGE_FIELD).size().sort_values(ascending=False)
page_group_nonspoiler = non_spoiler_list.groupby(kPAGE_FIELD).size().sort_values(ascending=False)


plt.xticks(rotation='vertical')
plt.gca().set_xticklabels(page_group_spoiler.index)
l1, = plt.plot(page_group_spoiler[0:20].values, label='Spoiler', marker='.', color = 'black')
l2, = plt.plot(page_group_spoiler[page_group_nonspoiler[0:20].index].values, label='Non Spoiler', marker='o')
plt.legend(handles=[l1, l2])
plt.tight_layout()
plt.title('Page : Top Spoiler Pages')
plt.show()

plt.xticks(rotation='vertical')
plt.gca().set_xticklabels(page_group_nonspoiler.index)
l1, = plt.plot(page_group_nonspoiler[0:20].values, label='Non Spoiler', marker='.')
l2, = plt.plot(page_group_nonspoiler[page_group_spoiler[0:20].index].values, label='Spoiler', marker='o', color = 'black')
plt.legend(handles=[l1, l2])
plt.title('Page : Top Non Spoiler distribution')
plt.show()