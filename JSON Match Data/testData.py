import json

matchArr = list()
with open("americasMatchData.txt") as file:
    reader = json.load(file)

    for match in reader:
        if match['info']['gameMode'] == "CLASSIC":
            matchArr.append(match)

with open("testData.txt",'w') as file:
    json.dump(matchArr, file)
