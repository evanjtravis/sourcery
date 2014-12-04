#!/usr/bin/env python
"""
A collection of handy utility functions used to set up the 'settings' git and
fun things in general.
"""

def get_file_contents( file_path, mode='r', lines=False ):
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
