label apartment:
    # Screens
    screen interact_apartment():
        frame:
            pos (0.315, 0.22)
            textbutton "hallway":
                xysize (0.085, 0.30)
                action [
                    SetDict(progress, "awake", True),
                    Jump("hallway")
                ]
        if (progress["night"] or inventory["key"]["active"]) and (inventory["shotgun"]["active"] == False):
            frame:
                pos (0.83, 0.08)
                textbutton "jump_window":
                    xysize (0.17, 0.6)
                    action [
                        Jump("corner_south")
                    ]
        else:
            frame:
                pos (0.885, 0.18)
                textbutton "look_window":
                    xysize (0.07, 0.30)
                    action [
                        Call("apartment.look")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]) and (inventory["shotgun"]["active"] == False):
        scene bg flats_apartment_night
    else:
        scene bg flats_apartment
    with fade

    if progress["awake"] == False:
        "What did we do with that narwhal? I don't remember a thing from last night!"
        show hint_paper
        show tutorial_interact:
            zoom 0.75
            align (0.5, 0.5)
            pos (0.5, 0.48)
        "{i}Click on people and things to interact and move.{/i}"
        hide tutorial_interact
        show tutorial_reverse:
            zoom 0.67
            align (0.5, 0.5)
            pos (0.5, 0.48)
        "{i}Click the edges of the screen to turn around/reverse.{/i}"
        hide tutorial_reverse
        show tutorial_inventory:
            zoom 0.67
            align (0.5, 0.5)
            pos (0.5, 0.48)
        "{i}Click highlighted items in your inventory to use them.{/i}"
        hide tutorial_inventory
        show tutorial_help:
            zoom 0.8
            align (0.5, 0.5)
            pos (0.5, 0.48)
        "{i}When in doubt, click the help (?) button, or just click everything!{/i}"
        hide tutorial_help
        hide hint_paper
    call screen interact_apartment

    label .look:
        "Man, I've got sweet views of the park{w=2}{nw}"
        call screen interact_apartment

label hallway:
    # Screens
    screen interact_hallway():
        frame:
            pos (0.625, 0.08)
            textbutton "apartment":
                xysize (0.05, 0.55)
                action [
                    Jump("apartment")
                ]
        frame:
            pos (0.07, 0.05)
            textbutton "lobby":
                xysize (0.2, 0.66)
                action [
                    Jump("lobby")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg flats_hallway_night
    else:
        scene bg flats_hallway
    with fade
    call screen interact_hallway
