label club_stairs:
    # Screens
    screen interact_club_stairs():
        frame:
            pos (0.0, 0.8)
            textbutton "sentinel_alley":
                xysize (1.0, 0.2)
                action [
                    Jump("sentinel_alley")
                ]
        frame:
            pos (0.48, 0.45)
            textbutton "club":
                xysize (0.035, 0.06)
                action [
                    Jump("club")
                ]

    # Sprites
    image bg sentinel_club_stairs:
        "bg sentinel_club_stairs_1"
        pause 0.5
        "bg sentinel_club_stairs_2"
        pause 0.5
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg sentinel_club_stairs_night
    else:
        scene bg sentinel_club_stairs
    with fade
    call screen interact_club_stairs

label alcove:
    # Settings
    if "alcove" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_alcove():
        frame:
            pos (0.0, 0.8)
            textbutton "club":
                xysize (1.0, 0.2)
                action [
                    Hide("zombies_alcove"),
                    Jump("club")
                ]
        frame:
            pos (0.16, 0.32)
            textbutton "talk_guard":
                xysize (0.09, 0.47)
                action [
                    Hide("zombies_alcove"),
                    Jump("alcove.talk")
                ]

    screen zombies_alcove_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("alcove.clear")
                ]
            else:
                action NullAction()
        timer 9:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("alcove.ambushed")
                ]

    screen zombies_alcove():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.4, 0.45)
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
            pos (0.53, 0.42)
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
    image bg sentinel_alcove:
        "bg sentinel_alcove_1"
        pause 0.5
        "bg sentinel_alcove_2"
        pause 0.5
        repeat

    image alcove_clown_guard:
        "clown/clown_guard.png"
        align (0, 0)
        pos (0.17, 0.35)

    image alcove_police_guard:
        "police/police_guard.png"
        align (0, 0)
        pos (0.17, 0.35)

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "alcove" not in progress["zombies"]["clear"]:
            scene bg sentinel_alcove_night_z
            show screen zombies_alcove_timer
            show screen zombies_alcove
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
            scene bg sentinel_alcove_night
    else:
        scene bg sentinel_alcove
        if progress["quests"]["clowns"]["complete"] or (inventory["sawnoff"]["active"] and inventory["cash"]["active"]):
            show alcove_police_guard
        elif inventory["bomb"]["active"] == False:
            show alcove_clown_guard
    with fade
    call screen interact_alcove

    label .talk:
        if inventory["bomb"]["active"] or (progress["night"] or inventory["key"]["active"]):
            jump backroom
        elif progress["quests"]["clowns"]["complete"] or (inventory["sawnoff"]["active"] and inventory["cash"]["active"]):
            officer "Sorry mate. No entry. Crime scene."
        elif inventory["letter"]["active"]:
            clown "Why haven't you got the package yet?"
            clown "Take that {i}letter{/i} to the man in the fireworks store."
        else:
            clown "Sorry mate. No Entry. Private Clown business."
        call screen interact_alcove

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
        hide screen zombies_alcove_timer
        hide screen zombies_alcove
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
        $ progress["zombies"]["clear"].append("alcove")
        hide screen zombies_alcove_timer
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
        call screen interact_alcove

label backroom:
    # Screens
    screen interact_backroom():
        frame:
            pos (0.0, 0.8)
            textbutton "alcove":
                xysize (1.0, 0.2)
                action [
                    Jump("alcove")
                ]
        if (progress["night"] or inventory["key"]["active"]) and (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]):
            frame:
                pos (0.36, 0.34)
                textbutton "inner_vault":
                    xysize (0.25, 0.39)
                    action [
                        Jump("inner_vault")
                    ]
        elif (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.49, 0.385)
                textbutton "breach":
                    xysize (0.075, 0.49)
                    action [
                        Jump("backroom.breach")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]) and (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]):
        scene bg sentinel_backroom_hole_night
    elif (progress["night"] or inventory["key"]["active"]):
        scene bg sentinel_backroom_empty_night
    else:
        scene bg sentinel_backroom
    with fade
    call screen interact_backroom

    label .breach:
        screen interact_backroom_breach():
            frame:
                pos (0.36, 0.34)
                textbutton "inner_vault":
                    xysize (0.25, 0.39)
                    action [
                        Jump("inner_vault")
                    ]

        $ inventory["bomb"]["active"] = False
        scene bg plain_white with fade
        scene bg sentinel_backroom_closeup with fade
        clown "Brilliant."
        clown "Alright boys. It's show time."
        clown "Put on a smile!"
        scene bg sentinel_backroom_breaching with fade
        pause 1.0
        play audio "audio/explosion.wav"
        show explosion_hole:
            align (0.5, 0.5)
            pos (0.5, 0.6)
        show explosion_smoke:
            align (0.5, 0.5)
            pos (0.5, 0.55)
            zoom 1
            alpha 1.0
            linear 0.5 zoom 1.25 ypos 0.45 alpha 0.0
        show explosion_flash:
            align (0.5, 0.5)
            pos (0.5, 0.55)
            zoom 1
            alpha 1.0
            linear 0.25 zoom 2 alpha 0.0
        with vpunch
        call screen interact_backroom_breach