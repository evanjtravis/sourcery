#!/usr/bin/env python
"""A simple python function to get the service name of the current system
out of a list of known service names.
"""
import os


def determine_service():
    """Tries to determine the name of the service to log into based on an
    assumed file structure present in SDG dev systems.
    Assumed File Structure:
        /services/lost+found
                 /scratch
                 /smg-p
    """
    service_dir = '/services'
    assumed_dirs = ['lost+found', 'scratch', 'smg-p']

    slash_services = os.listdir(service_dir)
    possible_services = []

    for item in slash_services:
        item_path = os.path.join(service_dir, item)
        if (not os.path.isfile(item_path)) and (item not in assumed_dirs):
            possible_services.append(item)

    if (len(possible_services) == 1):
        return possible_services[0]
    else:
        return None


def main():
    """The main function of the program.
    It prints the name of the service to be captured by bash source file.
    """
    SERVICE = determine_service()
    print SERVICE


if __name__ == "__main__":
    main()
