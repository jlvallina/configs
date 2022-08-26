# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys
from libqtile.dgroups import simple_key_binder


groups = [Group("", layout='max'),
          Group("", layout='monawide'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='max'),
          Group("", layout='floating')]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

keys.extend([
    Key([mod], "Home", lazy.screen.next_group()),
    Key([mod], "End", lazy.screen.prev_group()),
])


