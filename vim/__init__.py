
# By default, files are copied here
dest = "~/.vim"

# You can set some files to be placed and renamed into other locations explictly
exceptions = {
    "vimrc": "~/.vimrc",
}

# This function is called when dotfiles are installed (but not when updated)
def install():
    print("VIM!!")
