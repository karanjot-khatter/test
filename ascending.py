#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     01/10/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import operator
import csv

data = csv.reader(open("data.csv"))

for line in sorted(data, key=operator.itemgetter(10), reverse=True):
    print(line)




