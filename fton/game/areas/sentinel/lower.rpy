label club:
    # Settings
    if "club" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_club():
        frame:
            pos (0.0, 0.8)
            textbutton "club_stairs":
                xysize (1.0, 0.2)
                action [
                    Hide("zombies_club"),
                    Jump("club_stairs")
                ]
        frame:
            pos (0.13, 0.44)
            textbutton "alcove":
                xysize (0.1, 0.3)
                action [
                    Hide("zombies_club"),
                    Jump("alcove")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.45, 0.46)
                textbutton "dj":
                    xysize (0.1, 0.09)
                    action [
                        Jump("dj")
                    ]

    screen zombies_club_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("club.clear")
                ]
            else:
                action NullAction()
        timer 9:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("club.ambushed")
                ]

    screen zombies_club():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.4, 0.51)
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
            pos (0.15, 0.45)
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
            pos (0.60, 0.45)
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
    image club_strobe:
        "bg plain_black"
        ease 0.5 alpha 0.0
        ease 1.0 alpha 0.5
        repeat

    image bg sentinel_club:
        "bg sentinel_club_1"
        pause 0.5
        "bg sentinel_club_2"
        pause 0.5
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "club" not in progress["zombies"]["clear"]:
            scene bg sentinel_club_night_z
            show screen zombies_club_timer
            show screen zombies_club
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
            scene bg sentinel_club_night
    else:
        scene bg sentinel_club
        show club_strobe
    with fade
    call screen interact_club

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
        hide screen zombies_club_timer
        hide screen zombies_club
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
        $ progress["zombies"]["clear"].append("club")
        hide screen zombies_club_timer
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
        call screen interact_club

label dj:
    # Screens
    screen interact_dj():
        frame:
            pos (0.0, 0.8)
            textbutton "club":
                xysize (1.0, 0.2)
                action [
                    Jump("club")
                ]
        frame:
            pos (0.395, 0.06)
            textbutton "talk_dj":
                xysize (0.25, 0.54)
                action [
                    Jump("dj.talk")
                ]

    # Script
    scene bg sentinel_dj
    show club_strobe
    with fade

    label .talk:
        dixon "The Orange Narwhal? Is that a band?{w=2}{nw}"
        dixon "I don't take requests.{w=2}{nw}"
        call screen interact_dj