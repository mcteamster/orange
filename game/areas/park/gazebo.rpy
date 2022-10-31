label gazebo(origin):
    scene bg park_gazebo with fade
    "This is a nice gazebo"
    jump expression origin

label gazebo_northeast:
    # Settings
    if "gazebo_northeast" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_gazebo_northeast():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.3, 0)
                textbutton "gazebo":
                    xysize (0.4, 0.6)
                    action [
                        Call("gazebo", "gazebo_northeast")
                    ]
            frame:
                pos (0.72, 0.42)
                textbutton "gate_east":
                    xysize (0.13, 0.12)
                    action [
                        Jump("gate_east")
                    ]
        frame:
            pos (0, 0.8)
            textbutton "bend_southwest":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_gazebo_northeast"),
                    Jump("bend_southwest")
                ]
        frame:
            pos (0.0, 0.5)
            textbutton "bridge_north":
                xysize (0.15, 0.2)
                action [
                    Hide("zombies_gazebo_northeast"),
                    Jump("bridge_north")
                ]

        frame:
            pos (0.8, 0.55)
            textbutton "tee_east":
                xysize (0.2, 0.10)
                action [
                    Hide("zombies_gazebo_northeast"),
                    Jump("tee_east")
                ]

    screen zombies_gazebo_northeast_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("gazebo_northeast.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("gazebo_northeast.ambushed")
                ]

    screen zombies_gazebo_northeast():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.50, 0.40)
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
            pos (0.56, 0.37)
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
            pos (0.35, 0.40)
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
    image bg park_gazebo_northeast_night:
        "bg park_gazebo_northeast_night_1.png"
        pause 0.25
        "bg park_gazebo_northeast_night_2.png"
        pause 0.25
        repeat

    image bg park_gazebo_northeast_night_z:
        "bg park_gazebo_northeast_night_z_1.png"
        pause 0.25
        "bg park_gazebo_northeast_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "gazebo_northeast" not in progress["zombies"]["clear"]:
            scene bg park_gazebo_northeast_night_z
            show screen zombies_gazebo_northeast_timer
            show screen zombies_gazebo_northeast
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
            scene bg park_gazebo_northeast_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_gazebo_northeast_eve
    else:
        scene bg park_gazebo_northeast
    with fade
    call screen interact_gazebo_northeast

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_gazebo_northeast_timer
        hide screen zombies_gazebo_northeast
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("gazebo_northeast")
        hide screen zombies_gazebo_northeast_timer
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
        call screen interact_gazebo_northeast

label gazebo_northwest:
    # Settings
    if "gazebo_northwest" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_gazebo_northwest():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.3, 0)
                textbutton "gazebo":
                    xysize (0.4, 0.6)
                    action [
                        Call("gazebo", "gazebo_northwest")
                    ]
            frame:
                pos (0.75, 0.5)
                textbutton "gate_east":
                    xysize (0.25, 0.2)
                    action [
                        Jump("gate_east")
                    ]
        frame:
            pos (0, 0.8)
            textbutton "tee_east":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_gazebo_northwest"),
                    Jump("tee_east")
                ]
        frame:
            pos (0.0, 0.45)
            textbutton "bend_southwest":
                xysize (0.15, 0.2)
                action [
                    Hide("zombies_gazebo_northwest"),
                    Jump("bend_southwest")
                ]
        frame:
            pos (0.16, 0.4)
            textbutton "bridge_north":
                xysize (0.13, 0.15)
                action [
                    Hide("zombies_gazebo_northwest"),
                    Jump("bridge_north")
                ]

    screen zombies_gazebo_northwest_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("gazebo_northwest.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("gazebo_northwest.ambushed")
                ]

    screen zombies_gazebo_northwest():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.50, 0.40)
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
            pos (0.56, 0.37)
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
            pos (0.35, 0.40)
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
    image bg park_gazebo_northwest_night:
        "bg park_gazebo_northwest_night_1.png"
        pause 0.25
        "bg park_gazebo_northwest_night_2.png"
        pause 0.25
        repeat

    image bg park_gazebo_northwest_night_z:
        "bg park_gazebo_northwest_night_z_1.png"
        pause 0.25
        "bg park_gazebo_northwest_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "gazebo_northwest" not in progress["zombies"]["clear"]:
            scene bg park_gazebo_northwest_night_z
            show screen zombies_gazebo_northwest_timer
            show screen zombies_gazebo_northwest
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
            scene bg park_gazebo_northwest_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_gazebo_northwest_eve
    else:
        scene bg park_gazebo_northwest
    with fade
    call screen interact_gazebo_northwest

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_gazebo_northwest_timer
        hide screen zombies_gazebo_northwest
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("gazebo_northwest")
        hide screen zombies_gazebo_northwest_timer
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
        call screen interact_gazebo_northwest

label gazebo_southeast:
    # Settings
    if "gazebo_southeast" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_gazebo_southeast():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.3, 0)
                textbutton "gazebo":
                    xysize (0.4, 0.6)
                    action [
                        Call("gazebo", "gazebo_southeast")
                    ]
            frame:
                pos (0.44, 0.4)
                textbutton "gate_east":
                    xysize (0.1, 0.12)
                    action [
                        Jump("gate_east")
                    ]
        frame:
            pos (0, 0.8)
            textbutton "bridge_north":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_gazebo_southeast"),
                    Jump("bridge_north")
                ]
        frame:
            pos (0.8, 0.58)
            textbutton "bend_southwest":
                xysize (0.2, 0.2)
                action [
                    Hide("zombies_gazebo_southeast"),
                    Jump("bend_southwest")
                ]
        frame:
            pos (0.75, 0.4)
            textbutton "tee_east":
                xysize (0.15, 0.15)
                action [
                    Hide("zombies_gazebo_southeast"),
                    Jump("tee_east")
                ]

    screen zombies_gazebo_southeast_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("gazebo_southeast.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("gazebo_southeast.ambushed")
                ]

    screen zombies_gazebo_southeast():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.50, 0.40)
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
            pos (0.56, 0.37)
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
            pos (0.35, 0.40)
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
    image bg park_gazebo_southeast_night:
        "bg park_gazebo_southeast_night_1.png"
        pause 0.25
        "bg park_gazebo_southeast_night_2.png"
        pause 0.25
        repeat

    image bg park_gazebo_southeast_night_z:
        "bg park_gazebo_southeast_night_z_1.png"
        pause 0.25
        "bg park_gazebo_southeast_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "gazebo_southeast" not in progress["zombies"]["clear"]:
            scene bg park_gazebo_southeast_night_z
            show screen zombies_gazebo_southeast_timer
            show screen zombies_gazebo_southeast
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
            scene bg park_gazebo_southeast_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_gazebo_southeast_eve
    else:
        scene bg park_gazebo_southeast
    with fade
    call screen interact_gazebo_southeast

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_gazebo_southeast_timer
        hide screen zombies_gazebo_southeast
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("gazebo_southeast")
        hide screen zombies_gazebo_southeast_timer
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
        call screen interact_gazebo_southeast

label gazebo_west:
    # Screens
    screen interact_gazebo_west():
        frame:
            pos (0.3, 0)
            textbutton "gazebo":
                xysize (0.4, 0.6)
                action [
                    Call("gazebo", "gazebo_west")
                ]
        frame:
            pos (0.2, 0.8)
            textbutton "gate_east":
                xysize (0.8, 0.20)
                action [
                    Jump("gate_east")
                ]
        frame:
            pos (0.0, 0.6)
            textbutton "tee_east":
                xysize (0.2, 0.4)
                action [
                    Jump("tee_east")
                ]
        frame:
            pos (0.12, 0.38)
            textbutton "bend_southwest":
                xysize (0.15, 0.2)
                action [
                    Jump("bend_southwest")
                ]
        frame:
            pos (0.35, 0.4)
            textbutton "bridge_north":
                xysize (0.14, 0.13)
                action [
                    Jump("bridge_north")
                ]

    # Script
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_gazebo_west_eve
    else:
        scene bg park_gazebo_west
    with fade
    call screen interact_gazebo_west