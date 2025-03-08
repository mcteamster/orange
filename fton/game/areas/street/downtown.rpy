label downtown:
    # Settings
    $ inventory["smoke"]["highlight"] = False
    if "downtown" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 5,
            "z1": 2,
            "z2": 2,
            "z3": 1,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_downtown():
        frame:
            pos (0.09, 0.4)
            textbutton "lobby":
                xysize (0.08, 0.35)
                action [
                    Hide("zombies_downtown"),
                    Jump("lobby")
                ]
        frame:
            pos (0.35, 0.45)
            textbutton "police_west":
                xysize (0.05, 0.15)
                action [
                    Hide("zombies_downtown"),
                    Jump("police_west")
                ]
        frame:
            pos (0.415, 0.46)
            textbutton "station":
                xysize (0.04, 0.10)
                action [
                    Hide("zombies_downtown"),
                    Jump("station")
                ]
        frame:
            pos (0.59, 0.45)
            textbutton "corner_store_east":
                xysize (0.05, 0.15)
                action [
                    Hide("zombies_downtown"),
                    Jump("corner_store_east")
                ]
        frame:
            pos (0.69, 0.37)
            textbutton "tavern":
                xysize (0.05, 0.35)
                action [
                    Hide("zombies_downtown"),
                    Jump("tavern")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.92, 0.33)
                textbutton "downtown_bus":
                    xysize (0.08, 0.60)
                    action [
                        Jump("downtown_bus")
                    ]
            frame:
                pos (0.555, 0.47)
                textbutton "corner_store":
                    xysize (0.025, 0.08)
                    action [
                        Jump("corner_store")
                    ]
        
    screen zombies_downtown_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("downtown.clear")
                ]
            else:
                action NullAction()
        timer 10:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("downtown.ambushed")
                ]

    screen zombies_downtown():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.21, 0.37)
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
                    ground "zombie_tap_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_tap_a half"
            else: 
                ground "zombie_tap_a dead"

        imagemap:
            pos (0.54, 0.40)
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
                    ground "zombie_tap_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_tap_b half"
            else: 
                ground "zombie_tap_b dead"

        imagemap:
            pos (0.4, 0.37)
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
                ground "zombie_tap_c full"
            else: 
                ground "zombie_tap_c dead"

    # Sprites
    image bg street_downtown_night:
        "bg street_downtown_night_1.png"
        pause 0.25
        "bg street_downtown_night_2.png"
        pause 0.25
        repeat

    image bg street_downtown_night_z:
        "bg street_downtown_night_z_1.png"
        pause 0.25
        "bg street_downtown_night_z_2.png"
        pause 0.25
        repeat

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "downtown" not in progress["zombies"]["clear"]:
            scene bg street_downtown_night_z
            show screen zombies_downtown_timer
            show screen zombies_downtown
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
            scene bg street_downtown_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_downtown_eve
    else:
        scene bg street_downtown
    with fade
    call screen interact_downtown

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
        hide screen zombies_downtown_timer
        hide screen zombies_downtown
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
        $ progress["zombies"]["clear"].append("downtown")
        hide screen zombies_downtown_timer
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
        call screen interact_downtown