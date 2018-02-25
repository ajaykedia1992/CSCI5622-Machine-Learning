from matplotlib import pyplot as plt
from urllib.request import urlopen
import pickle
train_file = urlopen('https://github.com/ajaykedia1992/CSCI5622-Machine-Learning/blob/master/Homework%203_FeatureEngineering/train.pickle?raw=true')
dfTrain = pickle.load(train_file)
movie_released_country_train_file = urlopen('https://github.com/ajaykedia1992/CSCI5622-Machine-Learning/blob/master/Homework%203_FeatureEngineering/country.pickle?raw=true')
movie_released_country_train_load = pickle.load(movie_released_country_train_file)
kPAGE_FIELD = 'page'
kCOUNTRY_LIST = 'country'
kTARGET_FIELD = 'spoiler'

page = dfTrain[kPAGE_FIELD]
country_df = []
for p in page:
    if p in movie_released_country_train_load:
        country_df.append(movie_released_country_train_load[p])
dfTrain['country'] = country_df



spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 1]
spoiler_list = spoiler_list.drop_duplicates(subset=kPAGE_FIELD)
non_spoiler_list = dfTrain.loc[dfTrain[kTARGET_FIELD] == 0]
non_spoiler_list = non_spoiler_list.drop_duplicates(subset=kPAGE_FIELD)


# new_spoiler_list = []
# new_spoiler_df = spoiler_list
# for index,cont in spoiler_list.iterrows():
#     a = cont[kCOUNTRY_LIST]
#     country = a.split(',')
#     list = []
#     if len(country) == 1:
#         continue
#     else:
#         new_spoiler_list[new_spoiler_list.kPAGE_FIELD != cont[kPAGE_FIELD]]
#         cont.__delitem__(kCOUNTRY_LIST)
#         cont = cont.append(cont*(len(country)-1))
#         cont[kCOUNTRY_LIST] = country
#         new_spoiler_list.append((cont))


page_group_spoiler = spoiler_list.groupby(kCOUNTRY_LIST).size().sort_values(ascending=False)
page_group_nonspoiler = non_spoiler_list.groupby(kCOUNTRY_LIST).size().sort_values(ascending=False)

x = range(len(page_group_spoiler.index))
fig = plt.figure(figsize=(15,6))
ax1 = fig.add_subplot(111)
ax1.scatter(x, page_group_spoiler.values, s=10, c='r', marker="s", label='spoiler')
plt.xticks(x, page_group_spoiler.index)
loc,labels= plt.xticks()
plt.setp(labels, rotation = 90)
x = range(len(page_group_nonspoiler.index))
ax1.scatter(x, page_group_nonspoiler.values, s=10, c='b', marker="o", label='non-spoiler')
plt.xticks(x,page_group_nonspoiler.index)
loc,labels= plt.xticks()
plt.setp(labels, rotation = 90)
plt.xlabel('Rating')
plt.ylabel('count of pages')
plt.legend(loc='upper left')
plt.title('Rating : Spoiler and non-spoiler Analysis')
plt.show()