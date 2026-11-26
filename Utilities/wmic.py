#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Windows WMIC utility                                                       #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 21-03-05 |  0.0.1  | asasson  | Initial draft                              #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################

import subprocess


class Memory():
    GB = 1073741824
    PROP = ["devicelocator", "manufacturer", "partnumber", "serialnumber", "capacity", "speed", "memorytype", "formfactor"]
    FORM_FACTORS = ["Unknown", "Other", "SIP", "DIP", "ZIP", "SOJ", "Proprietary", "SIMM", "DIMM", "TSOP",
                 "PGA", "RIMM", "SODIMM", "SRIMM", "SMD", "SSMP", "QFP", "TQFP", "SOIC", "LCC",
                 "PLCC", "BGA", "FPBGA", "LGA", "FB-DIMM"]
    MEM_TYPES = ["Unknown", "Other", "DRAM", "Synchronous DRAM", "Cache DRAM",
          "EDO", "EDRAM", "VRAM", "SRAM", "RAM",
          "ROM", "Flash", "EEPROM", "FEPROM", " EPROM",
          "CDRAM", "3DRAM", "SDRAM", "SGRAM", "RDRAM",
          "DDR", "DDR2", "DDR2 FB-DIMM", "", "DDR3", "FBD2"]

    def capacity(self):
        capstr = subprocess.check_output("wmic memorychip get capacity").decode()
        print(capstr, "***********")
        cap = 0
        lastfind = capstr.find("\r\r\n") + 3
        find = capstr.find("\r\r\n",  lastfind) + 3
        while(find > 2):
            bankcap = capstr[lastfind : find - 5]
            print(bankcap)
            cap += int(bankcap)
            lastfind = find
            find = capstr.find("\r\r\n",  lastfind + 1) + 3
        return cap / Memory.GB

    def query(self, prop = ["capacity"]):
        s = ""
        for p in prop:
            p = p.lower()
            if(p in self.PROP):
                s += p + ", "

        return self.wmic(str(s[0:-2]))

    def wmic(self, prop):
        cmd = "wmic memorychip get devicelocator, " + prop
        return subprocess.check_output(cmd).strip().decode()

    def memlist(self):
        memstr = subprocess.check_output("wmic memorychip list full").decode()
        #print(memstr)
        out = []
        lastfind = 0
        find = memstr.find("\r\r\n\r\r\n\r\r\n")
        while(find != -1):
            d = {}
            paragraph = memstr[lastfind:find].strip()
            linebreak = 0
            efind = paragraph.find('=')
            while(efind != -1):
                rfind = paragraph.find("\r\r\n", efind + 1)
                if(rfind == -1):
                    break
                else:
                    k = paragraph[linebreak:efind]
                    #print(k)
                    v = paragraph[efind+1 : rfind]
                    #print(v)
                    d[k] = v
                    linebreak = rfind + 3
                    efind = paragraph.find('=', linebreak)
            out.append(d)
            #print("********************************")
            lastfind = find + 1
            find = memstr.find("\r\r\n\r\r\n\r\r\n", lastfind)
        out.pop()
        return out

if __name__ == '__main__':
    mem = Memory()
    ml =  mem.memlist()
    #print(mem.query(["manufacturer", "partnumber", "serialnumber", "capacity", "speed"]))
    cap = mem.capacity()
