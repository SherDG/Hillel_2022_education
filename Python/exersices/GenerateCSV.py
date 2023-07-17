import csv
import random

fieldnames = ['id', 'name', 'age', 'city']
csvfile = open("people_1.csv", "w")

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

names = ['Yulia', 'Stas', 'Max', 'Olga', 'Serg', 'Kate']
cities = ['Dnipro', 'Odesa', 'Kyiv', 'Kharkiv']

records = 10
for i in range(0, records):
    writer.writerow(
        {'id': str(i), 'name': random.choice(names), 'age': str(random.randint(18, 81)), 'city': random.choice(cities)})

csvfile.close()