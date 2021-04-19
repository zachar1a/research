# DATABASES

## matchIdByRegion
This holds match id's by general region americas, asia, europe

## uniqueMatchIdByRegion
This has the same tables as the last except all the matchId's
are unique

## playerAccountData
This holds player account data for all the subregions
of americas, europe and asia
The schema for the tables are

`(id text, accountId text, puuid text, name text, profileIconId real, revisionDate text, summonerLevel real);`


# getMatchData
This is a simple file that iterates over the uniqueMatchId
tables and saves all of the match data into a list
then dumps that list into a specified file.

The run time varies dependent on what region you want to get 
the match data for. It ranges from 8 to 11.5 hours.

# matchIdByRegion
This iterates over the tables from playerAccountData
and uses the `puuid` from each player and
sends a request to get their past 100 matches

# playerAccountData
This iterates over the tables from playerAccountData
and sends a request to get players individual account data
we need this info in order to get the matchId's for each
player


