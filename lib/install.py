#!/usr/bin/env python3

import dotfiles
import util
import shutil
import os

from pathlib import Path

util.initialize(Path(__file__).parent)

modules = dotfiles.Module.__subclasses__()
for i, module in enumerate(modules):
    progress = "({} out of {})".format(i + 1, len(modules))

    module_name = util.color(module.__name__, util.Color.green)
    module_source = util.color(module.__module__, util.Color.yellow)

    print("Installing module", module_name, "from", module_source, progress)
    instance = module()

    for message in instance.install():
        print(util.timestamp(message)) 

    print("Copying over files from module", module_name)

    default_path = Path(os.path.expanduser(module.default_dest))
    module_path = Path(module.__module__)
    valid_file_paths = [path for path in module_path.glob("*") if util.validate_path(path)]

    for path in valid_file_paths:
        dest_path = default_path
        new_dest = module.overriden_dests.get(path.name)
        
        if new_dest is not None:
            new_path = Path(os.path.expanduser(new_dest))

            if new_path.is_absolute():
                dest_path = Path(os.path.expanduser(str(new_path)))
            else:
                dest_path /= new_path
        else:
            dest_path /= path.name
   
        abs_path = str(path.absolute())
        abs_dest = str(dest_path.absolute())

        os.makedirs(str(dest_path.parent), exist_ok=True)

        if dest_path.exists():
            print(util.timestamp("File " + abs_dest + " already exists.  Overwriting"))
            os.remove(abs_dest)
  
        shutil.os.symlink(abs_path, abs_dest)

    print("Finalizing installation in module", module_name)

    for message in instance.post_install():
        print(util.timestamp(message))

