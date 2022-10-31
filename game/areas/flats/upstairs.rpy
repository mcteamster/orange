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
