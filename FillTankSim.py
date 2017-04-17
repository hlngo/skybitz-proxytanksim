# FillTankSim.py
# Version 1.0
# Used to fill tanks in proxy tank simulator

import sys, demotank, datetime

def isInt(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

try:
    d = demotank.DemoTank()
    if int(sys.argv[1]) < 1 or int(sys.argv[1]) > d.tanksimnum or isInt(sys.argv[1]) != True:
        print('Arg1 is not a positive Int or is an invalid Tank ID!')
    elif int(sys.argv[2]) < 1 or isInt(sys.argv[2]) != True:
        print('Arg2 is not a positive Int, please enter valid fill amount!')
    else:
        d.fillsimtank(int(sys.argv[1]), int(sys.argv[2]))
        resultstr = '\n'
        resultstr += str(datetime.datetime.now())
        resultstr += ' Tank ' + str(sys.argv[1]) + ' filled with ' + str(sys.argv[2]) + ' gallons.'
        d.logfill(resultstr)
        #print('Tank Filled!')
        #print(sys.argv)
except:
    print('Error: problem with inputs!')