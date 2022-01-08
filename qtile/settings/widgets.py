from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg],
    }


def separator(fg='light', bg='dark'):
    return widget.Sep(
        **base(fg=fg, bg=bg),
        linewidth=1, 
        padding=5
    )


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
        separator(fg='text', bg='dark'),
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
        separator(fg='active'),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    # powerline('color4', 'dark'),
    # icon(bg="color4", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        **base(fg='light', bg='dark'),
        colour_have_updates=colors['color4'],
        colour_no_updates=colors['active'],
        no_update_string='',
        display_format='  {updates}',
        update_interval=1800,
        padding=10,
        custom_command='checkupdates',
        execute='terminator -e "sudo pacman -Syu && yay" -p hold'
    ),

    # *double_powerline('color4', 'color3'),
    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.Wlan(
        **base(fg='light', bg='dark'),
        padding=10,
        format='  {essid} {percent:2.0%}',
        interface='wlp1s0'
    ),

    # *double_powerline('color3', 'color2'),
    widget.CurrentLayoutIcon(
        **base(fg='light', bg='dark'),
        scale=0.65
    ),
    widget.CurrentLayout(
        **base(fg='light', bg='dark'),
        padding=10
    ),

    # *double_powerline('color2', 'color1'),
    # icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(
        **base(fg='light', bg='dark'),
        format='   %d/%m/%Y   %H:%M',
        timezone='America/Lima'
    ),
    widget.Clock(
        **base(fg='light', bg='dark'),
        format=' / %H:%M',
        timezone='Europe/Madrid'
    ),


    # *double_powerline('color1', 'color0'),
    # icon(bg="color0", fontsize=17, text=' '),
    widget.PulseVolume(
        **base(fg='light', bg='dark'),
        emoji = False,
        fmt='   {}',
        step=10,
        padding=10,
        volume_app='pavucontrol'
    ),

    # *double_powerline('color0', 'color3'),
    # icon(bg="color3", fontsize=17, text=' '),
    widget.Battery(
        **base(fg='light', bg='dark'),
        padding=10,
        format='  {char} {percent:2.0%} {watt:.2f} W'
    ),



    # powerline('dark', 'color3'),

    widget.Systray(
        background=colors['dark'],
        padding=10
    ),

    separator(),
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
