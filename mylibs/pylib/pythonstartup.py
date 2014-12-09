#!/usr/bin/env python
"""Some helpful interactive shell functions.
This file is currently set to the PYTHONSTARTUP environment variable.
"""
import os, sys

def clear():
    """Clear the terminal in the python interpreter shell.
	
    """
    temp = os.system('clear')
    del temp
    print_intro()

def print_intro():
    """Print initial greeting given by interpreter.

    The greeting holds the same information including the python
    version and a list of helpful commands.
    """
    print "Python", sys.version, "on linux2"
    print 'Type "help", "copyright", "credits" or "license" for more information.'

def c():
    """A less verbose clear command wrapper.
    """
    clear()

def q():
    """A less verbose quit command wrapper.
    """
    quit()
