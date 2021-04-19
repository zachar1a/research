import requests,json
from bs4 import BeautifulSoup as bs4
from bs4 import BeautifulSoup


'''
To use this file uncomment the relative result var
and change the file destination in the findPlayer function
'''


# LCS 
#result = requests.get('https://lol.fandom.com/wiki/LCS/2021_Season/Spring_Season').text
# LEC
#result = requests.get('https://lol.fandom.com/wiki/LEC/2021_Season/Spring_Season').text
# LCK
#result = requests.get('https://lol.fandom.com/wiki/LCK/2021_Season/Spring_Season').text
# LPL
#result = requests.get('https://lol.fandom.com/wiki/LPL/2021_Season/Spring_Season').text
# TCL
#result = requests.get('https://lol.fandom.com/wiki/TCL/2021_Season/Winter_Season/Team_Rosters').text
# CBLOL
#result = requests.get('https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_1/Team_Rosters').text
# LCO
#result = requests.get('https://lol.fandom.com/wiki/LCO/2021_Season/Split_1/Team_Rosters').text
# LJL
#result = requests.get('https://lol.fandom.com/wiki/LJL/2021_Season/Spring_Season').text
# LCL
#result = requests.get('https://lol.fandom.com/wiki/LCL/2021_Season/Spring_Season').text
# LLA
#result = requests.get('https://lol.fandom.com/wiki/LLA/2021_Season/Opening_Season/Team_Rosters').text

soup = BeautifulSoup(result, 'html.parser')

def findPlayers(soup)
    players = soup.find_all('a', class_='catlink-players')
# switch the file name to the region to write players to file
    team = open("LLA.py", "w") 
    all_=[]
    for p in players:
        if p in all_:
            continue
        else:
            all_.append(p)

    for p in all_:
        print(p.text)
        team.write(str(",") + str("'") + p.text + str("'\n"))
    team.close()

findPlayers(soup)
