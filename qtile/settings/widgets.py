from libqtile import widget
from .theme import colors
import os
import socket
from libqtile import qtile
from libqtile.log_utils import logger

l_arrow = ""
r_arrow = ""

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())



class MyPulse(widget.PulseVolume):

    def _update_drawer(self):
        if self.volume <= 0:
            self.text = "婢"
        elif self.volume <= 25:
            self.text = "ﱜ"
        elif self.volume <= 50:
            self.text = "奔"
        elif self.volume <= 75:
            self.text = "墳"
        elif self.volume > 99:
            self.text = "ﱛ"


for color in colors:
    logger.warning(f"color: {color}: {colors[color]}")

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="UbuntuMono Nerd Font Mono",
    fontsize=12,
    padding=2,
    background=colors["dark"],
    foreground=colors["text"],
)
extension_defaults = widget_defaults.copy()


primary_widgets = [
    widget.Sep(
        linewidth=0,
        padding=10,
        fontsize=20,
    ),
    widget.TextBox(
        text='',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
        foreground=colors.get("iconn", "#1793d1"),
        padding=2,
        fontsize=40,
    ),
    widget.Sep(
        linewidth=0,
        padding=10,
        fontsize=20,
    ),
    widget.TextBox(
        text=r_arrow,
        background=colors["grey"],
        foreground=colors["dark"],
        padding=0,
        fontsize=30,
    ),
    widget.Sep(
        linewidth=0,
        padding=8,
        background=colors["grey"]
    ),
    widget.GroupBox(
        fontsize=30,
        margin_y=3,
        margin_x=0,
        padding_y=5,
        padding_x=5,
        borderwidth=1,
        active=colors["active"],
        inactive=colors["inactive"],
        highlight_color=colors["light"],
        this_current_screen_border=colors["focus"],
        this_screen_border=colors.get("debug", "#7FFF00"),
        other_current_screen_border=colors.get("debug", "#7FFF00"),
        other_screen_border=colors.get("debug", "#7FFF00"),
        foreground=colors.get("debug", "#7FFF00"),
        background=colors["grey"],
        rounded=False,
        highlight_method="line"
    ),
    widget.TextBox(
        text=r_arrow,
        background=colors["light"],
        foreground=colors["grey"],
        padding=0,
        fontsize=30,
    ),
    widget.CurrentLayout(
        fmt=' {}',
        foreground=colors["focus"],
        background=colors["light"],
        padding=5
    ),
    widget.TextBox(
        text="",
        background=colors["light"],
        foreground=colors["focus"],
        padding=0,
        fontsize=20,
    ),
    widget.WindowName(
        foreground=colors["focus"],
        background=colors["light"],
        padding=8,
        max_chars=40,
        width=300
    ),
    widget.Sep(
        linewidth=0,
        padding=0,
        foreground=colors["light"],
        background=colors["light"]
    ),
    widget.TextBox(
        text='',
        background=colors["dark"],
        foreground=colors["light"],
        padding=0,
        fontsize=37
    ),
    widget.Spacer(
        background=colors["dark"]
    ),
    widget.Sep(
        linewidth=0,
        padding=6,
        foreground=colors["dark"],
        background=colors["dark"]
    ),
    widget.TextBox(
        text='',
        background=colors["dark"],
        foreground=colors["grey"],
        padding=0,
        fontsize=37
    ),
    widget.Wlan(
        background=colors["grey"],
        foreground=colors["text"],
        format='{essid} {percent:2.0%}',
        interface='wlp1s0',
        padding=5
    ),
    widget.TextBox(
       text="",
       background=colors["grey"],
       foreground=colors["text"],
       padding=5,
       fontsize=20,
   ),
   MyPulse(
        background=colors["grey"],
        foreground=colors["text"],
        emoji = True,
        limit_max_volume=True,
        fmt='{}',
        volume_app='pavucontrol',
        fontsize=30,
        step=25,
        padding=5
    ),
    widget.TextBox(
       text="",
       background=colors["grey"],
       foreground=colors["text"],
       padding=5,
       fontsize=20,
   ),
    widget.TextBox(
       text="",
       background=colors["grey"],
       foreground=colors["text"],
       padding=5,
       fontsize=20,
   ),
    widget.Clock(
        foreground=colors["text"],
        background=colors["grey"],
        format='%d-%m-%Y',
        timezone='America/Lima'
    ),
    widget.TextBox(
       text="",
       background=colors["grey"],
       foreground=colors["text"],
       padding=5,
       fontsize=20,
   ),
    widget.Clock(
        foreground=colors["text"],
        background=colors["grey"],
        format='L: %H:%M',
        timezone='America/Lima',
        padding=5
    ),
    widget.Clock(
        foreground=colors["text"],
        background=colors["grey"],
        format='M: %H:%M',
        timezone='Europe/Madrid',
        padding=5
    ),
    ### Notis
    widget.TextBox(
        text=l_arrow,
        foreground=colors["color1"],
        background=colors["grey"],
        padding=0,
        fontsize=30
    ),
    widget.TextBox(
       text="ﮮ",
       background=colors["color1"],
       foreground=colors["focus"],
       padding=5,
       fontsize=20,
   ),
    widget.CheckUpdates(
        foreground=colors["focus"],
        background=colors["color1"],
        no_update_string='',
        display_format='{updates}',
        update_interval=1800,
        padding=2,
        custom_command='checkupdates',
        execute='terminator -e "sudo pacman -Syu && yay" -p hold'
    ),
    widget.TextBox(
       text="",
       background=colors["color1"],
       foreground=colors["focus"],
       padding=5,
       fontsize=20,
   ),
    widget.TextBox(
       text="",
       background=colors["color1"],
       foreground=colors["inactive"],
       padding=5,
       fontsize=20,
   ),
    widget.Battery(
        foreground=colors["focus"],
        background=colors["color1"],
        format='{percent:2.0%} ',
        hide_threshold=30,
        padding=2
    ),
    widget.TextBox(
        text=l_arrow,
        background=colors["color1"],
        foreground=colors["dark"],
        padding=0,
        fontsize=30
    ),
    widget.Systray(
        foreground=colors["dark"],
        background=colors["dark"],
        padding=2
    )
]


secondary_widgets = [

]
