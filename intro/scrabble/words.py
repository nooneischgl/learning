#!/usr/bin/env python3
import scrabble

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

def has_a_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
            return True
    return False

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for letter in letters:
    if not has_a_double(letter):
        print(letter + " never appears doubled")

counter = 0
for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
        counter += 1
print(counter)


## Print all words containing 'uu'.
#for word in scrabble.wordlist:
#    if 'q' in word and 'u' not in word:
#        print(word)