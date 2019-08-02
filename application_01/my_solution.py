#!/usr/bin/python3

from difflib import SequenceMatcher
import json

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def close(word, data):
    for another in data:
        if similar(word, another) > 0.75:
            yield another

data = {}
with open('data.json', 'r') as file:
    data = json.load(file)

while True:
    word = input("give a word: ").lower()
    if word in data:
        if type(data[word]) == list:
            for definition in data[word]:
                print(definition)
        else:
            print(data[word])
                
        break
    else:
        match = False
        for another in close(word, data):
            print(f"did you mean: {another}")
            match = True
        if match:
            answer = input("try again? (yes/no): ")
            if answer == "yes":
                continue
        else:
            print("unknown word")
        break
