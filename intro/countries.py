#!/usr/bin/env python3
filename = 'countries.txt'
countries = []
with open(filename, 'r') as file_object:
    for line in file_object:
        line = line.strip()
        #print(line)
        countries.append(line)
print(len(countries))

for country in countries:
    if country[0] == "T":
        print(country)

