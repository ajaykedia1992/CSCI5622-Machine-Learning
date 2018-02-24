from urllib.request import urlopen
import pickle

train_file = urlopen('https://github.com/ajaykedia1992/CSCI5622-Machine-Learning/blob/master/Homework%203_FeatureEngineering/train.pickle?raw=true')
train = pickle.load(train_file)
print(train)

my_badlist = urlopen('https://raw.githubusercontent.com/ajaykedia1992/CSCI5622-Machine-Learning/master/Homework%203_FeatureEngineering/my_badlist.txt').read()
my_badlist = my_badlist.decode("utf-8")
my_badlist = my_badlist.split("\n")
print(my_badlist)