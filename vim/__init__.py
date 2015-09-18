
import dotfiles
import sh

from pathlib import Path
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

    # This function is called when dotfiles are installed
    def install(self):
        yield self.install_vundle()

    def post_install(self):
        yield self.install_plugins()

    def install_vundle(self):
        vundle_dest = Path(path.expanduser("~/.vim/bundle/Vundle.vim"))

        if not vundle_dest.exists():
            git.clone("https://github.com/VundleVim/Vundle.vim.git", str(vundle_dest))
            return "Vundle has been downloaded successfully"
        else:
            git("-C", str(vundle_dest), "pull")
            return "Vundle was already installed, it has been updated"

    def install_plugins(self):
        vim("+PluginInstall", "+qall")
        return "Vim has installed all plugins"
