#!/usr/bin/env python
"""Module used to easily copy files while truncating common extensions and
adding common prefixes.
"""
import datetime
import os
import sys
import shutil
from myutils import list_files
from optparse import OptionParser

MYNAME = os.environ['USER']
PREFIX = ''
SUFFIX = ''
TEMPLATE = 'template'

DST = ''
OLD = ''
SRC = ''


class Opts():
    """Class whose members can be accessed in the same way as the
    options object in the OptionParser object.
    """
    def __init__(self, template, name, prefix, suffix):
        """Initialize the Opts object.
        """
        self.template = template
        self.name = name
        self.prefix = prefix
        self.suffix = suffix


def _check_for_old(filename):
    """If the given filename is in the DST directory, an old copy is made.
    """
    if os.path.isfile(filename):
        old_copy = filename + OLD
        shutil.copyfile(filename, old_copy)


def _copy_all(templates):
    """Copys all template files into the source directory.
    """
    for template_name in templates:
        template = os.path.join(SRC, template_name)
        new_filename = PREFIX + os.path.splitext(template_name)[0] + SUFFIX
        new_file = os.path.join(DST, new_filename)
        _check_for_old(new_file)
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


def _listify_args(args):
    """Returns a list whose elements are organized and accessed in the same
    way as the args object within the OptionParser object.
    Takes a list of arguments and determines if they are None.
    args order: [source, destination]
    """
    ret_args = []
    for elem in args:
        if elem != None:
            ret_args.append(elem)
    return ret_args


def _validate(options, args):
    """Set global variables.
    """
    global SRC
    global DST
    global MYNAME
    global TEMPLATE
    global PREFIX
    global SUFFIX
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
            raise Exception("Maximum of 2 arguments: SRC DST")
    if not os.path.isdir(SRC):
        raise Exception("Invalid Source argument. %s" % SRC)
    if not os.path.isdir(DST):
        raise Exception("Invalid Destination argument. %s" % DST)
    TEMPLATE = '.' + options.template
    if len(TEMPLATE) < 2:
        raise Exception("Invalid Template argument. %s" % TEMPLATE)
    MYNAME = options.name
    PREFIX = options.prefix
    SUFFIX = options.suffix
    OLD = '.OLD.%s.%s.%s.%s.%s.%s.%s.temp' % (
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        datetime.datetime.now().hour,
        datetime.datetime.now().minute,
        datetime.datetime.now().second,
        MYNAME
    )

#####################################################################

def _finish(options, args):
    """Execute the steps that the command line invoked and program invoked
    functions have in common.
    """
    _validate(options, args)
    templates = _get_templates()
    _copy_all(templates)


def copy_templates(
        source,
        destination=None,
        template=TEMPLATE,
        name=MYNAME,
        prefix=PREFIX,
        suffix=SUFFIX):
    """Copy all '.template' files from source to destination directory.
    Files are renamed without '.template' exention. Files can be renamed
    with a common prefix or suffix.
    This command is invoked by a python program.
    """
    options = Opts(template, name, prefix, suffix)
    args = _listify_args([source, destination])
    _finish(options, args)
    


def main():
    """Copy all '.template' files from source to destination directory.
    Files are renamed without '.template' exention. Files can be renamed
    with a common prefix or suffix.
    This command is invoked by the command line.
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
    parser.add_option(
        '-p',
        '--prefix',
        action='store',
        type='string',
        dest='prefix',
        default=PREFIX,
        help='When files are copied, they are copied with the prefix.'
    
    )
    parser.add_option(
        '-s',
        '--suffix',
        action='store',
        type='string',
        dest='suffix',
        default=SUFFIX,
        help='When files are copied, they are copied with the suffix.'
    )
    (options, args) = parser.parse_args()
    _finish(options, args)


if __name__ == "__main__":
    main()
