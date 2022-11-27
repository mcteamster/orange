label foyer_entry:
    # Screens
    screen interact_foyer_entry():
        frame:
            pos (0.0, 0.8)
            textbutton "bank_south":
                xysize (1.0, 0.2)
                action [
                    Jump("bank_south")
                ]
        if (progress["night"] or inventory["key"]["active"]):
            frame:
                pos (0.45, 0.45)
                textbutton "stairs":
                    xysize (0.095, 0.19)
                    action [
                        Jump("stairs")
                    ]
        elif progress["quests"]["clowns"]["complete"] == False and (inventory["sawnoff"]["active"] and inventory["cash"]["active"]) == False:
            frame:
                pos (0.45, 0.45)
                textbutton "stairs":
                    xysize (0.095, 0.19)
                    action [
                        Jump("stairs")
                    ]
            frame:
                pos (0.04, 0.5)
                textbutton "teller":
                    xysize (0.12, 0.2)
                    action [
                        Call("teller", "foyer_entry")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg bank_foyer_entry_night with fade
    elif progress["quests"]["clowns"]["complete"] or (inventory["sawnoff"]["active"] and inventory["cash"]["active"]):
        scene bg bank_foyer_entry_bloody with fade
        john "Sorry mate. Bank is closed today.{w=2}{nw}"
    else:
        scene bg bank_foyer_entry with fade

    if inventory["bomb"]["active"]:
        john "Oh my god! He's got a {i}bomb{/i}!{w=2}{nw}"
        show arrest_officer_left
        show arrest_officer_right
        pause 1.0
        jump arrested
    else:
        call screen interact_foyer_entry

label foyer_exit:
    # Settings
    if "bank" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_foyer_exit():
        frame:
            pos (0.0, 0.8)
            textbutton "stairs":
                xysize (1.0, 0.2)
                action [
                    Hide("zombies_foyer_exit"),
                    Jump("stairs")
                ]
        frame:
            pos (0.475, 0.48)
            textbutton "bank_south":
                xysize (0.045, 0.11)
                action [
                    Hide("zombies_foyer_exit"),
                    Jump("bank_south")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.76, 0.5)
                textbutton "teller":
                    xysize (0.115, 0.16)
                    action [
                        Call("teller", "foyer_exit")
                    ]

    screen zombies_foyer_exit_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("foyer_exit.clear")
                ]
            else:
                action NullAction()
        timer 9:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("foyer_exit.ambushed")
                ]

    screen zombies_foyer_exit():
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
            pos (0.15, 0.48)
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
            pos (0.55, 0.48)
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
        if "bank" not in progress["zombies"]["clear"]:
            scene bg bank_foyer_exit_night_z
            show screen zombies_foyer_exit_timer
            show screen zombies_foyer_exit
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
            scene bg bank_foyer_exit_night
    else:
        scene bg bank_foyer_exit 
    with fade
    call screen interact_foyer_exit

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
        hide screen zombies_foyer_exit_timer
        hide screen zombies_foyer_exit
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
        $ progress["zombies"]["clear"].append("bank")
        hide screen zombies_foyer_exit_timer
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
        call screen interact_foyer_exit

label teller(origin):
    screen interact_teller():
        frame:
            pos (0.0, 0.8)
            textbutton "foyer":
                xysize (1.0, 0.2)
                action [
                    Jump(origin)
                ]

    scene bg bank_teller with fade
    john "Your account appears to be empty.{w=2}{nw}"
    john "Um. No. I know nothing about an Orange Narwhal.{w=2}{nw}"
    call screen interact_teller

label bank_foyer_shootout:
    $ bank_foyer_shootout_enemies = [
        "swat_a",
        "swat_b",
        "swat_c",
        "swat_d",
        "swat_e",
        "swat_f",
    ]
    screen bank_foyer_timer():
        timer 12:
            if len(bank_foyer_shootout_enemies) > 0:
                action Jump("bank_foyer_shootout.fail")

    screen interact_bank_foyer_shootout():
        button:
            if len(bank_foyer_shootout_enemies) > 0:
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", None, bank_foyer_shootout_enemies, from_current=True)
                ]
            else:
                action NullAction()
        frame:
            align (0.5, 0.5)
            pos (0.34, 0.65)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_center"
                selected_idle "swat shot_center"
                selected "swat_a" not in bank_foyer_shootout_enemies
                sensitive "swat_a" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_a", bank_foyer_shootout_enemies, from_current=True)
                ]
                at medium
        frame:
            align (0.5, 0.5)
            pos (0.5, 0.63)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_center"
                selected_idle "swat shot_center"
                selected "swat_b" not in bank_foyer_shootout_enemies
                sensitive "swat_b" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_b", bank_foyer_shootout_enemies, from_current=True)
                ]
                at medium
        frame:
            align (0.5, 0.5)
            pos (0.67, 0.63)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_left"
                selected_idle "swat shot_left"
                selected "swat_c" not in bank_foyer_shootout_enemies
                sensitive "swat_c" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_c", bank_foyer_shootout_enemies, from_current=True)
                ]
                at medium
        frame:
            align (0.5, 0.5)
            pos (0.18, 0.75)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_right"
                selected_idle "swat shot_right"
                selected "swat_d" not in bank_foyer_shootout_enemies
                sensitive "swat_d" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_d", bank_foyer_shootout_enemies, from_current=True)
                ]
        frame:
            align (0.5, 0.5)
            pos (0.4, 0.7)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_left"
                selected_idle "swat shot_left"
                selected "swat_e" not in bank_foyer_shootout_enemies
                sensitive "swat_e" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_e", bank_foyer_shootout_enemies, from_current=True)
                ]
        frame:
            align (0.5, 0.5)
            pos (0.6, 0.72)
            imagebutton:
                idle "swat shooting"
                insensitive "swat shot_center"
                selected_idle "swat shot_center"
                selected "swat_f" not in bank_foyer_shootout_enemies
                sensitive "swat_f" in bank_foyer_shootout_enemies
                action [
                    Call("sawnoff.shoot", "bank_foyer_shootout", "swat_f", bank_foyer_shootout_enemies, from_current=True)
                ]

    scene bg bank_foyer_exit_shootout
    show screen interact_bank_foyer_shootout
    show screen bank_foyer_timer
    with fade
    show sawnoff equip onlayer screens zorder 50
    pause 3.0

    label .fail:
        scene bg meta_blood_screen
        hide screen interact_bank_foyer_shootout
        hide screen bank_foyer_timer
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
        jump bank_shot_death

    label .clear:
        hide screen bank_foyer_timer
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
        scene bg plain_white 
        hide screen interact_bank_foyer_shootout
        with fade
        jump bank_south_shootout

label bank_shot_death:
    scene bg bank_floor
    show shot_death
    with fade
    play audio "audio/bell.wav"
    pause 6.0
    $ inventory["sawnoff"]["active"] = False
    $ inventory["bomb"]["active"] = True
    jump game_over