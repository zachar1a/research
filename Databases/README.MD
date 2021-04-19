# DATABASES

## matchIdByRegion
This holds three tables: americas, asia, europe
The tables are comprised of match ID's that are used for
the riot v5 api


## uniqueMatchIdByRegion
This file holds the same region tables as matchIdByRegion
but the data has a unique constraint on it so everything
in here is unique

## playerAccountData
The tables in this file are: cblol, lck, lcl, lco, lcs, lec, ljl, lla, tcl

The schema for these tables is:
id text, accountId text, puuid text, name text, profileIconId real, revicionData text, summonerLevel real

## createRegionTables
This loops through a list called `region` and creates table
with the region name and the schema is given through
a variable called `command`

## makeUnique
This loops through a list called `region` and pulls the
data from matchIdByRegion into a var and then
passes the data into uniqueMatchIdByRegion 
