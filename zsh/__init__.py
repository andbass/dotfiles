
import dotfiles
import os
import sys

class Zsh(dotfiles.Module):
    overriden_dests = {
        "zshrc": "~/.zshrc",
        "glen-magic.zsh-theme": "~/.oh-my-zsh/custom/themes/glen-magic.zsh-theme"
    }

    def install(self):
        dotfiles.process('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
        yield "ZSH installed"

        os.makedirs(os.path.expanduser("~/projects"), exist_ok=True)
        yield "Created projects folder"
