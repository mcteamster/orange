label fork_north:
    # Settings
    if "fork" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_fork_north():
        frame:
            pos (0, 0.8)
            textbutton "corner_east":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_fork_north"),
                    Jump("corner_east")
                ]
        frame:
            pos (0.75, 0.35)
            textbutton "bend_east":
                xysize (0.25, 0.4)
                action [
                    Hide("zombies_fork_north"),
                    Jump("bend_east")
                ]
        frame:
            pos (0.25, 0.38)
            textbutton "arch_northwest":
                xysize (0.25, 0.2)
                action [
                    Hide("zombies_fork_north"),
                    Jump("arch_northwest")
                ]

    screen zombies_fork_north_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("fork_north.clear")
                ]
            else:
                action NullAction()
        timer 7:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("fork_north.ambushed")
                ]

    screen zombies_fork_north():
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

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "fork" not in progress["zombies"]["clear"]:
            scene bg park_fork_north
            show screen zombies_fork_north_timer
            show screen zombies_fork_north
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
            scene bg park_fork_north_night
    else:
        scene bg park_fork_north
    with fade
    call screen interact_fork_north

    label .ambushed:
        play audio "audio/bite.wav"
        show screen zombie_ambushed
        show zombie_ambush onlayer screens zorder 61:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_fork_north_timer
        hide screen zombies_fork_north
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
        $ progress["zombies"]["clear"].append("fork")
        hide screen zombies_fork_north_timer
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
        call screen interact_fork_north


label fork_southeast:
    # Screens
    screen interact_fork_southeast():
        frame:
            pos (0, 0.8)
            textbutton "arch_northwest":
                xysize (1.0, 0.20)
                action [
                    Jump("arch_northwest")
                ]
        frame:
            pos (0.5, 0.3)
            textbutton "corner_east":
                xysize (0.18, 0.2)
                action [
                    Jump("corner_east")
                ]
        frame:
            pos (0.25, 0.3)
            textbutton "bend_east":
                xysize (0.2, 0.2)
                action [
                    Jump("bend_east")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg park_fork_southeast_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg park_fork_southeast_eve
    else:
        scene bg park_fork_southeast
    with fade
    call screen interact_fork_southeast

label fork_west:
    # Settings
    if "fork" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_fork_west():
        frame:
            pos (0, 0.8)
            textbutton "bend_east":
                xysize (1.0, 0.20)
                action [
                    Hide("zombies_fork_west"),
                    Jump("bend_east")
                ]
        frame:
            pos (0, 0.4)
            textbutton "corner_east":
                xysize (0.25, 0.35)
                action [
                    Hide("zombies_fork_west"),
                    Jump("corner_east")
                ]
        frame:
            pos (0.58, 0.39)
            textbutton "arch_northwest":
                xysize (0.1, 0.3)
                action [
                    Hide("zombies_fork_west"),
                    Jump("arch_northwest")
                ]

    screen zombies_fork_west_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("fork_west.clear")
                ]
            else:
                action NullAction()
        timer 7:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("fork_west.ambushed")
                ]

    screen zombies_fork_west():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.35, 0.33)
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
            pos (0.44, 0.3)
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
            pos (0.25, 0.33)
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
        if "fork" not in progress["zombies"]["clear"]:
            scene bg park_fork_west
            show screen zombies_fork_west_timer
            show screen zombies_fork_west
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
            scene bg park_fork_west_night
    else:
        scene bg park_fork_west
    with fade
    call screen interact_fork_west

    label .ambushed:
        play audio "audio/bite.wav"
        show screen zombie_ambushed
        show zombie_ambush onlayer screens zorder 61:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_fork_west_timer
        hide screen zombies_fork_west
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
        $ progress["zombies"]["clear"].append("fork")
        hide screen zombies_fork_west_timer
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
        call screen interact_fork_west
