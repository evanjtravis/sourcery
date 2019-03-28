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
    
    @property
    def save(self, path=None):
        """save console work"""
        executable = os.path.join(os.environ["SOURCERY"],
                "lib/python/save_pyhistory.bash")
        self.sh("{}".format(executable))


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

