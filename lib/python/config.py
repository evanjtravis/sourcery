import os
from configparser import ConfigParser

DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser()
config.read(os.path.join(DIR, "python.config"))
