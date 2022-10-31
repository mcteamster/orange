label junction:
    # Settings
    if "junction" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_junction():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0, 0.3)
                textbutton "junction_bus":
                    xysize (0.08, 0.7)
                    action [
                        Jump("junction_bus")
                    ]
        frame:
            pos (0.38, 0.34)
            textbutton "cliefwood":
                xysize (0.06, 0.25)
                action [
                    Hide("zombies_junction"),
                    Jump("cliefwood")
                ]
        frame:
            pos (0.45, 0.34)
            textbutton "tent":
                xysize (0.08, 0.2)
                action [
                    Hide("zombies_junction"),
                    Jump("tent")
                ]
        frame:
            pos (0.62, 0.33)
            textbutton "chinatown_east":
                xysize (0.38, 0.5)
                action [
                    Hide("zombies_junction"),
                    Jump("chinatown_east")
                ]

    screen zombies_junction_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("junction.clear")
                ]
            else:
                action NullAction()
        timer 6:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("junction.ambushed")
                ]

    screen zombies_junction():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.55, 0.42)
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
                    ground "zombie_clown_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_clown_b half"
            else: 
                ground "zombie_clown_b dead"
        imagemap:
            pos (0.3, 0.4)
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
                    ground "zombie_clown_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_clown_a half"
            else: 
                ground "zombie_clown_a dead"
        imagemap:
            pos (0.45, 0.40)
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
                    ground "zombie_clown_c full"
                elif zombies["z3"] == 1:
                    ground "zombie_clown_c half"
            else: 
                ground "zombie_clown_c dead"

    # Sprites
    image bg street_junction_night:
        "bg street_junction_night_1.png"
        pause 0.25
        "bg street_junction_night_2.png"
        pause 0.25
        repeat

    image bg street_junction_night_z:
        "bg street_junction_night_z_1.png"
        pause 0.25
        "bg street_junction_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "junction" not in progress["zombies"]["clear"]:
            scene bg street_junction_night_z
            show screen zombies_junction_timer
            show screen zombies_junction
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
            scene bg street_junction_night
    else:
        $ junction_scene = "bg street_junction"
        if progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]:
            $ junction_scene += "_police"
        if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
            $ junction_scene += "_eve"
        scene expression junction_scene
    with fade
    call screen interact_junction

    label .ambushed:
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_junction_timer
        hide screen zombies_junction
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("junction")
        hide screen zombies_junction_timer
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
        call screen interact_junction