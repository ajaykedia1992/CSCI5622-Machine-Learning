import pickle
my_answer = []
answer = []
p=0
n=0
with open("actual_predictions.pickle",'rb') as fifty_f:
    answer = pickle.load(fifty_f)
with open("result_predictions.pickle",'rb') as fifty1_f:
    my_answer = pickle.load(fifty1_f)

for i in range(len(answer)):
    if answer[i] == my_answer[i]:
        p += 1
    else:
        n += 1
print(p,n)
print((p/(p+n)))