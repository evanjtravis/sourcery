#!/usr/bin/env python
"""
A collection of handy utility functions used to set up the 'settings' git and
fun things in general.
"""

import os

def get_file_contents(file_path, mode='r', lines=False):
    """Returns contents of the file.
    Opens the specified file, reads it into a string, closes the file, returns
    string.
    Will only READ files. mode defaults to 'r' if it is invalid.
    You can read lines or the entire file itself. lines defaults to False.
    """
    if 'b' in mode:
        mode = 'rb'
    if 'U' in mode:
        mode = 'rU'
    if 'r' not in mode:
        mode = 'r'

    with open(file_path, mode) as the_file:
        if lines:
            the_text = the_file.readlines()
        else:
            the_text = the_file.read()
    
    return the_text


def list_files(path):
    """Returns a list of all files in a directory.
    If path is a file, returns list of all files in that file's directory.
    """
    if os.path.isdir(path):
        files = [f for f in os.listdir(path)\
            if os.path.isfile(os.path.join(path, f))]
        return files
    elif os.path.isfile(path):
        # TODO warning, path is file
        return list_files(os.path.split(path)[0])
    else:
        raise Exception("Invalid path $s." % path)

