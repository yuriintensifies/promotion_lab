import csv
import string
import numpy as np

def build_naive(data):
    attributes = np.zeros((len(data), 2), dtype=int)
    totalcount = 0
    poscount = 0
    negcount = 0
    for line in data:
        classw = line[-1]
        for val in line:
            totalcount += 1
            if classw == 1:
                attributes[val][0] += 1
                poscount += 1
            elif classw == 0:
                attributes[val][1] += 1
                negcount += 1
    ppositive = poscount / totalcount
    pnegative = negcount / totalcount
    pattributes = np.zeros((len(data), 2), dtype=int)
    for n, pair in enumerate(attributes):
        pattributes[n][0] = pair[0] / poscount
        pattributes[n][1] = pair[1] / negcount
    return

with open("data/labeled_corpus.tsv", encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:
        line_arr = list(row)

        tweet = line_arr[0]
        sentiment = line_arr[1]

        table = str.maketrans('', '', string.punctuation)
        tweet = tweet.translate(table)

        words = tweet.split()

