label station:
    # Settings
    if "station" not in progress["zombies"]["clear"]:
        $ zombies = {
            "total": 6,
            "z1": 2,
            "z2": 2,
            "z3": 2,
        }
    $ active_weapon = "shotgun" if inventory["shotgun"]["active"] else "sawnoff"
    $ shoot_command = active_weapon+".shoot"

    # Screens
    screen interact_station():
        frame:
            pos (0.0, 0.8)
            textbutton "downtown":
                xysize (1.0, 0.2)
                action [
                    Hide("zombies_station"),
                    Jump("downtown")
                ]
        frame:
            pos (0.1, 0.22)
            textbutton "jail":
                xysize (0.095, 0.6)
                action [
                    Hide("zombies_station"),
                    Jump("jail")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.34, 0.31)
                textbutton "booth":
                    xysize (0.315, 0.2)
                    action [
                        Jump("booth")
                    ]
            if inventory["shotgun"]["active"]:
                frame:
                    pos (0.25, 0.345)
                    textbutton "bounty":
                        xysize (0.055, 0.13)
                        action [
                            Jump("bounty")
                        ]

    screen zombies_station_timer():
        timer 0.1:
            repeat True
            if zombies["total"] <= 0:
                action [
                    Hide(),
                    Jump("station.clear")
                ]
            else:
                action NullAction()
        timer 9:
            if zombies["total"] > 0:
                action [
                    Hide(),
                    Jump("station.ambushed")
                ]

    screen zombies_station():
        button:
            if zombies["total"] > 0:
                action [
                    Call(shoot_command, "zombies", None, zombies, from_current=True)
                ]
            else:
                action NullAction()
        imagemap:
            pos (0.51, 0.38)
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
                    ground "zombie_police_b full"
                elif zombies["z2"] == 1:
                    ground "zombie_police_b half"
            else: 
                ground "zombie_police_b dead"
        imagemap:
            pos (0.28, 0.36)
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
                    ground "zombie_police_a full"
                elif zombies["z1"] == 1:
                    ground "zombie_police_a half"
            else: 
                ground "zombie_police_a dead"
        imagemap:
            pos (0.4, 0.30)
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
                    ground "zombie_police_c full"
                elif zombies["z3"] == 1:
                    ground "zombie_police_c half"
            else: 
                ground "zombie_police_c dead"

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        if "station" not in progress["zombies"]["clear"]:
            scene bg police_station_night_z
            show screen zombies_station_timer
            show screen zombies_station
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
            scene bg police_station_night
    elif inventory["shotgun"]["active"]:
        scene bg police_station_no_bounty
    else:
        scene bg police_station
    with fade

    if (progress["night"] or inventory["key"]["active"]) == False:
        if progress["quests"]["clowns"]["complete"] or (inventory["sawnoff"]["active"] and inventory["cash"]["active"]):
            officer "Hey! He's one of the clowns from the bank robbery!{w=2}{nw}"
            show arrest_officer_left
            show arrest_officer_right
            pause 1.0
            jump arrested
        elif inventory["bomb"]["active"]:
            officer "Oh my god! He's got a {i}bomb{/i}!{w=2}{nw}"
            show arrest_officer_left
            show arrest_officer_right
            pause 1.0
            jump arrested
    call screen interact_station

    label .ambushed:
        play audio "audio/bite.wav"
        show zombie_ambush onlayer screens zorder 1:
            align (0.5, 0.5)
            pos (0.5, 1.5)
            linear 0.25 ypos 0.66
        pause 1.0
        scene bg plain_white
        hide zombie_ambush onlayer screens
        hide screen zombies_station_timer
        hide screen zombies_station
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        with fade
        jump horde

    label .clear:
        $ progress["zombies"]["clear"].append("station")
        hide screen zombies_station_timer
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
        call screen interact_station

label booth:
    # Screens
    screen interact_booth():
        frame:
            pos (0.0, 0.8)
            textbutton "station":
                xysize (1.0, 0.2)
                action [
                    Jump("station")
                ]
        frame:
            pos (0.41, 0.17)
            textbutton "booth_talk":
                xysize (0.175, 0.5)
                action [
                    Jump("booth.talk")
                ]

    # Script
    scene bg police_booth with fade
    call screen interact_booth

    label .talk:
        if (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]):
            officer "Thanks again for your help. You've made the city a safer place.{w=2}{nw}"
        elif inventory["radio"]["active"]:
            officer "Thanks for volunteering."
            officer "All you have to do is call us from their headquarters."
            officer "Then we'll come to you and take care of the Ninjas."
            officer "You're helping us make this city a safer place."
        elif (progress["quests"]["ninjas"]["complete"] or inventory["noodles"]["active"]):
            jump booth.quest
        else:
            officer "Be careful. There are criminals all over this town."
            officer "Keep an eye out for Ninjas. We offer a big reward if you find them."
        call screen interact_booth

    label .quest:
        screen interact_booth_talk():
            button action NullAction()
            frame:
                pos (0.0, 0.8)
                textbutton "station":
                    xysize (1.0, 0.2)
                    action [
                        Hide(),
                        Jump("station")
                    ]
            frame:
                pos (0.63, 0.46)
                textbutton "take_radio":
                    xysize (0.1, 0.15)
                    action [
                        Hide(),
                        Jump("booth.accepted")
                    ]

        $ progress["quests"]["police"]["offered"] = True
        officer "Ninjas have been terrorising the city lately."
        officer "We're trying to track them down, but they're very elusive."
        officer "If you know the whereabouts of their base of operations, we'd love your help."
        scene bg police_booth_offer
        show screen interact_booth_talk
        officer "If you'd like to help us out, take this Police {i}radio{/i}."
        pause

    label .accepted:
        $ progress["quests"]["police"]["accepted"] = True
        $ inventory["radio"]["active"] = True
        scene bg police_booth
        jump booth.talk


label bounty:
    # Screens
    screen interact_bounty():
        frame:
            pos (0.0, 0.8)
            textbutton "station":
                xysize (1.0, 0.2)
                action [
                    Jump("station")
                ]

    # Script
    scene bg police_bounty with fade
    "I should keep an eye out for Ninjas. I could do with the {i}cash{/i}."
    call screen interact_bounty