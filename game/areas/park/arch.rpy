label arch_northwest:
    # Screens
    screen interact_arch_northwest():
        frame:
            pos (0, 0.8)
            textbutton "fork_southeast":
                xysize (0.7, 0.20)
                action [
                    Jump("fork_southeast")
                ]
        frame:
            pos (0.4, 0.1)
            textbutton "chinatown_west":
                xysize (0.17, 0.38)
                action [
                    Jump("chinatown_west")
                ]
        frame:
            pos (0.8, 0.6)
            textbutton "bridge_southeast":
                xysize (0.2, 0.4)
                action [
                    Jump("bridge_southeast")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_arch_northwest_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_arch_northwest_eve
    else:
        scene bg park_arch_northwest
    with fade
    call screen interact_arch_northwest

label arch_southwest:
    # Screens
    screen interact_arch_southwest():
        frame:
            pos (0.4, 0.8)
            textbutton "bridge_southeast":
                xysize (0.6, 0.20)
                action [
                    Jump("bridge_southeast")
                ]
        frame:
            pos (0.4, 0.1)
            textbutton "chinatown_west":
                xysize (0.17, 0.38)
                action [
                    Jump("chinatown_west")
                ]
        frame:
            pos (0, 0.55)
            textbutton "fork_southeast":
                xysize (0.2, 0.45)
                action [
                    Jump("fork_southeast")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_arch_southwest_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_arch_southwest_eve
    else:
        scene bg park_arch_southwest
    with fade
    call screen interact_arch_southwest

label arch_east:
    screen interact_arch_east():
        frame:
            pos (0.0, 0.8)
            textbutton "chinatown_west":
                xysize (1.0, 0.20)
                action [
                    Jump("chinatown_west")
                ]
        frame:
            pos (0.24, 0.2)
            textbutton "bridge_southeast":
                xysize (0.2, 0.38)
                action [
                    Jump("bridge_southeast")
                ]
        frame:
            pos (0.56, 0.2)
            textbutton "fork_southeast":
                xysize (0.2, 0.38)
                action [
                    Jump("fork_southeast")
                ]

    scene bg park_arch_east with fade
    call screen interact_arch_east