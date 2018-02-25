from matplotlib import pyplot as plt
from urllib.request import urlopen
import pickle
train_file = urlopen('https://github.com/ajaykedia1992/CSCI5622-Machine-Learning/blob/master/Homework%203_FeatureEngineering/train.pickle?raw=true')
train_file_load = pickle.load(train_file)
episode_file_1 = urlopen('https://github.com/ajaykedia1992/CSCI5622-Machine-Learning/blob/master/Homework%203_FeatureEngineering/episode_test_dump.pickle?raw=true')
episode_train_file_load = pickle.load(episode_file_1)
kPAGE_FIELD = 'page'
kEPISODE_LIST = 'episode'
kTARGET_FIELD = 'spoiler'


dfTrain = train_file_load
episode_list = episode_train_file_load
page = dfTrain[kPAGE_FIELD]
episode = []
for p in page:
    if p in episode_list:
        episode.append(episode_list[p])

dfTrain[kEPISODE_LIST] = episode


spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 1]
spoiler_list = spoiler_list.drop_duplicates(subset='page')
non_spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 0]
non_spoiler_list = non_spoiler_list.drop_duplicates(subset='page')

# page_group_spoiler = spoiler_list.groupby(kEPISODE_LIST).size().sort_values(ascending=False)
# page_group_nonspoiler = non_spoiler_list.groupby(kEPISODE_LIST).size().sort_values(ascending=False)

spoiler_movie_list = spoiler_list[kPAGE_FIELD]
spoiler_episode_no = spoiler_list[kEPISODE_LIST]

non_spoiler_movie_list = non_spoiler_list[kPAGE_FIELD]
non_spoiler_episode_no = non_spoiler_list[kEPISODE_LIST]

x = range(20)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, spoiler_episode_no[0:20], s=10, c='r', marker="s", label='spoiler')
plt.xticks(x,spoiler_movie_list[0:20])
loc,labels= plt.xticks()
plt.setp(labels, rotation = 90)
ax1.scatter(x, non_spoiler_episode_no[0:20], s=10, c='b', marker="o", label='non-spoiler')
plt.xticks(x,non_spoiler_movie_list[0:20])
loc,labels= plt.xticks()
plt.setp(labels, rotation = 90)
plt.xlabel('Rating')
plt.ylabel('count of pages')
plt.legend(loc='upper left')
plt.title('Rating : Spoiler and non-spoiler Analysis')
plt.show()