#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Servo controller base class                                                #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 19-03-19 |  0.0.1  | asasson  | Initial draft                              #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################
import time
from Utilities import SerialPortDevice

class ServoDevice():
    """ This class controls the servo Serial Port """
    def __init__(self, address):
        super(ServoDevice,self).__init__(address)
        if address:
            self.connection = SerialPortDevice(address, async=True, name="Servo", tx_term = '\r',echos=False)
        else:
            self.serial_Servo = None

    def __del__(self):
        self.close()

    def close(self):
        """ Closes the serial port and stops the Asynchronous read-thread. """
        if self.connection:
            self.connection.close()
            del self.connection
        self.connection = None

    def ServoEnabled(self):
        return True if self.connection else False

    def off(self):
        if self.connection:
            self.connection.send('set 0 off')
            time.sleep(1)

    def Ld(self):
        if self.connection:
            self.connection.send('set 0 l')
            time.sleep(1)

    #will eventually make this compatible with all slots.
    def ServoControlSlot1(self):
        if self.connection:
            self.connection.send('set 0 1')
            time.sleep(1)

    #Note: Untested, dont jump too many slots!
    def ServoControlSlotX(self, slot):
        if self.connection:
            self.connection.send('set 0 %d' %slot)
            time.sleep(1)
