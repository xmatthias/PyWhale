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

import json


class Api(object):
    """	Whaleclub.co cryptocurrency Exchange API Pyhon Client
        Connection Handler methods:"""

    verbose = False  # set to True if you get output twice

    keydict = {
        "BTC_demo_key": "",
        "BTC_real_key": "",
        "DASH_demo_key": "",
        "DASH_real_key": "",
    }
    default_key = "BTC_demo_key"
    loaded = False

    def __init__(self, start_url='https://api.whaleclub.co/v1/'):
        """Create an object with authentication information.
        API Token could be find from your API Settings panel which is
        available from the top right menu in your trading dashboard.
        """
        # initialize only once
        if not self.loaded:
            self.start_url = start_url
            self.load_tokens()
            self.loaded = True

    def load_tokens(self):
        """Load API token from files
        BTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt
        """
        files = [
            "BTC_demo_key.txt",
            "BTC_real_key.txt",
            "DASH_demo_key.txt",
            "DASH_real_key.txt"]
        # open files and save token
        for file in files:
            fil = open(file, 'r')
            keyname = file[:-4]
            if keyname in self.keydict:
                self.keydict[keyname] = fil.readline().rstrip('\n')

    def _updateKey(self, key):
        if key is None:
            key = self.default_key

        # Return if key exists
        if key in self.keydict:
            return(True, self.keydict[key])

        print("\nError, undefined key parameter ", key, ".")
        print("enter an acctepted value for key parameter, "
              "could either be 'BTC_real_key', 'BTC_demo_key', "
              "'DASH_real_key' or 'DASH_demo_key' \n")
        return(False, None)

    def _checkresp(self, resp):
        """Check whenever an response return an error"""
        parsed = json.loads(resp.text)

        # every thing is ok
        if resp.status_code == 200 or resp.status_code == 201:
            if self.verbose:
                print(json.dumps(parsed, indent=4, sort_keys=True))
            return parsed

        # we have an error
        else:
            print('\nOOps, somethings went Wrong!\n')

            try:
                print(parsed['error']['name'])
                print(parsed['error']['message'])
            except BaseException:
                print(parsed)

    @staticmethod
    def _testsymbols(symb):
        if symb != '' and len(symb.split(',')) > 5:
            print('Error, You can only request information for up to '
                  '5 elements at once. Lower your input number and retry\n')
            return False
        return True
