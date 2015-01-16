#!/usr/bin/env python

import os
from optparse import OptionParser
from ConfigParser import ConfigParser

_ARGS = {
    'DISABLE_LOG': False,
    'CUT': False,
    'HELP': False,
    'VERBOSE': False
}


def _validate(options, args):
    


def log():
    pass


def pinch():
    pass


def main():
    parser = OptionParser()
    parser.add_option(
        '-x',
        '--cut',
        action='store_true',
        dest='cut',
        default=_ARGS['CUT'],
        help='Delete lines from source file and paste to destination file.'
    )
    parser.add_option(
        '-v',
        '--verbose',
        action='store_true',
        dest='verbose',
        default=_ARGS['VERBOSE'],
        help='Execute program while printing important messages.'
    )
    parser.add_option(
        '-d',
        '--disable-log',
        action='store_true',
        dest='disable-log',
        default=_ARGS['DISABLE_LOG'],
        help='Disable program logs during execution.'
    )
    parser.add_option(
        '-h',
        '--help',
        action='store_true',
        dest='help',
        default=_ARGS['HELP'],
        help='Display this help.'
    )
    parser.add_option(
        '-i',
        '--input-file',
        action='store',
        dest='input_file',
        default=_ARGS['INPUT_FILE'],
        help='Provide input file to the program.'
    )
    (options, args) = parser.parse_args()
    _validate(options, args)

if __name__ == "__main__":
    main()
