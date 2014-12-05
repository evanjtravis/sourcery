#!/usr/bin/env python
"""Module used to 
"""
import datetime
import os
import sys
import shutil
from optparse import OptionParser

MYNAME = os.environ['USER']
DST = ''
SRC = ''
TEMPLATE = 'template'
OLD = ''



def list_files(path):
    """Returns a list of all files in a directory.
    """
    if os.path.isdir(path):
        files = [f for f in os.listdir(path)\
                if os.path.isfile(os.path.join(path, f))]
        if len(files) == 0:
            print os.listdir(path)
            raise Exception("No files in '%s'." % path)
        return files
    else:
        raise Exception("Not a valid directory '%s'." % path)


def _check_dst(templates):
    """Checks to make sure destination is a directory.
    Copies files that have the same names as templates older versions.
    """
    if os.path.isfile(DST):
        raise Exception('Destination is a file.')
    elif os.path.isdir(DST):
        files = list_files(DST)
        for filename in templates:
            new = os.path.splitext(filename)[0]
            if new in files:
                old = os.path.join(DST, new)
                new = old + OLD
                shutil.copyfile(old, new)


def _copy_all(templates):
    """Copys all template files into the source directory.
    """
    for filename in templates:
        template = os.path.join(SRC, filename)
        new_file = os.path.join(DST, os.path.splitext(filename)[0])
        shutil.copyfile(template, new_file)


def _get_templates():
    """Returns a list of all files with TEMPLATE extension.
    """
    templates = []
    files = list_files(SRC)
    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension == TEMPLATE:
            templates.append(name + extension)
    if len(templates) == 0:
        raise Exception('No template \'%s\' files found.\n\t%s\n\t%s' %
                (TEMPLATE, SRC, files))
    return templates


def _validate(options, args):
    """Set global variables.
    """
    global SRC
    global DST
    global MYNAME
    global TEMPLATE
    global OLD

    if len(args) == 0:
        raise Exception("Need at least 1 argument: SRC")
    else:
        SRC = args[0]
        if len(args) == 1:
            DST = args[0]
        elif len(args) == 2:
            DST = args[1]
        else:
            raise Exception("Need at most 2 arguments: SRC DST")
    TEMPLATE = '.' + options.template
    MYNAME = options.name
    OLD = '.OLD.%s.%s.%s.%s.%s.%s.%s.temp' % (
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        datetime.datetime.now().hour,
        datetime.datetime.now().minute,
        datetime.datetime.now().second,
        MYNAME
    )
# TODO add option to copy files as hidden so that hey can be stored in settings as unhidden files.
def main():
    """Copy all '.template' files from source to destination directory.
    Files are renamed without '.template' exention.
    """
    parser = OptionParser()
    parser.add_option(
        '-t',
        '--template',
        action='store',
        type='string',
        dest='template',
        default=TEMPLATE,
        help='Specify an alternate template file extention.'
    )
    parser.add_option(
        '-n',
        '--name',
        action='store',
        type='string',
        dest='name',
        default=MYNAME,
        help='Specify an alternate name for old files.'
    )
    (options, args) = parser.parse_args()
    _validate(options, args)
    templates = _get_templates()
    _check_dst(templates)
    _copy_all(templates)
    sys.exit(0)


if __name__ == "__main__":
    main()
