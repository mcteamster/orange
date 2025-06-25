label bank_south:
    # Settings
    if "bank_south" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_bank_south():
        frame:
            pos (0.0, 0.8)
            textbutton "bank_north":
                xysize (1.0, 0.2)
                if (progress["night"] or inventory["key"]["active"]):
                    action [
                        Hide("zombies_bank_south"),
                        Jump("foyer_entry")
                    ]
                else:
                    action [
                        Jump("bank_north")
                    ]
        frame:
            pos (0.89, 0.18)
            textbutton "gate_west":
                xysize (0.11, 0.72)
                action [
                    Hide("zombies_bank_south"),
                    Jump("gate_west")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.26, 0.3)
                textbutton "police_east":
                    xysize (0.09, 0.4)
                    action [
                        Jump("police_east")
                    ]

    screen zombies_bank_south_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("bank_south.clear")
                ]
            else:
                action NullAction()
        timer 9:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("bank_south.ambushed")
                ]

    screen zombies_bank_south():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.50, 0.44)
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
            pos (0.37, 0.40)
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
            pos (0.60, 0.40)
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
    image bg street_bank_south_night:
        "bg street_bank_south_night_1.png"
        pause 0.25
        "bg street_bank_south_night_2.png"
        pause 0.25
        repeat

    image bg street_bank_south_night_z:
        "bg street_bank_south_night_z_1.png"
        pause 0.25
        "bg street_bank_south_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "bank_south" not in progress["zombies"]["clear"]:
            scene bg street_bank_south_night_z
            show screen zombies_bank_south_timer
            show screen zombies_bank_south
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
            scene bg street_bank_south_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_bank_south_eve
    else:
        scene bg street_bank_south
    with fade
    call screen interact_bank_south

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
        hide screen zombies_bank_south_timer
        hide screen zombies_bank_south
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
        $ progress["zombies"]["clear"].append("bank_south")
        hide screen zombies_bank_south_timer
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
        call screen interact_bank_south

label bank_north:
    # Screens
    screen interact_bank_north():
        frame:
            pos (0.0, 0.8)
            textbutton "bank_south":
                xysize (1.0, 0.2)
                action [
                    Jump("bank_south")
                ]
        frame:
            pos (0.25, 0.3)
            textbutton "gate_west":
                xysize (0.09, 0.4)
                action [
                    Jump("gate_west")
                ]
        frame:
            pos (0.42, 0.35)
            textbutton "foyer_entry":
                xysize (0.16, 0.26)
                action [
                    Jump("foyer_entry")
                ]

    # Script
    scene bg street_bank_north with fade
    call screen interact_bank_north

label bank_south_shootout:
    # Settings
    $ bank_south_shootout_enemies = [
        "swat_a",
        "swat_b",
        "swat_c",
        "swat_d"
    ]

    # Screens
    screen bank_south_timer():
        timer 10:
            if len(bank_south_shootout_enemies) > 0:
                action Jump("bank_south_shootout.fail")

    screen interact_bank_south_shootout():
        button:
            if len(bank_south_shootout_enemies) > 0:
                action [
                    Call("sawnoff.shoot", "bank_south_shootout", None, bank_south_shootout_enemies, from_current=True)
                ]
            else:
                action NullAction()
        frame:
            align (0.5, 0.5)
            pos (0.4, 0.59)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_left"
                selected_idle "swat shot_left"
                selected "swat_a" not in bank_south_shootout_enemies
                sensitive "swat_a" in bank_south_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_south_shootout", "swat_a", bank_south_shootout_enemies, from_current=True)
                ]
                at small
        frame:
            align (0.5, 0.5)
            pos (0.59, 0.59)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_left"
                selected_idle "swat shot_left"
                selected "swat_b" not in bank_south_shootout_enemies
                sensitive "swat_b" in bank_south_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_south_shootout", "swat_b", bank_south_shootout_enemies, from_current=True)
                ]
                at small
        frame:
            align (0.5, 0.5)
            pos (0.33, 0.7)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_center"
                selected_idle "swat shot_center"
                selected "swat_c" not in bank_south_shootout_enemies
                sensitive "swat_c" in bank_south_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_south_shootout", "swat_c", bank_south_shootout_enemies, from_current=True)
                ]
        frame:
            align (0.5, 0.5)
            pos (0.5, 0.7)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_center"
                selected_idle "swat shot_center"
                selected "swat_d" not in bank_south_shootout_enemies
                sensitive "swat_d" in bank_south_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_south_shootout", "swat_d", bank_south_shootout_enemies, from_current=True)
                ]

    # Sprites
    image bank_wall:
        "street/bank_wall.png"
        align (0.0875, 0.0475)
        pos (0, 0)

    # Script
    scene bg street_bank_south
    show screen interact_bank_south_shootout
    show screen bank_south_timer
    show bank_wall as bank_wall_base
    with fade
    show sawnoff equip onlayer screens zorder 50
    pause 3.0

    label .fail:
        scene bg meta_blood_screen
        hide screen interact_bank_south_shootout
        hide screen bank_south_timer
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        hide sawnoff_base onlayer screens
        hide sawnoff_shells onlayer screens
        hide sawnoff_barrel onlayer screens
        hide sawnoff_hand onlayer screens
        hide screen reloading
        $ inventory["sawnoff"]["ammo"] = 2
        stop sound fadeout 1.0
        pause 0.5
        jump street_shot_death

    label .clear:
        screen interact_bank_south_shootout_clear():
            frame:
                pos (0.475, 0.44)
                textbutton "enter_van":
                    xysize (0.085, 0.21)
                    action [
                        Hide(),
                        Jump("clown_quest_complete")
                    ]

        image swat_ambush:
            "enemies/swat.png"
            align (0, 0)
            pos (0.2, 0.5)
            zoom 0.7
            linear 0.25 xpos 0.27

        image swat_hit:
            "enemies/swat_hit.png"
            align (0, 0)
            pos (0.27, 0.48)
            zoom 0.7
            linear 0.25 xpos 0.64

        image clown_van:
            "clown/clown_van.png"
            align (0, 0)
            pos (0, 0.43)
            zoom 0.8
            linear 0.25 xpos 0.33

        show sawnoff unequip onlayer screens
        pause 0.5
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        hide sawnoff_base onlayer screens
        hide sawnoff_shells onlayer screens
        hide sawnoff_barrel onlayer screens
        hide sawnoff_hand onlayer screens
        hide screen reloading
        $ inventory["sawnoff"]["ammo"] = 2
        show swat_ambush onlayer screens
        show bank_wall as bank_wall_overlay onlayer screens zorder 1
        pause 1.0
        hide swat_ambush onlayer screens
        show clown_van onlayer screens
        show swat_hit onlayer screens
        play audio "audio/skid.wav"
        pause 0.25
        hide swat_hit onlayer screens
        show swat_dead_left:
            align (0, 0)
            pos (0.62, 0.595)
            zoom 0.9
        show screen interact_bank_south_shootout_clear
        clown "Jump in!"
        pause

label street_shot_death:
    scene bg plain_charcoal
    show shot_death
    with fade
    play audio "audio/bell.wav"
    pause 6.0
    $ inventory["sawnoff"]["active"] = False
    $ inventory["bomb"]["active"] = True
    $ achievement.grant("shot")
    $ achievement.sync()
    jump game_over