#demotank.py
#Andrew Knight
#Feb 2017

import csv, datetime
import json

class DemoTank:
    """DemoTank class def"""

    def __init__(self):
        self.tanksimnum = 10
        self.logfilerun = 'logs/run_log.txt'
        self.logfilefill = 'logs/fill_log.txt'
        return

    def logrun(self, string):
        """logrun Docstring here - TXT NOT CSV"""
        with open(self.logfilerun, 'a') as text_file:
            text_file.write(string)
        return string

    def logfill(self, string):
        """logfill Docstring here - TXT NOT CSV"""
        with open(self.logfilefill, 'a') as text_file:
            text_file.write(string)
        return string

    def readcsv(self, filestring):
        """readcsv Docstring here"""
        with open(filestring, newline='') as csvfile:
            rowlist = []
            csvreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            for row in csvreader:
                rowlist.append(row)
        return rowlist

    def writecsvfile(self, listofrows):
        """writecsvfile docstring here"""
        #TODO: Add code block to jsonify the listofrows and save to json file
        dictdata = {}
        for row in listofrows:
            #dictdata[str(row[0])] = str(row)
            dictdata[str(row[0])] = []
            dictdata[str(row[0])].append({
                'id' : str(row[0]),
                'amount' : str(row[1]),
                'key value' : str(row[2]),
                'tank name' : str(row[3]),
                'tank capacity' : str(row[4]),
                'tank units' : str(row[5]),
                'product' : str(row[6]),
                'datetime updated' : str(row[7])
            })
        with open('simtanks.json', 'w') as jsonobj:
            json.dump(dictdata, jsonobj, sort_keys=True, indent=4)
        
        #previously created code - still working and required
        with open('simtanks.csv', 'w') as csvobj:
            wr = csv.writer(csvobj, quoting=csv.QUOTE_NONE)
            tankcsvfile = 'data/tankdat.csv'
            headerlist = self.listfromrow(self.readcsv(tankcsvfile), 1)#always read the first row for this one
            wr.writerow(headerlist)
            for item in listofrows:
                wr.writerow(item)
        return

    def writecsvrow(self, str, list):
        """writecsvrow Docstring here"""
        with open(str, 'w') as csvobj:
            wr = csv.writer(csvobj, quoting=csv.QUOTE_NONE)
            wr.writerow(list)
        return list

    def listfromrow(self, list, int):
        """Get a list of a single row from the list of the entire csv file.
        Takes the entire csv file read as a list for param1 and the intended row# as an int."""
        mylist = []
        selectedRow = 1
        for row in list:
            if selectedRow == int:   #if selected row based on input param
                tmpStr1 = str(row)   #convert the row to string
                rowStr = tmpStr1[2:len(tmpStr1)-2]   #strip the first and last '[ and ]' chars
                mylist = rowStr.split(',')           #split string from commas
            selectedRow += 1

        newlist = []
        for item in mylist:
            newlist.append(str(item))
        #print(newlist)
        return newlist

    def simtankcallout(self, integer):
        """updatetank Docstring here"""
        tankcsvfile = 'data/tankdat'+str(integer)+'.csv'
        pt = self.listfromrow(self.readcsv(tankcsvfile), 1)#always read the first row for tankdat files
        newlevel = int(pt[1]) - int(pt[2])
        if newlevel > 0:
            pt[1] = str(newlevel)     #reduce the gal level reading by the standard amt, draining tank
        else:
            pt[1] = '0'
        pt.pop()                            #remove last 'date' list item
        pt.append(datetime.datetime.now())  #re-append the updated date/time
        #print(pt)
        return pt

    def fillsimtank(self, tanknum, amt):
        """fillsimtank Docstring here"""
        tankcsvfile = 'data/tankdat'+str(tanknum)+'.csv'
        pt = self.listfromrow(self.readcsv(tankcsvfile), 1)#always read the first row for tankdat files
        newtotal = int(pt[1]) + amt
        if newtotal < int(pt[4]):               #if less than tank capacity, else set new amt to capacity
            pt[1] = str(int(pt[1]) + amt)       #increase tank level by fill amt indicated, draining tank
        else:
            pt[1] = str(pt[4])

        pt.pop()                            #remove last 'date' list item
        pt.append(datetime.datetime.now())  #re-append the updated date/time
        self.writecsvrow(tankcsvfile, pt)           #re-write the new filled value to csv
        #print(pt)
        return pt

    #TODO Add more tank dat files
    def updateallsimtanks(self):
        """updatesimtanks Docstring here"""
        simtanklist = []
        numofsimtanks = self.tanksimnum
        index = 1
        while(index <= numofsimtanks):
            simtanklist.append(self.writecsvrow('data/tankdat'+ str(index) +'.csv', self.simtankcallout(index)))
            index += 1

        #print(simtanklist)
        return simtanklist
