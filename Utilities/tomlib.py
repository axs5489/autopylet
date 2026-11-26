#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# TOML utility                                                               #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.0.1'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 26-11-25 |  0.0.1  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################
import tomllib

def toml_init(filename="project.toml"):
    with open(filename, "rb") as file:
        prj_data = tomllib.load(file)

if __name__ == "__main__":
    toml_init()
