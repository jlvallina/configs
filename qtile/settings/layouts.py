# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from .theme import colors


layout_conf = {
    "border_width": 4,
    "margin": 8,
    "border_focus": colors.get("border_focus", "#7FFF00"),
    "border_normal": colors.get("inactive", "#7FFF00")
}

layouts = [
    layout.MonadTall(
        single_border_width=4,
        single_margin=1,
        **layout_conf
    ),
    layout.MonadWide(
        single_border_width=4,
        single_margin=1,
        **layout_conf
    ),
    layout.Max(**layout_conf),
    layout.Floating(**layout_conf),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
        Match(title='Find/Replace'),
    ],
    border_focus=colors.get("urgent", "#7FFF00")
)
