label bend_southwest:
    # Screens
    screen interact_bend_southwest():
        frame:
            pos (0, 0.8)
            textbutton "gazebo_northeast":
                xysize (1.0, 0.20)
                action [
                    Jump("gazebo_northeast")
                ]
        frame:
            pos (0.75, 0.35)
            textbutton "fork_west":
                xysize (0.25, 0.3)
                action [
                    Jump("fork_west")
                ]

    # Script
    scene bg park_bend_southwest with fade
    call screen interact_bend_southwest

label bend_east:
    # Screens
    screen interact_bend_east():
        frame:
            pos (0, 0.8)
            textbutton "fork_west":
                xysize (1.0, 0.20)
                action [
                    Jump("fork_west")
                ]
        frame:
            pos (0, 0.35)
            textbutton "gazebo_northeast":
                xysize (0.2, 0.25)
                action [
                    Jump("gazebo_northeast")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_bend_east_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_bend_east_eve
    else:
        scene bg park_bend_east
    with fade
    call screen interact_bend_east