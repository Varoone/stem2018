import json
from pprint import pprint

with open('.\\data\\chemicals.csv', 'r') as filechemicals:
    chemdata = json.load(filechemicals)

with open('.\\data\\state.csv', 'r') as filex:
    statedata = json.load(filex)

pickone = input("Do you want to search about states or chemicals ENTER S for states and C for chemicals: ")
if pickone == "S":
   state = input("Enter state abbreviations: ")
   print(statedata.get(state))
else:
    cheminput = input("Enter chemical name in all CAPS: ")
    print(chemdata.get(cheminput))





