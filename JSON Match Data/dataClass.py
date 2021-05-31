import json

class dataClass:
   


    def returnJSONObject(file):
        try:
            with open(file,'r') as jf:
                return json.load(jf)
        except:
            exceptString = 'File {0} Does Not Exist'.format(file)
            print(exceptString)
            return None

    def findItems(data):
        '''
        @param data:
        This is a json object of matchData text file
        '''
        for player in data[0]['info']['participants']:
            print(str(player['item0']) + " " + str(player['item1']) + " " + str(player['item2']) + " "
                + str(player['item3']) + " " + str(player['item4']) + " " + str(player['item5']) + " " + str(player['item6']))


