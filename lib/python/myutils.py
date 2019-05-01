#!/usr/bin/env python
"""
A collection of handy utility functions used to set up the 'settings' git and
fun things in general.
"""

#import copy_templates as cp_templates
import os
import subprocess
import sys


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
    
    def _trunc_hist(self):
        """Remove py.* commands from ptpython history file after executing them"""
        executable = os.path.join(os.environ["SOURCERY"],
                "lib/python/trunc_hist.bash")
        subprocess.run(executable)


    def _sh(self, *args, **kwargs):
        """"""
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


    @property
    def save(self, path=None):
        """save console work"""
        #self._trunc_hist()
        executable = os.path.join(os.environ["SOURCERY"],
                "lib/python/save_pyhistory.bash")
        self._sh(executable)


    @property
    def c(self):
        """"""
        #self._trunc_hist()
        self._sh("clear")


    @property
    def q(self):
        #self._trunc_hist()
        quit()


    @property
    def up(self):
        #self._trunc_hist()
        os.chdir("..")
        self._sh("pwd")
        self._sh("ls", "-la")


    @property
    def home(self):
        #self._trunc_hist()
        os.chdir(os.path.expanduser("~/"))
        self._sh("ls", "-la")


    @property
    def version(self):
        #self._trunc_hist()
        print("Python ", sys.version, "on linux")
        print(('Type "help", "copyright", "credits" or "license" for '
            'more information.'))


    def cd(self, path):
        #self._trunc_hist()
        os.chdir(os.path.expanduser(path))
        self._sh("pwd")
        self._sh("ls", "-la")
    

    def sh(self, *args, **kwargs):
        """execute shell command"""
        #self._trunc_hist()
        self._sh(*args, **kwargs)


py = PythonConsole()

