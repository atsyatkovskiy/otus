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
        "name": i['name'], "gender": i['gender'], "address": i['address']
    })

print(list(json_list))

slov = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        print(row['Title'], row['Author'], row['Height'])
        slov.append({
                "title": row['Title'],
                "author": row['Author'],
                "height": row['Height']
        })

total_books = len(slov)

# total_books = len(slov)
# total_users = len(json_list)
#
# print("total_users=", total_users)
# print("total_books=", total_books)
#
# print(list(range(total_users)))

for i in range(len(json_list)):
    user = json_list[i]
    if i < total_books:
        book = slov[i]
        user['books'] = [book]
    else:
        user['books'] = []

# print(list(slov))
#
json_result = 'result.json'
with open(json_result, "w", encoding="utf-8") as resultfile:
    json.dump(json_list, resultfile, indent=4)

# res_dict = {}
# for item in json_list:
#     res_dict.update(item)
#
# print(res_dict)
