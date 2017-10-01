import operator
import csv

data = csv.reader(open("data.csv"))

for line in sorted(data, key=operator.itemgetter(10), reverse=True):
       print(line)




