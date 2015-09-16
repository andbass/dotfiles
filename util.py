
import importlib
import os

from os import path
from glob import glob

def load_modules(loc):
    """Loads each directory in given path as a Python module and then yields it"""
    loc = path.dirname(path.realpath(loc)) 
    
    for module_path in glob(path.join(loc, "*")):
        if path.isdir(module_path):
            module_name = path.basename(module_path)

            if module_name != "__pycache__":
                yield importlib.import_module(module_name)
