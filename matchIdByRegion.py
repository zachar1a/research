import requests, json, sqlite3, time
from config import key


# regions
# lck, ljl, cblol, lco, lcs, lla, lcl, lec, tcl

# regions done so far
# lck
# ljl
# cblol
# lco
# lcs
# lla
# lcl
# tcl
region = 'lec'
country = 'europe'
headers= {
        'X-Riot-token':key
        }

def getPlayerList(region):
# id text, accountId text, puuid text, name text, profileIconId real, revisionDate text, summonerLevel real
    con = sqlite3.connect('playerAccountData.db')
    cur = con.cursor()

    data = cur.execute('SELECT * FROM %s' % region)
    data = data.fetchall()
    cur.close()

    playerList = []
    for d in data:
        # this is appending the accountID to a list
        playerList.append(d[2])

    return playerList

def makeRequest(playerList, url):

    data=[]
    for player in playerList:
        time.sleep(2)
        tmp = url.format(player)
        try:
            result = json.loads(requests.get(tmp, headers=headers).text)
        except:
            continue

        try:
            if result is not None:
                print(result)
                for r in result:
                    data.append(r)
                    print(r)
            else:
                print('no matches somehow')
                continue
        except:
            continue
    return data

def sendToDB(country, data):
    con = sqlite3.connect('matchIdByRegion.db')
    cur = con.cursor()
    command = 'INSERT INTO %s VALUES(?)' % country
    for d in data:
        cur.execute(command, (d,))
        con.commit()
    con.close()


# america serves na br lan las oce
# asia serves kr jp
# europe servers eune euw tr ru

def getMatchId(playerList, region):
    if region == 'lck':
        url = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'cblol':
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'lcl':
        print('europe')
        url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'lco':
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'lcs':
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'lec':
        url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'ljl':
        url = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'tcl':
        url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)
    elif region == 'lla':
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{0}/ids?start=0&count=100'
        return makeRequest(playerList,url)

def main(region):
    playerList = getPlayerList(region)
    matchIdList = getMatchId(playerList, region)
    sendToDB(country, matchIdList)

if __name__ == "__main__":
    main(region)
    





