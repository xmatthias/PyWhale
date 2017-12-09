# Author: Logan Schwartz
# This file is part of pywhale.
# pywhale is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pywhale is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser
# General Public LICENSE along with krakenex. If not, see
# <http://www.gnu.org/licenses/gpl-3.0.txt>.

import sys


class Api (object):
    """	Whaleclub.co cryptocurrency Exchange API Pyhon Client
        Connection Handler methods:"""

    verbose = False  # set to True if you get output twice

    def __init__(self, start_url='https://api.whaleclub.co/v1/',
                 BTC_real_key='', BTC_demo_key='',
                 DASH_real_key='', DASH_demo_key=''):
        """Create an object with authentication information.
        API Token could be find from your API Settings panel which is
        available from the top right menu in your trading dashboard.

        Args:
                DASH_demo_key -- DASH API Token for demo mode
                DASH_real_key -- DASH API Token for real mode
                BTC_demo_key  -- BTC API Token for demo mode
                BTC_real_key  -- BTC API Token for real mode


        """
        self.start_url = start_url
        self.BTC_demo_key = BTC_demo_key
        self.BTC_real_key = BTC_real_key
        self.DASH_demo_key = DASH_demo_key
        self.DASH_real_key = DASH_real_key
        self.load_tokens()

    def load_tokens(self):
        """Load API token from files
        BTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt
        """
        files = [
            "BTC_demo_key.txt",
            "BTC_real_key.txt",
            "DASH_demo_key.txt",
            "DASH_real_key.txt"]
        keys = []

        # open files and save token
        for file in files:
            f = open(file, 'r')
            key = f.readline().rstrip('\n')
            keys.append(key)

        # check if token exist
        for key in keys:
            if len(key) == 0:
                error_message = '''Error, at least one API token is missing.
Check that the API tokens in following files are correct and try again:
BTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt'''
                print(error_message)
                sys.exit(1)

        # update token with token loaded
        self.BTC_demo_key, self.BTC_real_key, self.DASH_demo_key, self.DASH_real_key = keys

    @staticmethod
    def _testsymbols(symb):
        if symb != '' and len(symb.split(',')) > 5:
            print('Error, You can only request information for up to '
                  '5 elements at once. Lower your input number and retry\n')
            return False
        return True

    def _updateKey(self, key):
        if key is None:
            key = self.default_key

        # test if key parameter value is an accepted input
        l = ['BTC_real_key', 'BTC_demo_key', 'DASH_real_key', 'DASH_demo_key']
        if key in l:
            i = l.index(key)
            k = [
                self.BTC_real_key,
                self.BTC_demo_key,
                self.DASH_real_key,
                self.DASH_demo_key]
            key = k[i]
        else:
            print("\nError, enter an acctepted value for key parameter, "
                  "could either be 'BTC_real_key', 'BTC_demo_key', "
                  "'DASH_real_key' or 'DASH_demo_key' \n")
            return (False, key)

        return (True, key)
