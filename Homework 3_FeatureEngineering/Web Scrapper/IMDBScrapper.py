import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
import pickle
import imdb
from bs4 import BeautifulSoup
import requests
ia = imdb.IMDb()
str1 = 'https://www.imdb.com/title/tt'
#url = urllib.urlopen(str).read()
#bs = BeautifulSoup(r.text)
'''s_result = ia.search_movie('Break The Bank1985')

print(s_result)
# Print the long imdb canonical title and movieID of the results.
for item in s_result:
   print(item['long imdb canonical title'], item.movieID)'''

def mearge(li):
    str = ""
    art = ['in','a','the','and']
    #print(li)
    for i in range(len(li)):
        if li[i] != len(li)-1:
            if len(li[i]) > 1:
                #re.findall('\d+[a-z]', li[i])
                str += li[i] + ' '
            else:
                if (i+1) < len(li) and len(li[i+1])>1:
                    str += li[i] + ' '
                else:
                    str += li[i]
        else:
            str+= li[i]
    return str
#url = 'https://www.imdb.com/title/'
d = pd.read_csv("data/spoilers/train.csv")

list_set = set(d['page'])
#print(len(list_set))

# set_split = []
#
# i = 0
# i_len = 62
# for row in list_set:
#     set_split.append(row)
#     i += 1

# print(len(set_split[0]))
# print(len(set_split[1]))
# print(len(set_split[2]))
# print(len(list_set))

'''import pickle

with open('genre_1.pickle', 'wb') as handle:
    pickle.dump(set_split[0], handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('genre_2.pickle', 'wb') as handle:
    pickle.dump(set_split[1], handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('genre_3.pickle', 'wb') as handle:
    pickle.dump(set_split[2], handle, protocol=pickle.HIGHEST_PROTOCOL)'''

pos = {}

#with open('genre_3.pickle', 'rb') as handle:
 #   list_set = pickle.load(handle)
gen_list = {}
#for index,row in d.iterrows():
import pickle
def genre_find():

    for row in list_set:
        li = re.findall('[A-Z][^A-Z]*', row)
        title = mearge(li)
        s_result = ia.search_movie(title)
        print(title)
        try:
            print(s_result[0]['title'],s_result[0].movieID)
            #str = str+ str(s_result[0].movieID)+'/'
            print(str1+str(s_result[0].movieID)+'/')
            url = requests.get(str1+str(s_result[0].movieID)+'/')
            bs = BeautifulSoup(url.content,'html.parser')
            #print(list(bs.children))
            genre_tags = bs.find_all('span', itemprop='genre')
            gen = ""
            for th in genre_tags:
                for one in th.find_all('a'):
                    gen +=  one.contents[0]+","
            print(gen[:-1])
            gen_list[row] = (gen[:-1])
        except:
            print("No found for this one")
            gen_list[row] = "None"



    with open('genre_test_dump.pickle', 'wb') as handle:
        pickle.dump(gen_list, handle, protocol=pickle.HIGHEST_PROTOCOL)



genre_find()