import json
from dataClass import dataClass


data = dataClass.returnJSONObject('americasMatchData.txt')
dataClass.findItems(data)
