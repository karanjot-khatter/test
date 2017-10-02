import operator
import csv

outFileName = "data2.csv"
outFile = open(outFileName, "w")

data = csv.reader(open("data.csv"), delimiter=',')

for line in sorted(data, key=operator.itemgetter(10), reverse=True):
       print(line.strip(), file = outFile)

outFile.close()


