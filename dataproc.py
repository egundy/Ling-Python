import csv
import json

with open('pythonistas.json') as file1:
    output = json.load(file1)
    
with open('pythonistas_convoluted.txt', 'w') as file2:
    result = csv.DictWriter(file2, ['last','first'])
    result.writeheader()
    result.writerows(output)