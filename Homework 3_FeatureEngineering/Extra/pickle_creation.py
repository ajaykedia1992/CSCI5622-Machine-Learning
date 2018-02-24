import pickle


subjectivity = []
file_list = ['strong_pos.txt','strong_neg.txt','weak_pos.txt','weak_neg.txt']
for filename in file_list:
    myfile = open(filename, 'r')
    list = []
    for w in myfile:
        list.append(w.rstrip())

    subjectivity.append(list)


with open('load_subjectivity.pickle', 'wb') as f:
    pickle.dump(subjectivity,f)

with open("load_subjectivity.pickle",'rb') as fifty_f:
    myfile1 = pickle.load(fifty_f)
print(myfile1[3])

