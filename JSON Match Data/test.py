import json


with open('asiaMatchData.txt','r') as amd:

    matches = json.load(amd)

    print(matches[0])

    with open('testData.txt', 'w') as test:

        json.dump(matches[0], test)
