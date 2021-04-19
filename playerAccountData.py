from Regions.CBLOL import CBLOLPLAYERS as cblol
from Regions.LCK import LCKPLAYERS as lck
from Regions.LCL import LCLPLAYERS as lcl
from Regions.LCO import LCOPLAYERS as lco
from Regions.LCS import LCSPLAYERS as lcs
from Regions.LEC import LECPLAYERS as lec
from Regions.LJL import LJLPLAYERS as ljl
from Regions.LPL import LPLPLAYERS as lpl
from Regions.TCL import TCLPLAYERS as tcl
from Regions.LLA import LLAPLAYERS as lla

import requests, json, sqlite3
from time import sleep
from config import key

'''
    (done)lck
    (waiting)cblol
    (waiting)lcl
    (waiting)lco
    (done)lcs
    (waiting)lec
    (done)ljl
    (waiting)lpl
    (waiting)tcl
    (waiting)lla
'''


# @param player
# This is a unique summoner name that 
# we need to get account data from the api endpoint
def findData(player):
    # this has to be uncommented an made sure that the correct
    # value is being used
    url = 'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s'%(player)
    headers={
            'X-Riot-Token':key
            }
    result = requests.get(url,headers=headers)
    return result

# @param region
# This controls what list of players to use
def getPlayerAccountData(region):
    playerAccountData=[]

    if region == 'lck':
        playerList = lck
    elif region == 'cblol':
        playerList = cblol
    elif region == 'lcl':
        playerList = lcl
    elif region == 'lco':
        playerList = lco
    elif region == 'lcs':
        playerList = lcs
    elif region == 'lec':
        playerList = lec
    elif region == 'ljl':
        playerList = ljl
    elif region == 'lpl':
        playerList = lpl
    elif region == 'tcl':
        playerList = tcl
    elif region == 'lla':
        playerList = lla

    for p in playerList:
        data = findData(p)
        if data.status_code == 200:
            data = json.loads(data.text)
            playerTuple = (data['id'],data['accountId'],data['puuid'],data['name'],data['profileIconId'],data['revisionDate'],data['summonerLevel'])
            print(playerTuple)
            playerAccountData.append(playerTuple)
            sleep(3)
        else:
            continue

    return playerAccountData

# @param data
# This is a list of the account data in tuple form
# @param region
# This is what region we are getting info from in string form
def insertToTable(data, region):
    con = sqlite3.connect('playerAccountData.db')
    cur = con.cursor() 

    if region == 'lck':
        cur.executemany('INSERT INTO lck VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'cblol':
        cur.executemany('INSERT INTO cblol VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lcl':
        cur.executemany('INSERT INTO lcl VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lco':
        cur.executemany('INSERT INTO lco VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lcs':
        cur.executemany('INSERT INTO lcs VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lec':
        cur.executemany('INSERT INTO lec VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'ljl':
        cur.executemany('INSERT INTO ljl VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lpl':
        cur.executemany('INSERT INTO lpl VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'tcl':
        cur.executemany('INSERT INTO tcl VALUES (?,?,?,?,?,?,?)', data)
    elif region == 'lla':
        cur.executemany('INSERT INTO lla VALUES (?,?,?,?,?,?,?)', data)

    con.commit()
    con.close()

data = getPlayerAccountData('lla')
insertToTable(data, 'lla')
