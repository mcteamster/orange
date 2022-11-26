label gate_northeast:
    # Screens
    screen interact_gate_northeast():
        frame:
            pos (0.45, 0.8)
            textbutton "tee_south":
                xysize (0.55, 0.20)
                action [
                    Jump("tee_south")
                ]
        frame:
            pos (0.0, 0.36)
            textbutton "river_north":
                xysize (0.25, 0.3)
                action [
                    Jump("river_north")
                ]
        frame:
            pos (0.45, 0.2)
            textbutton "bank_south":
                xysize (0.15, 0.3)
                action [
                    Jump("bank_south")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.0, 0.7)
                textbutton "gazebo_west":
                    xysize (0.3, 0.3)
                    action [
                        Jump("gazebo_west")
                    ]

    # Script
    scene bg park_gate_northeast with fade
    call screen interact_gate_northeast

label gate_southeast:
    # Screens
    screen interact_gate_southeast():
        frame:
            pos (0.75, 0.48)
            textbutton "tee_south":
                xysize (0.25, 0.20)
                action [
                    Jump("tee_south")
                ]
        frame:
            pos (0.0, 0.8)
            textbutton "river_north":
                xysize (0.60, 0.2)
                action [
                    Jump("river_north")
                ]
        frame:
            pos (0.39, 0.2)
            textbutton "bank_south":
                xysize (0.15, 0.3)
                action [
                    Jump("bank_south")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.7, 0.8)
                textbutton "gazebo_west":
                    xysize (0.3, 0.2)
                    action [
                        Jump("gazebo_west")
                    ]

    # Script
    scene bg park_gate_southeast with fade
    call screen interact_gate_southeast

label gate_east:
    # Screens
    screen interact_gate_east():
        frame:
            pos (0.75, 0.6)
            textbutton "tee_south":
                xysize (0.25, 0.4)
                action [
                    Jump("tee_south")
                ]
        frame:
            pos (0.0, 0.5)
            textbutton "river_north":
                xysize (0.25, 0.25)
                action [
                    
                    Jump("river_north")
                ]
        frame:
            pos (0.41, 0.2)
            textbutton "bank_south":
                xysize (0.15, 0.3)
                action [
                    Jump("bank_south")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.0, 0.8)
                textbutton "gazebo_west":
                    xysize (0.75, 0.2)
                    action [
                        Jump("gazebo_west")
                    ]

    # Script
    scene bg park_gate_east with fade
    call screen interact_gate_east

label gate_west:
    # Settings
    if "gate" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_gate_west():
        frame:
            pos (0, 0.8)
            textbutton "bank_south":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_gate_west"),
                    Jump("bank_south")
                ]
        frame:
            pos (0.2, 0.4)
            textbutton "tee_south":
                xysize (0.20, 0.25)
                action [
                    Hide("zombies_gate_west"),
                    Jump("tee_south")
                ]
        frame:
            pos (0.6, 0.4)
            textbutton "river_north":
                xysize (0.20, 0.25)
                action [
                    Hide("zombies_gate_west"),
                    Jump("river_north")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.42, 0.3)
                textbutton "gazebo_west":
                    xysize (0.16, 0.25)
                    action [
                        Jump("gazebo_west")
                    ]

    screen zombies_gate_west_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("gate_west.clear")
                ]
            else:
                action NullAction()
        timer 8:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("gate_west.ambushed")
                ]

    screen zombies_gate_west():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.43, 0.40)
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
            pos (0.32, 0.37)
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
            pos (0.62, 0.40)
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
    image bg park_gate_west_night:
        "bg park_gate_west_night_1.png"
        pause 0.25
        "bg park_gate_west_night_2.png"
        pause 0.25
        repeat

    image bg park_gate_west_night_z:
        "bg park_gate_west_night_z_1.png"
        pause 0.25
        "bg park_gate_west_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "gate" not in progress["zombies"]["clear"]:
            scene bg park_gate_west_night_z
            show screen zombies_gate_west_timer
            show screen zombies_gate_west
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
            scene bg park_gate_west_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_gate_west_eve
    else:
        scene bg park_gate_west
    with fade
    call screen interact_gate_west

    label .ambushed:
        play audio "audio/bite.wav"
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_gate_west_timer
        hide screen zombies_gate_west
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
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
        $ progress["zombies"]["clear"].append("gate")
        hide screen zombies_gate_west_timer
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
        call screen interact_gate_west