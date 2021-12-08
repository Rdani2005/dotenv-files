# Libraries
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from .keys import mod

def UsingMouseLayouts():
    mouse_list = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
            start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
            start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]
    return mouse_list

mouse = UsingMouseLayouts()