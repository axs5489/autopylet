#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# VXI11 Adapter class                                                        #
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

try:
    from .vxi11 import VXI11Adapter
except ImportError:
    import vxi11
except ImportError:
    print('Failed to import vxi11 package, which is required for the VXI11Adapter')

from .adapter import Adapter


class VXI11Adapter(Adapter):
    """ VXI11 Adapter class. Provides a adapter object that
        wraps around the read, write and ask functionality
        of the vxi11 library.

    :param host: string containing the visa connection information.

    """

    def __init__(self, host, **kwargs):

        # Filter valid arguments that can be passed to vxi instrument
        valid_args = ["name", "client_id", "term_char"]
        self.conn_kwargs = {}
        for key in kwargs:
            if key in valid_args:
                self.conn_kwargs[key] = kwargs[key]

        self.connection = vxi11.Instrument(host, **self.conn_kwargs)

    def __repr__(self):
        return '<VXI11Adapter(host={})>'.format(self.connection.host)

    def write(self, command):
        """ Wrapper function for the write command using the vxi11 interface.

        :param command: string with command the that will be transmitted
                         to the instrument.
        """
        self.connection.write(command)

    def read(self):
        """ Wrapper function for the read command using the    vxi11 interface.

        :return string containing a response from the device.
        """
        return self.connection.read()

    def ask(self, command):
        """ Wrapper function for the ask command using the vxi11 interface.

        :param command: string with the command that will be transmitted
                        to the instrument.
        :returns string containing a response from the device.
        """
        return self.connection.ask(command)

    def write_raw(self, command):
        """ Wrapper function for the write_raw command using the vxi11 interface.

        :param command: binary string with the command that will be
                        transmitted to the instrument
        """
        self.connection.write_raw(command)

    def read_raw(self):
        """ Wrapper function for the read_raw command using the    vx11 interface.

        :returns binary string containing the response from the device.
        """
        return self.connection.read_raw()

    def ask_raw(self, command):
        """ Wrapper function for the ask_raw command using the vxi11 interface.

        :param command: binary string with the command that will be
                        transmitted to the instrument

        :returns binary string containing the response from the device.
        """
        return self.connection.ask_raw(command)
