# Dotfiles
Here's my personal dotfile configuration.  It's designed to be very easy to extend and modify.

In essence, each directory is a Python module (with excpetion to the "lib" folder).
Each module defines a class that extends from `dotfiles.Module`, and optionally overrides the `install` and `post_install` methods.

To add a module, just make a new directory and add your `__init__.py` file that defines a class that subclasses `dotfiles.Module`.  Insert any relevants files to that module (config files, settings, etc) inside the directory.

Two class level variables, `default_dest` and `overriden_dests`, are used to determine where the files within the module are to be symlinked.
`install` is called before files are copied over, whereas `post_install` is called after the `install` method is executed and all of the module's files are copied.

By default, files are copied into `default_dest`.  You can change the output directory and/or name of certain files by adding them to the `overriden_dests` dictionary.

Take a look around at "vim" folder to get a general idea of how things work.
