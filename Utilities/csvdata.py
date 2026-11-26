#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Delimited data utility to load or save data                                #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 19-03-03 |  0.0.1  | asasson  | Initial draft                              #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################
import csv
import os
import sys

class DelimitedData():
    def __init__(self, path=None):
        self._path = path
        self.load = False
        self.saved = False
        self.data = []
        self.numrows = 0
        if(path is not None):
            if(isinstance(path, str) and os.path.exists(path)):
                self.importFile(path, dlm=',')
            else:
                self.loadData(None, path)

    def __del__(self):
        self.close()

    def close(self):
        if(not self.saved):
            print("DeleteSave ", self.__hash__())
            self.save()
        self._path = None
        self.saved = None
        self.cols = None
        self.data = None
        self.numrows = None
        print("Closed")

    def __str__(self):
        dd = ""
        for field in self.cols:
            dd += field + "\t\t\t"
        dd += "\n\r"
        for rec in self.data:
            print(rec)
            for item in rec:
                dd += str(item) + "\t\t\t"
            dd += "\n\r"

        return dd

    def importFile(self, path, dlm=','):
        if(path != None and os.path.exists(path)):
            with open(path, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=dlm, skipinitialspace=True)
                line_count = 0
                for row in csv_reader:
                    copy = row
                    print(copy)
                    if line_count == 0:
                        self.cols = copy
                        print(self.cols)
                    else:
                        self.data.append(copy)
                    line_count += 1
    
                self.numrows = line_count
                print(self.numrows)

    def importFileDict(self, path, dlm=','):
        if(path != None and os.path.exists(path)):
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=dlm, skipinitialspace=True)
                line_count = 0
                for row in csv_reader:
                    copy = row
                    if line_count == 0:
                        self.cols = copy
                        print(self.cols)
                    else:
                        self.data.append(copy)
                    line_count += 1
    
                self.numrows = line_count
                print(self.numrows)

    def loadData(self, cols, data):
        self.cols = cols
        self.data = data
        self.load = True

    def save(self, savpath = None, dlm=','):
        if(self._path != None):
            with open(self._path, mode='w', newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=dlm, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(self.cols)

                for rec in self.data:
                    writer.writerow(rec)

            self.saved = True
        else:
            print("Please specify a path")

    def saveDict(self, savpath = None, dlm=','):
        if(self._path != None and hasattr(self,"cols")):
            with open(self._path, mode='w', newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.cols)
                writer.writeheader()
                writer.writerow(self.cols)
                

                for rec in self.data:
                    writer.writerow(rec)
        else:
            print("Please specify a path")

    def sort(self):
        self.data = sorted(self.data)

    def filtered(self, search, col=1):
        fdata = []
        if(isinstance(col, str)):
            for i, c in enumerate(self.cols):
                if(col == c):
                    col = i
                    break
        for row in sorted(self.data):
            if(search in row[col]):
                fdata.append(row)
        return fdata

    def filterout(self, search):
        fdata = []
        for row in sorted(self.data):
            notfound = True
            print(row)
            for c in row:
                #print(c)
                if(search in c):
                    notfound = False
            if(notfound):
                fdata.append(row)
        return fdata

if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)
    path = "BOM\\resistors-agile.csv"

    dd = DelimitedData(path)
    dds = DelimitedData()
    da = dd.data
    ds = sorted(da)
    dds.loadData(None, ds)
