## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Find the Orange Narwhal")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

#define gui.show_name = True
define gui.show_name = False


## The version of the game.

define config.version = "4.0.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
------------------------

Find the Orange Narwhal is a wild teenage fever dream jammed into a point-and-click adventure.

Earler versions of this game were made in PowerPoint, pushing the limits of what was possible.
Unfortunately, computers back then weren't powerful enough to handle 4606 slides of action-packed interactive content.

Our raging ambition has since faded and the time has come to share this masterpiece with a wider audience.

Click, click, click! Walk around town and uncover the mystery of what happened to the Orange Narwhal!

Honestly this game doesn't make much sense - we just hope you enjoy figuring it out as much as we enjoyed making it.

------------------------

Ohnomer | 2022

Story and Graphics by Andrew W.

Programming and Production by {a=https://games.tonz.io}Tony Z.{/a}

Music from the Public Domain:\n
- {a=https://www.chosic.com/download-audio/25966/}Mozart: Symphony No. 40 in G Minor, K. 550 – I. Molto Allegro{/a} by Musopen Symphony

Sound effects mixed from {a=https://soundbible.com}soundbible.com{/a} under {a=https://creativecommons.org/licenses/by/3.0/}Creative Commons Attribution 3.0{/a} license:\n
- {a=https://soundbible.com/1571-Fishtank-Bubbles-2.html}Bubbles{/a} by amanda\n
- {a=https://soundbible.com/1911-Mandatory-Evacuation.html}Alarm{/a} by Brandon\n
- {a=https://soundbible.com/1757-Car-Brake-Crash.html}Skid{/a} by Cam Martinez\n
- {a=https://soundbible.com/2209-Muscle-Car.html}Bus{/a},
{a=https://soundbible.com/2201-Large-Waterfall.html}Water Rush{/a} by Daniel Simion\n
- {a=https://soundbible.com/2062-Metal-Gong-1.html}Bell{/a} by Dianakc\n
- {a=https://soundbible.com/2068-Woosh.html}Whoosh{/a} by Mark DiAngelo\n
- {a=https://soundbible.com/1529-Dog-Bite.html}Bite{/a},
{a=https://soundbible.com/2114-Flush-Toilet--2.html}Drain{/a},
{a=https://soundbible.com/538-Blast.html}Explosion{/a},
{a=https://soundbible.com/105-Light-Bulb-Breaking.html}Glass{/a},
{a=https://soundbible.com/1271-Harpoon.html}Harpoon{/a},
{a=https://soundbible.com/1894-Helicopter-Hovering.html}Helicopter{/a},
{a=https://soundbible.com/1522-Balloon-Popping.html}Pop{/a},
{a=https://soundbible.com/1201-Automatic-Machine-Gun-3x.html}Rifle{/a},
{a=https://soundbible.com/1611-TV-Static.html}Static{/a},
{a=https://soundbible.com/1008-Decapitation.html}Sword{/a},
{a=https://soundbible.com/2115-Pouring-Drink.html}Water Rising{/a} by Mike Koenig\n
- {a=https://soundbible.com/1996-Shotgun-Reload-Old.html}Reload{/a},
{a=https://soundbible.com/2095-Mossberg-500-Pump-Shotgun.html}Shotgun{/a} by RA The Sun God\n
- {a=https://soundbible.com/2021-Atchisson-Assault-Shotgun.html}Sawnoff{/a} by Soundeffects\n
- {a=https://soundbible.com/1987-Rockslide-Small.html}Crash{/a} by Sound Explorer
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "fton"

## Keymap ######################################################################
init:
    $ config.keymap["rollback"] = []
    $ config.keymap["hide_windows"] = []
    $ config.keymap["launch_editor"] = []
    $ config.keymap["inspector"] = []
    $ config.keymap["full_inspector"] = []
    $ config.keymap["developer"] = []
    $ config.keymap["help"] = []
    $ config.keymap["choose_renderer"] = []
    $ config.keymap["progress_screen"] = []
    $ config.keymap["rollforward"] = []
    $ config.keymap["dismiss"] = ["mouseup_1"]
    $ config.keymap["focus_left"] = []
    $ config.keymap["focus_right"] = []
    $ config.keymap["focus_up"] = []
    $ config.keymap["focus_down"] = []
    $ config.keymap["skip"] = []
    $ config.keymap["toggle_skip"] = []
    $ config.keymap["fast_skip"] = []
    $ config.keymap["director"] = []
    # DISABLED IN PRODUCTION
    $ config.keymap["console"] = []
    $ config.keymap["console_older"] = []
    $ config.keymap["console_newer"] = []
    $ config.keymap["performance"] = []
    $ config.keymap["image_load_log"] = []

## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/music/molto_allegro.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

#default preferences.text_cps = 0
default preferences.text_cps = 100


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "fton-1663821038"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"