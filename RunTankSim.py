# RunTankSim.py
# Version 1.0
# Used to run the proxy tank simulator

import demotank, ftplib, datetime, time
import config

d = demotank.DemoTank()     #create the demotank global object first

def runSim():
    d.writecsvfile(d.updateallsimtanks())

    try:
        session = ftplib.FTP(config.url, config.uname, config.pword)
        # session = ftplib.FTP('10.35.98.81', 'upload', 'password')
        file = open('simtanks.csv', 'rb')                  # file to send
        session.storbinary('STOR simtanks.csv', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
        return ' Sim tanks updated, ftp transfer success!'
    except:
        return ' Oops, there was a problem with ftp.'

#run main program
while(True):
    resultstr = '\n'
    resultstr += str(datetime.datetime.now())
    d.logrun(resultstr)
    d.logrun(runSim())
    #time.sleep(120)     #used for testing
    time.sleep(10800)   #3hr delay used actual demo
