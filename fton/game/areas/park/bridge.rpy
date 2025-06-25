label bridge_north:
    # Settings
    if "bridge" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_bridge_north():
        frame:
            pos (0, 0.8)
            textbutton "gazebo_southeast":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_bridge_north"),
                    Jump("gazebo_southeast")
                ]
        frame:
            pos (0.85, 0.45)
            textbutton "river_east":
                xysize (0.15, 0.3)
                action [
                    Hide("zombies_bridge_north"),
                    Jump("river_east")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.0, 0.47)
                textbutton "arch_southwest":
                    xysize (0.25, 0.15)
                    action [
                        Jump("arch_southwest")
                    ]

    screen zombies_bridge_north_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("bridge_north.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("bridge_north.ambushed")
                ]

    screen zombies_bridge_north():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.62, 0.40)
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

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "bridge" not in progress["zombies"]["clear"]:
            scene bg park_bridge_north_night_z
            show screen zombies_bridge_north_timer
            show screen zombies_bridge_north
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
            scene bg park_bridge_north_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_bridge_north_eve
    else:
        scene bg park_bridge_north
    with fade
    call screen interact_bridge_north

    label .ambushed:
        play audio "audio/bite.wav"
        show screen zombie_ambushed
        show zombie_ambush onlayer screens zorder 60:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_bridge_north_timer
        hide screen zombies_bridge_north
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide screen pumping
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        hide sawnoff_base onlayer screens
        hide sawnoff_shells onlayer screens
        hide sawnoff_barrel onlayer screens
        hide sawnoff_hand onlayer screens
        hide screen reloading
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("bridge")
        hide screen zombies_bridge_north_timer
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
            hide sawnoff_base onlayer screens
            hide sawnoff_shells onlayer screens
            hide sawnoff_barrel onlayer screens
            hide sawnoff_hand onlayer screens
            hide screen reloading
            $ inventory["sawnoff"]["ammo"] = 2
        call screen interact_bridge_north

label bridge_southeast:
    # Screens
    screen interact_bridge_southeast():
        frame:
            pos (0, 0.8)
            textbutton "arch_southwest":
                xysize (1.0, 0.20)
                action [
                    Jump("arch_southwest")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.0, 0.33)
                textbutton "river_east":
                    xysize (0.25, 0.15)
                    action [
                        Jump("river_east")
                    ]
            frame:
                pos (0.45, 0.33)
                textbutton "gazebo_southeast":
                    xysize (0.25, 0.15)
                    action [
                        Jump("gazebo_southeast")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_bridge_southeast_night
    else:
        scene bg park_bridge_southeast
    with fade
    call screen interact_bridge_southeast

label bridge_west:
    # Settings
    if "bridge" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_bridge_west():
        frame:
            pos (0, 0.8)
            textbutton "river_east":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_bridge_west"),
                    Jump("river_east")
                ]
        frame:
            pos (0.0, 0.45)
            textbutton "gazebo_southeast":
                xysize (0.25, 0.3)
                action [
                    Hide("zombies_bridge_west"),
                    Jump("gazebo_southeast")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.75, 0.45)
                textbutton "arch_southwest":
                    xysize (0.25, 0.2)
                    action [
                        Jump("arch_southwest")
                    ]

    screen zombies_bridge_west_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("bridge_west.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("bridge_west.ambushed")
                ]

    screen zombies_bridge_west():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.42, 0.40)
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
            pos (0.26, 0.40)
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

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "bridge" not in progress["zombies"]["clear"]:
            scene bg park_bridge_west_night_z
            show screen zombies_bridge_west_timer
            show screen zombies_bridge_west
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
            scene bg park_bridge_west_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_bridge_west_eve
    else:
        scene bg park_bridge_west
    with fade
    call screen interact_bridge_west

    label .ambushed:
        play audio "audio/bite.wav"
        show screen zombie_ambushed
        show zombie_ambush onlayer screens zorder 60:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_bridge_west_timer
        hide screen zombies_bridge_west
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide screen pumping
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        hide sawnoff_base onlayer screens
        hide sawnoff_shells onlayer screens
        hide sawnoff_barrel onlayer screens
        hide sawnoff_hand onlayer screens
        hide screen reloading
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("bridge")
        hide screen zombies_bridge_west_timer
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
            hide sawnoff_base onlayer screens
            hide sawnoff_shells onlayer screens
            hide sawnoff_barrel onlayer screens
            hide sawnoff_hand onlayer screens
            hide screen reloading
            $ inventory["sawnoff"]["ammo"] = 2
        call screen interact_bridge_west
