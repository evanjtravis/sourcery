#!/usr/bin/env python
"""
A collection of handy utility functions used to set up the 'settings' git and
fun things in general.
"""

#import copy_templates as cp_templates
import datetime
import os
import subprocess
import sys

NOW = datetime.datetime.now()

RESERVE_SAVE_PATH = "~/python_interpreter_savefile_{}.{}.{}.file".format(
    str(NOW.date()),
    str(NOW.hour),
    str(NOW.minute)
)

def _get_default_save_path():
    path = "~/python_workbench.file"
    if os.path.isfile(path):
        path = RESERVE_SAVE_PATH
    return path

#####################################################################
# Shortcuts
#####################################################################

#_CP_OPTS = cp_templates.get_option

def _print_pwd():
    """"""
    print("{}\n".format(os.getcwd()))


#####################################################################
# End Shortcuts
#####################################################################

class PythonConsole(object):
    
    @property
    def save(self, path=None):
        """save console work"""
        if not path:
            path = _get_default_save_path()
        path = os.path.expanduser(path)
        import readline
        readline.write_history_file(path)


    @property
    def c(self):
        """"""
        self.sh("clear")


    @property
    def q(self):
        quit()


    @property
    def up(self):
        os.chdir("..")
        self.sh("pwd")
        self.sh("ls", "-la")


    @property
    def home(self):
        os.chdir(os.path.expanduser("~/"))
        self.sh("ls", "-la")


    @property
    def version(self):
        print("Python ", sys.version, "on linux")
        print(('Type "help", "copyright", "credits" or "license" for '
            'more information.'))


    def cd(self, path):
        os.chdir(os.path.expanduser(path))
        self.sh("pwd")
        self.sh("ls", "-la")
    

    def sh(self, *args, **kwargs):
        """execute shell command"""
        defaults = {
            "shell": True,
            "executable": "/bin/bash"
        }
        for key,value in defaults.items():
            if key not in kwargs:
                kwargs[key] = value
        proc = subprocess.run(args, **kwargs)
        if not proc.returncode:
            print(proc.stdout)
        else:
            print(proc.stderr)
        return proc


py = PythonConsole()

