import json

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)