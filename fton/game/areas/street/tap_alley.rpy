label tap_alley:
    # Screens
    screen interact_tap_alley():
        frame:
            pos (0.13, 0.15)
            textbutton "storeroom":
                xysize (0.15, 0.55)
                action [
                    Jump("storeroom")
                ]
        frame:
            pos (0.9, 0)
            textbutton "corner_store_north":
                xysize (0.1, 1.0)
                action [
                    Jump("corner_store_north")
                ]

    # Sprites
    image bg street_tap_alley_night:
        "bg street_tap_alley_night_1.png"
        pause 0.25
        "bg street_tap_alley_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_tap_alley_night
    else:
        scene bg street_tap_alley
    with fade
    call screen interact_tap_alley
