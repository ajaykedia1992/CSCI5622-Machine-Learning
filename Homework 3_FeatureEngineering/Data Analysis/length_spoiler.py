import pandas as pd
from matplotlib import pyplot as plt

kTARGET_FIELD = 'spoiler'
kTEXT_FIELD = 'sentence'

dfTrain = pd.read_csv("../data/spoilers/train.csv")

spoiler_len = []
non_spoiler_len = []

for index,row in dfTrain.iterrows():
    if row[kTARGET_FIELD] == True:
        spoiler_len.append(len(row[kTEXT_FIELD]))
    else:
        non_spoiler_len.append(len(row[kTEXT_FIELD]))

plt.title('Text Length')
l1, = plt.plot(spoiler_len, label = 'spoiler', color = 'black')
l2, = plt.plot(non_spoiler_len, label = 'non-spoiler', color = 'red')
plt.legend(handles=[l1, l2])

plt.show()