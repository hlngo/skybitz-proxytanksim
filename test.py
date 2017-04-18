# test.py
import json, pprint

#Project restructuring tests
# file = 'logs/test.txt'
# with open(file, 'a') as text_file:
#     text_file.write('it works')

# #Testing the new writecsvfile function which now also creates json file - working well
# import config, demotank
# d = demotank.DemoTank()     #create the demotank global object first
# alltankslist = d.updateallsimtanks()
# #print(alltankslist)
# d.writecsvfile(alltankslist)

# tanks = {}
# with open('simtanks.json', 'r') as jfile:
#     tanks = json.load(jfile)
# print(str(type(tanks)))
# #pprint.pprint(tanks)

# with open('simtanks.json', 'r') as jfile:
#     tanks = json.load(jfile)

# print(tanks['S01'][0]['tank name'])
