
import dotfiles
import sh

from sh import git, vim
from os import path

class Vim(dotfiles.Module):
    # By default, files are copied here 
    # ("dest" is short for destination)
    default_dest = "~/.vim"

    # You can set some files to be placed into other locations explictily and/or renamed
    # The path provided, if not absolute, is relative to the "default_dest"
    overriden_dests = {
        "vimrc": "~/.vimrc",
    }

    # This function is called when dotfiles are installed (but not when updated)
    def install(self):
        try:
            yield self.install_vundle()
        except sh.ErrorReturnCode_128 as err:
            if "already exists and is not an empty directory" in str(err.stderr): 
                yield "Vundle has already been installed"
            else:
                raise err

    def post_install(self):
        yield self.install_plugins()

    def install_vundle(self):
        git.clone("https://github.com/VundleVim/Vundle.vim.git", 
                  path.expanduser("~/.vim/bundle/Vundle.vim"))

        return "Vundle has been downloaded successfully"

    def install_plugins(self):
        vim("+PluginInstall", "+qall")
        return "Vim has installed all plugins"
