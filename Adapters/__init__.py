#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Adapter class imports                                                      #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 20-07-10 |  0.0.1  | asasson  | Initial draft                              #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################

from .adapter import Adapter, FakeAdapter

try:
    from .visa import VISAAdapter
except ImportError:
    print("ERROR! PyVISA library could not be loaded")

try:
    from .serial import SerialAdapter
    #from pymeasure.adapters.prologix import PrologixAdapter
except ImportError:
    print("ERROR! PySerial library could not be loaded")

try:
    from .vxi11 import VXI11Adapter
except ImportError:
    print("ERROR! VXI-11 library could not be loaded")
