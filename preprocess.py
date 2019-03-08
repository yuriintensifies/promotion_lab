import csv
import sys
import random

def reduce_cardinality(data, attribute, desired=5):
    values = {}
    for line in data:
        if line[attribute] not in values:
            values[line[attribute]] = 0
        values[line[attribute]] += 1
    counts = sorted(values.items(), key=lambda kv: kv[1])
    print(counts)
    top = counts[-desired:]
    topw = []
    for x in top:
        topw.append(x[0])
    print(topw)
    for line in data:
        if line[attribute] not in topw:
            line[attribute] = -1

with open(sys.argv[1]) as data:
    output = []
    count = 0
    dreader = csv.reader(data, delimiter=',')
    for row, line in enumerate(dreader):
        count += 1
        if row == 0:
            continue
        output.append(list(line))

reduce_cardinality(output, 20)

test = []
for x in range(count//5):
    ind = random.randrange(count - x)
    test.append(output[ind])
    del output[ind]


with open('training.csv', 'w', newline='') as out:
    dwriter = csv.writer(out)
    dwriter.writerows(output)

with open('testing.csv', 'w', newline='') as out:
    dwriter = csv.writer(out)
    dwriter.writerows(test)