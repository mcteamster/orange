label tee_north:
    # Screens
    screen interact_tee_north():
        frame:
            pos (0, 0.8)
            textbutton "corner_south":
                xysize (1.0, 0.20)
                action [
                    Jump("corner_south")
                ]
        frame:
            pos (0.38, 0.22)
            textbutton "gate_northeast":
                xysize (0.20, 0.22)
                action [
                    Jump("gate_northeast")
                ]
        frame:
            pos (0.0, 0.31)
            textbutton "gazebo_northwest":
                xysize (0.23, 0.4)
                action [
                    Jump("gazebo_northwest")
                ]

    # Script
    scene bg park_tee_north with fade
    call screen interact_tee_north

label tee_south:
    # Settings
    if "tee" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_tee_south():
        frame:
            pos (0, 0.8)
            textbutton "gate_northeast":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_tee_south"),
                    Jump("gate_northeast")
                ]
        frame:
            pos (0.75, 0.3)
            textbutton "gazebo_northwest":
                xysize (0.25, 0.4)
                action [
                    Hide("zombies_tee_south"),
                    Jump("gazebo_northwest")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.4, 0.2)
                textbutton "corner_south":
                    xysize (0.20, 0.25)
                    action [
                        Jump("corner_south")
                    ]

    screen zombies_tee_south_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("tee_south.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("tee_south.ambushed")
                ]

    screen zombies_tee_south():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.50, 0.33)
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
            pos (0.56, 0.3)
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
            pos (0.35, 0.33)
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
    image bg park_tee_south_night:
        "bg park_tee_south_night_1.png"
        pause 0.25
        "bg park_tee_south_night_2.png"
        pause 0.25
        repeat

    image bg park_tee_south_night_z:
        "bg park_tee_south_night_z_1.png"
        pause 0.25
        "bg park_tee_south_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "tee" not in progress["zombies"]["clear"]:
            scene bg park_tee_south_night_z
            show screen zombies_tee_south_timer
            show screen zombies_tee_south
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
            scene bg park_tee_south_night
    else:
        scene bg park_tee_south
    with fade
    call screen interact_tee_south

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_tee_south_timer
        hide screen zombies_tee_south
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("tee")
        hide screen zombies_tee_south_timer
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
        call screen interact_tee_south

label tee_east:
    screen interact_tee_east():
        frame:
            pos (0, 0.8)
            textbutton "gazebo_northwest":
                xysize (1.0, 0.20)
                action [
                    Jump("gazebo_northwest")
                ]
        frame:
            pos (0.0, 0.4)
            textbutton "gate_northeast":
                xysize (0.25, 0.4)
                action [
                    Jump("gate_northeast")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.75, 0.4)
                textbutton "corner_south":
                    xysize (0.25, 0.4)
                    action [
                        Jump("corner_south")
                    ]

    scene bg park_tee_east with fade
    call screen interact_tee_east