#!/usr/bin/env python
"""
To be run upon initialization. Sets up pip initially. A one-off pattern.
"""
# TODO check connection to internet first.
import os, sys, urllib2


PIP_LOCATION = 'https://bootstrap.pypa.io/get-pip.py'
BASE = os.path.dirname(os.path.realpath(__file__))
FILENAME = 'get-pip.py'

def main():
    """
    The main function of this module.
    """
    filename = os.path.join(BASE, FILENAME)
    old_text = ''
    try:
        response = urllib2.urlopen(PIP_LOCATION)
    except urllib2.URLError:
        print "No connection to internet."
        sys.exit(1)

    html = response.read()
    
    if os.path.isfile(filename) == False:
        get_pip = open(filename, 'w')
        get_pip.write(html)
        get_pip.close()

if __name__ == "__main__":
    main()
