import sys
from os import chdir, getcwd

def load_project(cd=''):
    if cd:
        chdir(cd)
    sys.path.append(getcwd())
    __import__('__init__')
