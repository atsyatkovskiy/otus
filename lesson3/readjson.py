import json
import csv
from csv import DictReader, DictWriter
from collections import defaultdict
import collections

with open('users.json', 'r') as userfile:
    data = json.load(userfile)

json_list = []
for i in data:
    json_list.append({
        "name": i['name'], "gender": i['gender'], "address": i['address'],
        "books": {
            "title": "Fundamentals of Wavelets",
            "author": "Goswami, Jaideva",
            "height": "228"
        },
    })

print(list(json_list))

slov = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        print(row['Title'], row['Author'], row['Height'])
        slov.append({
            "books": {
                "title": row['Title'],
                "author": row['Author'],
                "height": row['Height']
            }
        })

print(list(slov))

json_result = 'result.json'
with open(json_result, "w", encoding="utf-8") as resultfile:
    json.dump(json_list, resultfile)

# res_dict = {}
# for item in json_list:
#     res_dict.update(item)
#
# print(res_dict)
