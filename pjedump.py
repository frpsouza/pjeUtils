import re
import csv

from ExtractPage import *
from cleantext import *


with open("processo.txt", 'r', encoding='utf-8') as file:
    text=file.readlines()

lines = RepairText(text)
lines = RemoveEmptyLines(lines)

indexes = getIndexes(lines)

for i in indexes:
    dict= ExtractPageData(i, lines)




with open("output.csv", 'w') as f:
    write = csv.writer(f)
    for rows in listHeaders:
        write.writerow(rows)
