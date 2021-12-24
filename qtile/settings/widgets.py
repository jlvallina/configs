from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
            text='\uE0B2',
            padding=0,
            fontsize=37,
            **base(fg, bg)
    )

def double_powerline(fg="light", bg="dark"):
    return [powerline('dark', fg), powerline(bg, 'dark')]

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='line',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),
    icon(bg="color4", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates} ',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    *double_powerline('color4', 'color3'),
    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.Wlan(
        **base(bg='color3'),
        padding=10,
        format='{essid} {percent:2.0%}',
        interface='wlp1s0'
    ),

    *double_powerline('color3', 'color2'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'), padding=5),

    *double_powerline('color2', 'color1'),
    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    *double_powerline('color1', 'color0'),
    icon(bg="color0", fontsize=17, text=' '),
    widget.PulseVolume(
        background=colors['color0'],
        fmt='{} ',
        padding=10,
        volume_app='pavucontrol'
    ),

    *double_powerline('color0', 'color3'),
    icon(bg="color3", fontsize=17, text=' '),
    widget.Battery(
        background=colors['color3'],
        padding=10,
        format='{char} {percent:2.0%} {watt:.2f} W'
    ),


    powerline('dark', 'color3'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
