
import dotfiles

class I3(dotfiles.Module):
    default_dest = "~/.i3"

    overriden_dests = {
        "sandstone_background.jpg": "~/backgrounds/Sandstone.jpg"  
    }
