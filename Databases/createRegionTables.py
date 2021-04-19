# This file creates a table for different regions
# in a given database file


import sqlite3


con = sqlite3.connect('matchIdByRegion.db')
cursor = con.cursor()

regions=[
        # these are the regions for the v4 api
        #'cblol','lck','lcl','lco','lcs','lec','ljl','lpl','tcl','lla'

        'americas',
        'europe',
        'asia'

        ]

for r in regions:
    # these are the values used for the v4 matchList responses
    # (platformId text, gameId text, champion text, queue text, season text, timestamp text,  role text, lane text)
    cursor.execute('''CREATE TABLE %s (gameId text) '''% r)
con.commit()
con.close()
