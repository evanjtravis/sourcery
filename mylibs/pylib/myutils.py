#!/usr/bin/env python
"""
A collection of handy utility functions used to set up the 'settings' git and
fun things in general.
"""

import copy_templates as cp_templates
import os, sys

#####################################################################
# Shortcuts
#####################################################################

_CP_OPTS = cp_templates.get_option

#####################################################################
# End Shortcuts
#####################################################################
def c():
    """A less verbose clear command wrapper.
    """
    clear()


def cd(directory):
    """Wrapper for changing current directory."""
    if '~/' in directory:
        directory = directory.replace('~/', os.environ['HOME'])
    os.chdir(directory)


def cdd():
    """Move up one directory."""
    os.chdir('..')


def cdh():
    """Go to home directory."""
    cd('~/')


def clear():
    """Clear the terminal in the python interpreter shell.
    """
    temp = os.system('clear')
    del temp
    print_intro()


def copy_templates(
        source,
        destination=_CP_OPTS('dst'),
        template=_CP_OPTS('src'),
        name=_CP_OPTS('myname'),
        prefix=_CP_OPTS('prefix'),
        suffix=_CP_OPTS('suffix'),
        force=_CP_OPTS('force')):
    """Wrapper for function found in copy_templates.py
    """
    cp_templates.copy_templates(
        source,
        destination=destination,
        template=template,
        name=name,
        prefix=prefix,
        suffix=suffix,
        force=force
    )


def ENV(var=None):
    """Display environment variable defined by var.
    If var is None, display entire environment.
    """
    data = {}
    if var == None:
        data = os.environ
    else:
        data[var] = os.environ[var]

    if is_interactive():
        pretty_print(dict(data), name='Environment')
    else:
        return data


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


def is_interactive():
    """Determine if methods are called from an interactive shell."""
    return sys.__stdin__.isatty()


def list_files(path):
    """Wrapper for list_files function in copy_templates.py
    """
    return cp_templates.list_files(path)


def ls(path=None):
    """Wrapper for listing directory items."""
    files = []
    directories = []
    if path == None:
        path = pwd()
    contents = os.listdir(path)
    for elem in contents:
        item = os.path.join(path, elem)
        if os.path.isdir(item):
            directories.append(elem)
        elif os.path.isfile(item):
            files.append(elem)
    files.sort()
    directories.sort()
    
    if is_interactive():
        print path
        pretty_print(directories, name='Directories')
        pretty_print(files, name='Files')
    else:
        return files, directories


def pretty_print(the_item, name=None, level=0):
    """Print an object out in a pretty way.
    If the object is named, the name is printed and the contents are tabbed
    underneath.
    Supports dicts and lists
    """
    # TODO determine rows and columns to print out 2D+ lists prettily
    level = level
    padding = ' ' * 4
    def pad(level, count=1, mode='+'):
        """Add and remove indentation in a uniform way.
        Optional Arguments:
            Count determines number of times operation is performed.
                If count == 0, None, or False, then level is reset to 0
            Mode determines if padding is added or subtracted.
                '+' or '-'
        """
        if not count:
            return 0
        if mode == '+':
            for _ in range(count):
                level += 1
        elif mode == '-':
            for _ in range(count):
                level -= 1
        if level < 0:
            level = 0
        return level
    ##############################
    if name:
        print "%s%s" % (padding*level, name)
        level = pad(level)

    if isinstance(the_item, list):
        for elem in the_item:
            print "%s%s" % (padding*level, elem)

    elif isinstance(the_item, dict):
        for key, value in the_item.items():
            print "%s%-20s%20s" % (padding*level, key, value)


def print_intro():
    """Print initial greeting given by interpreter.
    The greeting holds the same information including the python
    version and a list of helpful commands.
    """
    print "Python", sys.version, "on linux2"
    print 'Type "help", "copyright", "credits" or "license" for more information.'


def pwd():
    """Wrapper for getting current working directory."""
    return os.getcwd()


def q():
    """A less verbose quit command wrapper.
    """
    quit()


