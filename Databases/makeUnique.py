import sqlite3


regions=['europe','asia','americas']

#con = sqlite3.connect('Databases/matchIdByRegion.db')
con= sqlite3.connect('uniqueMatchIdByRegion.db')

cur = con.cursor()
#conUnique = unique.cursor()


for r in regions:
    command = 'SELECT * FROM {0}'.format(r)
    data = cur.execute(command)
    data = data.fetchall()
    print(str(r) + " " + str(len(data)))

cur.close()
'''
    uniqueCommand = 'INSERT OR IGNORE INTO %s  VALUES(?)' % r
    for d in data:
        conUnique.execute(uniqueCommand, (d[0],))
        unique.commit()
        print(d[0])
    print(len(data))

cur.close()
conUnique.close()
'''
