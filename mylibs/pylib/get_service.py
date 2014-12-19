#!/usr/bin/env python
"""A simple python function to get the service name of the current system
out of a list of known service names.
"""
import os


def main():
    """The main function of the program.
    It prints the name of the service to be captured by bash source file.
    """
    HOST = os.environ['HOST']
    SERVICE = ''

    # HOST: SERVICE
    services = {
        'orwell': 'security-tools',
        'caboose': 'sdg-sandbox',
        'spacereq': 'crl-svcs'
    }
    if '-' in HOST:
        SERVICE = HOST.split('-')[0]
    else:
        SERVICE = HOST.split('.')[0]

    if SERVICE in services.keys():
        try:
            print services[SERVICE]
        except KeyError:
            print None
    else:
        print None



if __name__ == "__main__":
    main()

