default progress = {
    "awake": False,
    "bus_ticket": False,
    "cheats": False,
    "evening": False,
    "help": {
        "page": "map",
        "hints": {
            "hint_1": False,
            "hint_2": False,
            "hint_3": False,
            "hint_4": False,
            "hint_5": False,
        }
    },
    "lives": 1,
    "minigames": {
        "land_mines": {
            "highscore": 999,
            "remaining": 81,
            "tripped": False,
            "victory": False,
        },
        "ninja_assassin": {
            "attempts": 0,
            "complete": False,
        },
    },
    "night": False,
    "quests": {
        "clowns": {
            "disabled": False,
            "offered": False,
            "accepted": False,
            "complete": False,
        },
        "ninjas": {
            "disabled": False,
            "offered": False,
            "accepted": False,
            "complete": False,
        },
        "mermaids": {
            "disabled": False,
            "offered": False,
            "accepted": False,
            "complete": False,
        },
        "pirates": {
            "disabled": False,
            "offered": False,
            "accepted": False,
            "complete": False,
        },
        "police": {
            "disabled": False,
            "offered": False,
            "accepted": False,
            "complete": False,
        }
    },
    "zombies": {
        "clear": [],
    }
}

# Track State
init python:
    def label_callback(name, abnormal):
        ignored_labels = ["_after_load", "_start", "_quit", "_splashscreen", "_before_main_menu", "_main_menu", "_after_warp", "_hide_windows", "help"]

        if not name in ignored_labels:
            if not name.startswith("help."):
                store.current_label = name

    config.label_callback = label_callback