import json


with open('asiaMatchData.txt') as jf:
    data = json.load(jf)

    for m in data:
        print(m['metadata']['matchId'] + " " + m['info']['gameMode'])
