
import importlib
import sys
import time

from enum import Enum
from pathlib import Path

def initialize(loc):
    prepare_path(loc)
    load_modules(loc)

    # Automate the installation of SH if it isn't installed
    try:
        import sh
    except ImportError:
        import pip
        pip.main(["install", "sh"])


def prepare_path(loc):
    """Appends the "dotfiles.py" file to the search path"""
    dotfiles_path = loc / "dotfiles.py"
    sys.path.append(str(dotfiles_path))
    sys.path.append(str(dotfiles_path.parent / ".."))

def load_modules(loc):
    """Loads each directory in given path as a Python module"""
    paths = [path for path in loc.parent.glob("*") if not path.match(".*")]

    for module_path in paths:
        if module_path.is_dir():
            module_name = module_path.name
            if module_name != "__pycache__" and module_name != loc.parent:
                importlib.import_module(module_name)

def timestamp(message):
    return "  [{}] {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), message)

def validate_path(path):
    return not path.match(".*") and path.name != "__pycache__" and path.name != "__init__.py"

class Color(Enum):
    red = 1
    blue = 4
    green = 2
    yellow = 3

def color(text, col, bold=True):
    colored_text = "\033[9" + str(col.value) + "m" + text + "\033[0m"

    if bold:
        colored_text = "\033[1m" + colored_text

    return colored_text
