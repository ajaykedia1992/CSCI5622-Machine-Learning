import pickle
import csv

answer_list = []
count = 0
with open('prediction_result.csv', 'r') as csvfile:
    sentence_reader = csv.reader(csvfile, delimiter='\n')
    for row in sentence_reader:
        if count == 0:
            count = 1
            continue
        answer_list.append(row[0].split(',')[1])

with open('another_predictions.pickle', 'wb') as f:
    pickle.dump(answer_list, f)
