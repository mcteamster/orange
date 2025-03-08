label cliefwood:
    # Settings
    $ inventory["key"]["highlight"] = False

    # Screens
    screen interact_cliefwood():
        frame:
            pos (0.0, 0.8)
            textbutton "junction":
                xysize (1.0, 0.2)
                action [
                    Jump("junction")
                ]
        frame:
            pos (0.69, 0.52)
            textbutton "locked_house":
                xysize (0.03, 0.24)
                action [
                    Jump("cliefwood.locked_house")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.22, 0.5)
                textbutton "pats_house":
                    xysize (0.035, 0.23)
                    action [
                        Jump("pats_house")
                    ]
            frame:
                pos (0.46, 0.51)
                textbutton "empty_house":
                    xysize (0.035, 0.125)
                    action [
                        Jump("empty_house")
                    ]
            frame:
                pos (0.045, 0.815)
                textbutton "sign":
                    xysize (0.23, 0.07)
                    action [
                        Jump("cliefwood.sign")
                    ]

    # Sprites
    image bg street_cliefwood_night:
        "bg street_cliefwood_night_1.png"
        pause 0.25
        "bg street_cliefwood_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_cliefwood_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_cliefwood_eve
    else:
        scene bg street_cliefwood
    with fade
    call screen interact_cliefwood

    label .sign:
        "Wow. Cliefwood got gentrified.{w=2}{nw}"
        call screen interact_cliefwood

    label .locked_house:
        # Settings
        $ inventory["key"]["highlight"] = True

        # Screens
        screen interact_cliefwood_locked_house():
            frame:
                pos (0.0, 0.8)
                textbutton "cliefwood":
                    xysize (1.0, 0.2)
                    action [
                        Jump("cliefwood")
                    ]

        # Script
        if (progress["night"] or inventory["key"]["active"]):
            scene bg street_cliefwoods_door_night
            call screen interact_cliefwood_locked_house
        else:
            "Locked.{w=2}{nw}"
            call screen interact_cliefwood

    label .unlocked:
        # Settings
        $ inventory["key"]["active"] = False
        $ inventory["key"]["highlight"] = False

        # Screens
        screen interact_cliefwood_unlocked_house():
            frame:
                pos (0.38, 0.21)
                textbutton "cliefwoods_house":
                    xysize (0.24, 0.7)
                    action [
                        Jump("cliefwoods_house")
                    ]

        # Script
        scene bg street_cliefwoods_door_open_night
        call screen interact_cliefwood_unlocked_house