import operator
import csv

outFileName = "data2.csv"
outFile = open(outFileName, "w")

data = csv.reader(open("data.csv"), delimiter=',')
for line in range(5):
    for line in sorted(data, key=operator.itemgetter(10), reverse=True):
       print(line, file = outFile)

outFile.close()


