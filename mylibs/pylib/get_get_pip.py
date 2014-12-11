#!/usr/bin/env python
"""
To be run upon initialization. Sets up pip initially. A one-off pattern.
"""

import os, urllib2


PIP_LOCATION = 'https://bootstrap.pypa.io/get-pip.py'
BASE = os.path.dirname(os.path.realpath(__file__))
FILENAME = 'get-pip.py'

def main():
    """
    The main function of this module.
    """
    filename = os.path.join(BASE, FILENAME)
    old_text = ''

    response = urllib2.urlopen(PIP_LOCATION)
    html = response.read()

    if not os.path.isfile(filename):
        with open(filename, 'w') as newfile:
            newfile.write(html)

if __name__ == "__main__":
    main()
