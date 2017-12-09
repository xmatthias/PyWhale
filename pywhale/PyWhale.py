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
from pywhale.trade.Api import Api
from pywhale.trade.General import General
from pywhale.trade.Live import Live
from pywhale.trade.Turbo import Turbo


class PyWhale(General, Live, Turbo):
    """Whaleclub.co cryptocurrency Exchange API Pyhon Client"""

    def __init__(self, start_url='https://api.whaleclub.co/v1/'):
        Api.__init__(self, start_url=start_url)

        General.__init__(self)
        Live.__init__(self)
        Turbo.__init__(self)

        PyWhale.print_welcome()

        self.start_url = start_url
        # set the key that will be used when no value is given in key parameter
        self.default_key = 'BTC_demo_key'

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
    def print_welcome():
        """Print welcome message """
        print()
        print('#' * 49)
        print('#' * 6, ' ' * 9, "Welcome to PyWhale", ' ' * 6, '#' * 6)
        print('#' * 6, ' ' * 4, "Python wrapper for whaleclub.co", '#' * 5)
        print('#' * 49)
        print()
        print("API token loaded, ready to trade!")
        print("type PyWhale.help() at anytime to see available functions")


# pylint: disable=C0103
pw = PyWhale()
