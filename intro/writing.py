#!/usr/bin/env python3

with open('scores.txt', 'w') as file_object:
    while True:
        participant = input("Participant name > ")
        if participant == 'quit':
            print("Quitting...")
            break
            
        score = input("Score for " + participant + "> ")
        file_object.write(participant + ", " + score + "\n")
