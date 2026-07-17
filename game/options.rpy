## GIVEN project configuration.
## See https://www.renpy.org/doc/html/options.html for supported options.

define config.name = "GIVEN"
define config.version = "0.1.0"
define build.name = "given"

define gui.about = _p("""
GIVEN is a Ren'Py visual novel project.
""")

define config.save_directory = "given-0.1.0"
define config.window_title = "GIVEN"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
