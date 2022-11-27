label dock:
    # Settings
    if "dock" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Settings
    $ inventory["smoke"]["highlight"] = False

    # Screens
    screen interact_dock():
        frame:
            pos (0.0, 0)
            textbutton "corner_store_south":
                xysize (0.1, 1.0)
                action [
                    Hide("zombies_dock"),
                    Jump("corner_store_south")
                ]
        frame:
            pos (0.7, 0.7)
            textbutton "pier":
                xysize (0.3, 0.3)
                action [
                    Hide("zombies_dock"),
                    Jump("pier")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.255, 0.20)
                textbutton "pub":
                    xysize (0.055, 0.43)
                    action [
                        Jump("pub")
                    ]

    screen zombies_dock_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("dock.clear")
                ]
            else:
                action NullAction()
        timer 10:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("dock.ambushed")
                ]

    screen zombies_dock():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.37, 0.3)
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
                    ground "zombie_pirate_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_pirate_b half"
            else: 
                ground "zombie_pirate_b dead"
        imagemap:
            pos (0.48, 0.29)
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
                    ground "zombie_pirate_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_pirate_a half"
            else: 
                ground "zombie_pirate_a dead"
        imagemap:
            pos (0.2, 0.25)
            alpha True
            if zombies["z3"] > 0:
                hotspot (0, 0, 200, 100):
                    action [
                        Call(shoot_command, "zombies", "z3", zombies, damage=0, from_current=True),
                    ]
                hotspot (0, 100, 200, 1000):
                    ypos 100
                    action [
                        Call(shoot_command, "zombies", "z3", zombies, from_current=True),
                    ]
                if zombies["z3"] == 2:
                    ground "zombie_pirate_c full"
                elif zombies["z3"] == 1:
                    ground "zombie_pirate_c half"
            else: 
                ground "zombie_pirate_c dead"

    # Sprites
    image bg street_dock_night:
        "bg street_dock_night_1.png"
        pause 0.25
        "bg street_dock_night_2.png"
        pause 0.25
        repeat

    image bg street_dock_night_z:
        "bg street_dock_night_z_1.png"
        pause 0.25
        "bg street_dock_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "dock" not in progress["zombies"]["clear"]:
            scene bg street_dock_night_z
            show screen zombies_dock_timer
            show screen zombies_dock
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
            scene bg street_dock_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_dock_eve
    else:
        scene bg street_dock
    with fade
    call screen interact_dock

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
        hide screen zombies_dock_timer
        hide screen zombies_dock
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
        $ progress["zombies"]["clear"].append("dock")
        hide screen zombies_dock_timer
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
        call screen interact_dock

label pier:
    # Screens
    screen interact_pier():
        frame:
            pos (0.7, 0.45)
            textbutton "depths":
                xysize (0.3, 0.55)
                if inventory["helmet"]["active"]:
                    action [
                        Call("ship", "pier")
                    ]
                else:
                    action [
                        Jump("pier.think")
                    ]
        frame:
            pos (0, 0.8)
            textbutton "dock":
                xysize (1.0, 0.2)
                action [
                    Jump("dock")
                ]
                
    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg street_pier_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_pier_eve
    else:
        scene bg street_pier
    with fade
    call screen interact_pier

    label .think:
        "I'd love to go swimming, but I don't have any diving equipment with me.{w=2}{nw}"
        call screen interact_pier

    label .dive:
        screen interact_pier_dive():
            frame:
                pos (0.37, 0.125)
                textbutton "harpoon":
                    xysize (0.08, 0.6)
                    action [
                        Jump("pier.harpoon")
                    ]
        
        image pier_captain_helmet:
            "pirate/captain_helmet_sword.png"
            align (0.5, 0.5)
            pos (0.65, 0.45)

        image pier_captain_helmet diving:
            "pirate/captain_helmet_sword.png"
            rotate 0
            align (0.5, 0.5)
            pos (0.65, 0.45)
            ease 2.0 pos (1.5, 1.5) rotate 450

        image pier_pirate_blue:
            "pirate/pirate_blue.png"
            align (0.0, 0.0)
            pos (0.5, 0.25)

        image pier_pirate_purple:
            "pirate/pirate_purple.png"
            align (0.0, 0.0)
            pos (0.25, 0.1)

        image pier_pirate_purple_hand:
            "pirate/pirate_hand.png"
            align (0.0, 0.0)
            pos (0.365, 0.4)

        image pier_handed_harpoon:
            "pirate/handed_harpoon.png"
            align (0.0, 0.0)
            pos (0.365, 0.12)

        image pier_bollard:
            "pirate/bollard.png"
            align (0.0, 0.0)
            pos (0.915, 0.56)

        scene bg plain_white with fade
        scene bg street_pier
        show pier_bollard zorder 1
        show pier_captain_helmet
        show pier_pirate_blue
        show pier_pirate_purple
        show pier_handed_harpoon
        with fade
        captain "Ahoy me harty. Grab that there harpoon and join me in the depths!"
        call screen interact_pier_dive

    label .harpoon:
        screen interact_pier_harpoon():
            frame:
                pos (0.7, 0.45)
                textbutton "depths":
                    xysize (0.3, 0.55)
                    action [
                        Jump("ship.fight")
                    ]

        hide pier_handed_harpoon
        show pier_pirate_purple_hand
        show pier_captain_helmet diving
        call screen interact_pier_harpoon