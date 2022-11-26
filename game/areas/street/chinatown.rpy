label chinatown_east:
    # Screens
    screen interact_chinatown_east():
        frame:
            pos (0.0, 0.8)
            textbutton "junction":
                xysize (1.0, 0.2)
                action [
                    Jump("junction")
                ]
        frame:
            pos (0.755, 0.31)
            textbutton "arch_east":
                xysize (0.1, 0.11)
                action [
                    Jump("arch_east")
                ]
        if (inventory["shotgun"]["active"] == False) or (progress["night"] or inventory["key"]["active"]):
            frame:
                pos (0.21, 0.32)
                textbutton "arcade":
                    xysize (0.095, 0.4)
                    action [
                        Call("arcade", "chinatown_east")
                    ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            if inventory["shotgun"]["active"] == False:
                frame:
                    pos (0.685, 0.36)
                    textbutton "fireworks":
                        xysize (0.015, 0.1)
                        action [
                            Call("fireworks", "chinatown_east")
                        ]
                frame:
                    pos (0.57, 0.35)
                    textbutton "noodle_house":
                        xysize (0.03, 0.17)
                        action [
                            Call("noodle_house", "chinatown_east")
                        ]

    # Sprites
    image bg street_chinatown_east_night:
        "bg street_chinatown_east_night_1.png"
        pause 0.25
        "bg street_chinatown_east_night_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_chinatown_east_night
    else:
        $ chinatown_east_scene = "bg street_chinatown_east"
        if progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]:
            $ chinatown_east_scene += "_police"
        if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
            $ chinatown_east_scene += "_eve"
        scene expression chinatown_east_scene
    with fade
    call screen interact_chinatown_east

label chinatown_west:
    # Settings
    if "chinatown" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_chinatown_west():
        frame:
            pos (0.0, 0.8)
            textbutton "arch_east":
                xysize (1.0, 0.2)
                action [
                    Hide("zombies_chinatown_west"),
                    Jump("arch_east")
                ]
        frame:
            pos (0.14, 0.31)
            textbutton "junction":
                xysize (0.1, 0.11)
                action [
                    Hide("zombies_chinatown_west"),
                    Jump("junction")
                ]
        if (inventory["shotgun"]["active"] == False) or (progress["night"] or inventory["key"]["active"]):
            frame:
                pos (0.27, 0.35)
                textbutton "arcade":
                    xysize (0.015, 0.1)
                    action [
                        Hide("zombies_chinatown_west"),
                        Call("arcade", "chinatown_west")
                    ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            if inventory["shotgun"]["active"] == False:
                frame:
                    pos (0.40, 0.35)
                    textbutton "noodle_house":
                        xysize (0.025, 0.18)
                        action [
                            Call("noodle_house", "chinatown_west")
                        ]
                frame:
                    pos (0.56, 0.34)
                    textbutton "fireworks":
                        xysize (0.06, 0.28)
                        action [
                            Call("fireworks", "chinatown_west")
                        ]

    screen zombies_chinatown_west_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("chinatown_west.clear")
                ]
            else:
                action NullAction()
        timer 7:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("chinatown_west.ambushed")
                ]

    screen zombies_chinatown_west():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.3, 0.37)
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
                    ground "zombie_ninja_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_ninja_b half"
            else: 
                ground "zombie_ninja_b dead"
        imagemap:
            pos (0.62, 0.39)
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
                    ground "zombie_ninja_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_ninja_a half"
            else: 
                ground "zombie_ninja_a dead"
        imagemap:
            pos (0.18, 0.39)
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
                    ground "zombie_ninja_c full"
                elif zombies["z3"] == 1:
                    ground "zombie_ninja_c half"
            else: 
                ground "zombie_ninja_c dead"

    # Sprites
    image bg street_chinatown_west_night:
        "bg street_chinatown_west_night_1.png"
        pause 0.25
        "bg street_chinatown_west_night_2.png"
        pause 0.25
        repeat

    image bg street_chinatown_west_night_z:
        "bg street_chinatown_west_night_z_1.png"
        pause 0.25
        "bg street_chinatown_west_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "chinatown" not in progress["zombies"]["clear"]:
            scene bg street_chinatown_west_night_z
            show screen zombies_chinatown_west_timer
            show screen zombies_chinatown_west
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
            scene bg street_chinatown_west_night
    else:
        $ chinatown_west_scene = "bg street_chinatown_west"
        if progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]:
            $ chinatown_west_scene += "_police"
        if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
            $ chinatown_west_scene += "_eve"
        scene expression chinatown_west_scene
    with fade
    call screen interact_chinatown_west

    label .ambushed:
        play audio "audio/bite.wav"
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_chinatown_west_timer
        hide screen zombies_chinatown_west
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
        $ progress["zombies"]["clear"].append("chinatown")
        hide screen zombies_chinatown_west_timer
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
        call screen interact_chinatown_west