import requests, json, sqlite3, time
from config import key

region='americas'
headers={
        'X-Riot-token':key
        }

def getMatchId():
    con = sqlite3.connect('Databases/uniqueMatchIdByRegion.db')
    cur = con.cursor()

    data = cur.execute('SELECT * FROM %s' % region)
    data = data.fetchall()
    cur.close()
    return data
    


def makeRequest(region):
    data = getMatchId()
    allData=[]
    for mid in data:
        time.sleep(1.3)
        url = 'https://{0}.api.riotgames.com/lol/match/v5/matches/{1}'.format(region, mid[0])
        try:
            result = json.loads(requests.get(url,headers=headers).text)
            print("appending " + result['metadata']['matchId'])
            allData.append(result)
        except:
            print("no match found for " + mid[0])
            continue


    with open('americasMatchData.txt', 'w') as out:
        json.dump(allData, out)

makeRequest(region)
