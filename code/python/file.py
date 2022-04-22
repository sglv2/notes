try:
    f1 = open('f1.txt', 'r')
    for line in f1:
        print(line)
    f1.close()
except FileNotFoundError:
    print('File not found')

f2 = open('f2.txt', 'w')
f2.write("first\n")
f2.write("second\n")
f2.writelines(["third\n", "fourth\n"])
f2.close()

f2 = open('f2.txt', 'a')
f2.write("fifth\n")
f2.close()

# CSV
import csv

## open() function is used as a context manager that ensures that the file will be closed after executing the loop
with open('f3.csv', mode='r') as f3:
    csv_content = csv.reader(f3)

    for line_items in csv_content:
        print(line_items)

# JSON

import json

f4 = open('f4.json')
data = json.load(f4)
print(data)
for k, v in data.items():
    print(f'k={k} v={v}')
f4.close()
