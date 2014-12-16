#!/usr/bin/env python
"""Module used to easily copy files while truncating common extensions and
adding common prefixes.
"""
import datetime
import os
import shutil
from optparse import OptionParser

# Dictionary of all private variables
_ARGS = {
    'FORCE':  False,
    'MYNAME': os.environ['USER'],
    'OLD': '',
    'PREFIX': '',
    'SUFFIX': '',
    'TEMPLATE': 'template',
    'DST': None,
    'SRC': ''
}

#####################################################################
# Module Specific Definitions
#####################################################################
# Public
def get_option(key):
    """Access the values stored in the the global variables of this module.
    """
    ALL = 'ALL'
    key = key.upper()
    if key == ALL:
        return _ARGS.copy()
    else:
        try:
            return _ARGS[key]
        except KeyError as err:
            print("Valid inputs: %s, or %s." % (_ARGS.keys(), ALL))
            raise err

# Private
class _EMPTY():
    """Class whose members can be accessed in the same way as the
    options object in the OptionParser object.
    Attributes are assigned in the copy_templates function.
    """
    pass


def _check_for_old(filename):
    """If the given filename is in the DST directory, an old copy is made.
    """
    OLD = _ARGS['OLD']

    if os.path.isfile(filename):
        old_copy = filename + OLD
        shutil.copyfile(filename, old_copy)


def _copy_all(templates):
    """Copys all template files into the source directory.
    """
    for template_name in templates:
        template = os.path.join(_ARGS['SRC'], template_name)
        new_filename = _ARGS['PREFIX'] + \
                os.path.splitext(template_name)[0] + _ARGS['SUFFIX']
        new_file = os.path.join(_ARGS['DST'], new_filename)
        if _ARGS['FORCE'] == False:
            _check_for_old(new_file)
        shutil.copyfile(template, new_file)


def _get_templates():
    """Returns a list of all files with TEMPLATE extension.
    """
    templates = []
    files = list_files(_ARGS['SRC'])
    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension == _ARGS['TEMPLATE']:
            templates.append(name + extension)
    if len(templates) == 0:
        raise Exception('No template \'%s\' files found.\n\t%s\n\t%s' %
                (_ARGS['TEMPLATE'], _ARGS['SRC'], files))
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
    if len(args) == 0:
        raise Exception("Need at least 1 argument: SRC")
    else:
        _ARGS['SRC'] = args[0]
        if len(args) == 1:
            _ARGS['DST'] = args[0]
        elif len(args) == 2:
            _ARGS['DST'] = args[1]
        else:
            raise Exception("Maximum of 2 arguments: SRC DST")
    if not os.path.isdir(_ARGS['SRC']):
        raise Exception("Invalid Source argument. %s" % _ARGS['SRC'])
    if not os.path.isdir(_ARGS['DST']):
        raise Exception("Invalid Destination argument. %s" % _ARGS['DST'])
    _ARGS['FORCE'] = options.force
    _ARGS['TEMPLATE'] = '.' + options.template
    if len(_ARGS['TEMPLATE']) < 2:
        raise Exception("Invalid Template argument. %s" % _ARGS['TEMPLATE'])
    _ARGS['MYNAME'] = options.name
    _ARGS['PREFIX'] = options.prefix
    _ARGS['SUFFIX'] = options.suffix
    _ARGS['OLD'] = '.OLD.%s.%s.%s.%s.%s.%s.%s.temp' % (
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        datetime.datetime.now().hour,
        datetime.datetime.now().minute,
        datetime.datetime.now().second,
        _ARGS['MYNAME']
    )

#####################################################################
# MAIN
#####################################################################
def copy_templates(
        source,########################### Arguments
        destination=_ARGS['DST'],
        template=_ARGS['TEMPLATE'],####### Options
        name=_ARGS['MYNAME'],
        prefix=_ARGS['PREFIX'],
        suffix=_ARGS['SUFFIX'],
        force=_ARGS['FORCE']):
    """Copy all '.template' files from source to destination directory.
    Files are renamed without '.template' exention. Files can be renamed
    with a common prefix or suffix.
    This command is invoked by a python program.
    """
    options = _EMPTY()
    ##############################
    options.template = template
    options.name = name
    options.prefix = prefix
    options.suffix = suffix
    options.force = force
    ##############################
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
        default=_ARGS['TEMPLATE'],
        help='Specify an alternate template file extention.'
    )
    parser.add_option(
        '-n',
        '--name',
        action='store',
        type='string',
        dest='name',
        default=_ARGS['MYNAME'],
        help='Specify an alternate name for old files.'
    )
    parser.add_option(
        '-p',
        '--prefix',
        action='store',
        type='string',
        dest='prefix',
        default=_ARGS['PREFIX'],
        help='When files are copied, they are copied with the prefix.'
    
    )
    parser.add_option(
        '-s',
        '--suffix',
        action='store',
        type='string',
        dest='suffix',
        default=_ARGS['SUFFIX'],
        help='When files are copied, they are copied with the suffix.'
    )
    parser.add_option(
        '-f',
        '--force',
        action='store_true',
        dest='force',
        default=_ARGS['FORCE'],
        help='Do not save files with the same name with OLD extensions.'
    )
    (options, args) = parser.parse_args()
    _finish(options, args)


def _finish(options, args):
    """Execute the steps that the command line invoked and program invoked
    functions have in common.
    """
    _validate(options, args)
    templates = _get_templates()
    _copy_all(templates)

#####################################################################
# UTILITIES
#####################################################################

def list_files(path):
    """Returns a list of all files in a directory.
    If path is a file, returns list of all files in that file's directory.
    """
    if os.path.isdir(path):
        files = [f for f in os.listdir(path)\
            if os.path.isfile(os.path.join(path, f))]
        return files
    elif os.path.isfile(path):
        # If path is a file, return list of files of parent directory.
        return list_files(os.path.split(path)[0])
    else:
        raise Exception("Invalid path $s." % path)

#####################################################################
# END UTILITIES
#####################################################################

if __name__ == "__main__":
    main()

