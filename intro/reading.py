#!/usr/bin/env python3

participants = {}
with open('scores.txt', 'r') as file_object:
    for line in file_object:
        entry = line.strip().split(",")
        participant = entry[0]
        score = entry[1]
        participants[participant] = score
        print(participant + ": " + score)

print(participants)