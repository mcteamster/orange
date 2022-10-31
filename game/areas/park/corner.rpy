label corner_east:
    # Screens
    screen interact_corner_east():
        frame:
            pos (0, 0.8)
            textbutton "fork_north":
                xysize (1.0, 0.20)
                action [
                    Jump("fork_north")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0, 0.38)
                textbutton "tee_north":
                    xysize (0.25, 0.3)
                    action [
                        Jump("tee_north")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_corner_east_night
    else:
        scene bg park_corner_east
    with fade
    call screen interact_corner_east

label corner_south:
    # Screens
    screen interact_corner_south():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0, 0.8)
                textbutton "tee_north":
                    xysize (1.0, 0.20)
                    action [
                        Jump("tee_north")
                    ]
        frame:
            pos (0.75, 0.3)
            textbutton "fork_north":
                xysize (0.25, 0.4)
                action [
                    Jump("fork_north")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_corner_south_night
    else:
        scene bg park_corner_south
    with fade
    call screen interact_corner_south