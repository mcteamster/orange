label corner_store_north:
    # Settings
    if "corner_store" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_corner_store_north():
        frame:
            pos (0.0, 0)
            textbutton "corner_store_west":
                xysize (0.15, 1.0)
                action [
                    Hide("zombies_corner_store_north"),
                    Jump("corner_store_west")
                ]
        frame:
            pos (0.37, 0.4)
            textbutton "sentinel_alley":
                xysize (0.05, 0.2)
                action [
                    Hide("zombies_corner_store_north"),
                    Jump("sentinel_alley")
                ]
        frame:
            pos (0.58, 0.40)
            textbutton "dock":
                xysize (0.06, 0.2)
                action [
                    Hide("zombies_corner_store_north"),
                    Jump("dock")
                ]

    screen zombies_corner_store_north_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("corner_store_north.clear")
                ]
            else:
                action NullAction()
        timer 10:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("corner_store_north.ambushed")
                ]

    screen zombies_corner_store_north():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.45, 0.42)
            alpha True
            if zombies["z2"] > 0:
                hotspot (0, 0, 200, 100):
                    action [
                        Call(shoot_command, "zombies", "z2", zombies, damage=2, from_current=True),
                    ]
                hotspot (0, 100, 200, 1000):
                    ypos 100
                    action [
                        Call(shoot_command, "zombies", "z2", zombies, from_current=True),
                    ]
                if zombies["z2"] == 2:
                    ground "zombie_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_b half"
            else: 
                ground "zombie_b dead"
        imagemap:
            pos (0.25, 0.4)
            alpha True
            if zombies["z1"] > 0:
                hotspot (0, 0, 200, 100):
                    action [
                        Call(shoot_command, "zombies", "z1", zombies, damage=2, from_current=True),
                    ]
                hotspot (0, 100, 200, 1000):
                    ypos 100
                    action [
                        Call(shoot_command, "zombies", "z1", zombies, from_current=True),
                    ]
                if zombies["z1"] == 2:
                    ground "zombie_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_a half"
            else: 
                ground "zombie_a dead"
        imagemap:
            pos (0.53, 0.35)
            alpha True
            if zombies["z3"] > 0:
                hotspot (0, 0, 200, 100):
                    action [
                        Call(shoot_command, "zombies", "z3", zombies, damage=2, from_current=True),
                    ]
                hotspot (0, 100, 200, 1000):
                    ypos 100
                    action [
                        Call(shoot_command, "zombies", "z3", zombies, from_current=True),
                    ]
                if zombies["z3"] == 2:
                    ground "zombie_c full"
                elif zombies["z3"] == 1:
                    ground "zombie_c half"
            else: 
                ground "zombie_c dead"

    # Sprites
    image bg street_corner_store_north_night:
        "bg street_corner_store_north_night_1.png"
        pause 0.25
        "bg street_corner_store_north_night_2.png"
        pause 0.25
        repeat

    image bg street_corner_store_north_night_z:
        "bg street_corner_store_north_night_z_1.png"
        pause 0.25
        "bg street_corner_store_north_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "corner_store" not in progress["zombies"]["clear"]:
            scene bg street_corner_store_north_night_z
            show screen zombies_corner_store_north_timer
            show screen zombies_corner_store_north
            with fade
            if active_weapon == "shotgun":
                show shotgun equip onlayer screens zorder 50
                if inventory["sawnoff"]["active"]:
                    if zombies["z1"] == 2:
                        $ zombies["z1"] = 1
                        $ zombies["total"] -= 1
                        play audio "audio/sawnoff.wav"
                    pause 0.25
                    if zombies["z1"] == 1:
                        $ zombies["z1"] = 0
                        $ zombies["total"] -= 1
                        play audio "audio/sawnoff.wav"
            else:
                show sawnoff equip onlayer screens zorder 50
            pause
        else:
            scene bg street_corner_store_north_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_corner_store_north_eve
    else:
        scene bg street_corner_store_north
    with fade
    call screen interact_corner_store_north

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_corner_store_north_timer
        hide screen zombies_corner_store_north
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("corner_store")
        hide screen zombies_corner_store_north_timer
        if active_weapon == "shotgun":
            show shotgun unequip onlayer screens zorder 50
            pause 0.5
            hide shotgun onlayer screens
            hide shotgun_flash onlayer screens
            hide screen pumping
        else:
            show sawnoff unequip onlayer screens zorder 50
            pause 0.5
            hide sawnoff onlayer screens
            hide sawnoff_flash onlayer screens
            $ inventory["sawnoff"]["ammo"] = 2
        call screen interact_corner_store_north

label corner_store_south:
    # Screens
    screen interact_corner_store_south():
        frame:
            pos (0.0, 0)
            textbutton "dock":
                xysize (0.15, 1.0)
                action [
                    Jump("dock")
                ]
        frame:
            pos (0.47, 0.3)
            textbutton "tap_alley":
                xysize (0.06, 0.25)
                action [
                    Jump("tap_alley")
                ]
        frame:
            pos (0.56, 0.40)
            textbutton "corner_store_west":
                xysize (0.08, 0.2)
                action [
                    Jump("corner_store_west")
                ]
        frame:
            pos (0.86, 0)
            textbutton "sentinel_alley":
                xysize (0.14, 1.0)
                action [
                    Jump("sentinel_alley")
                ]

    # Sprites
    image bg street_corner_store_south_night:
        "bg street_corner_store_south_night_1.png"
        pause 0.25
        "bg street_corner_store_south_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_corner_store_south_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_corner_store_south_eve
    else:
        scene bg street_corner_store_south
    with fade
    call screen interact_corner_store_south

label corner_store_east:
    # Screens
    screen interact_corner_store_east():
        frame:
            pos (0, 0.8)
            textbutton "corner_store_west":
                xysize (1.0, 0.2)
                action [
                    Jump("corner_store_west")
                ]
        frame:
            pos (0.26, 0.35)
            textbutton "corner_store_north":
                xysize (0.08, 0.35)
                action [
                    Jump("corner_store_north")
                ]
        frame:
            pos (0.66, 0.35)
            textbutton "tap_alley":
                xysize (0.08, 0.35)
                action [
                    Jump("tap_alley")
                ]

    # Sprites
    image bg street_corner_store_east_night:
        "bg street_corner_store_east_night_1.png"
        pause 0.25
        "bg street_corner_store_east_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_corner_store_east_night
    else:
        scene bg street_corner_store_east
    with fade
    call screen interact_corner_store_east

label corner_store_west:
    # Screens
    screen interact_corner_store_west():
        frame:
            pos (0.0, 0)
            textbutton "tap_alley":
                xysize (0.14, 1.0)
                action [
                    Jump("tap_alley")
                ]
        frame:
            pos (0.38, 0.4)
            textbutton "downtown":
                xysize (0.06, 0.2)
                action [
                    Jump("downtown")
                ]
        frame:
            pos (0.45, 0.45)
            textbutton "police_west":
                xysize (0.08, 0.1)
                action [
                    Jump("police_west")
                ]
        frame:
            pos (0.55, 0.45)
            textbutton "station":
                xysize (0.01, 0.1)
                action [
                    Jump("station")
                ]
        frame:
            pos (0.86, 0)
            textbutton "corner_store_north":
                xysize (0.14, 1.0)
                action [
                    Jump("corner_store_north")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.655, 0.40)
                textbutton "corner_store":
                    xysize (0.05, 0.28)
                    action [
                        Jump("corner_store")
                    ]

    # Sprites
    image bg street_corner_store_west_night:
        "bg street_corner_store_west_night_1.png"
        pause 0.25
        "bg street_corner_store_west_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_corner_store_west_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_corner_store_west_eve
    else:
        scene bg street_corner_store_west
    with fade
    call screen interact_corner_store_west
