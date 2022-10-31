label police_east:
    # Screens
    screen interact_police_east():
        frame:
            pos (0.0, 0.8)
            textbutton "police_west":
                xysize (1.0, 0.2)
                action [
                    Jump("police_west")
                ]
        frame:
            pos (0.1, 0.25)
            textbutton "station":
                xysize (0.15, 0.6)
                action [
                    Jump("station")
                ]
        frame:
            pos (0.43, 0.47)
            textbutton "corner_store_east":
                xysize (0.12, 0.08)
                action [
                    Jump("corner_store_east")
                ]
        frame:
            pos (0.6, 0.37)
            textbutton "downtown":
                xysize (0.14, 0.35)
                action [
                    Jump("downtown")
                ]
        frame:
            pos (0.68, 0.43)
            textbutton "tavern":
                xysize (0.03, 0.16)
                action [
                    Jump("tavern")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.41, 0.46)
                textbutton "corner_store":
                    xysize (0.01, 0.12)
                    action [
                        Jump("corner_store")
                    ]

    # Script
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_police_east_eve
    else:
        scene bg street_police_east
    with fade
    call screen interact_police_east

label police_west:
    # Screens
    screen interact_police_west():
        frame:
            pos (0.15, 0.8)
            textbutton "police_east":
                xysize (0.85, 0.2)
                if (progress["night"] or inventory["key"]["active"]):
                    action [
                        Jump("downtown")
                    ]
                else:
                    action [
                        Jump("police_east")
                    ]
        frame:
            pos (0.0, 0)
            textbutton "downtown":
                xysize (0.15, 1.0)
                action [
                    Jump("downtown")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.43, 0.43)
                textbutton "bank_north":
                    xysize (0.21, 0.19)
                    action [
                        Jump("bank_north")
                    ]
        frame:
            pos (0.75, 0.26)
            textbutton "station":
                xysize (0.15, 0.55)
                action [
                    Jump("station")
                ]

    # Sprites
    image bg street_police_west_night:
        "bg street_police_west_night_1.png"
        pause 0.25
        "bg street_police_west_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_police_west_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_police_west_eve
    else:
        scene bg street_police_west
    with fade
    call screen interact_police_west