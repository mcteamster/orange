label roof:
    # Screens
    screen interact_roof():
        frame:
            pos (0.0, 0.8)
            textbutton "jail":
                xysize (1.0, 0.2)
                action [
                    Jump("jail")
                ]
        if (progress["night"] or inventory["key"]["active"]):
            if (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]):
                frame:
                    pos (0.27, 0.1)
                    textbutton "helicopter":
                        xysize (0.56, 0.45)
                        action [
                            Jump("helicopter")
                        ]
        else:
            frame:
                pos (0.115, 0.27)
                textbutton "talk_officer":
                    xysize (0.11, 0.67)
                    action [
                        Jump("roof.talk")
                    ]

    # Sprites
    image police_helicopter:
        "police/police_helicopter.png"
        align (0.5, 0.5)
        pos (0.55, 0.33)

    image police_officer_helicopter:
        "police/police_guard.png"
        align (0.5, 0.5)
        pos (0.46, 0.41)
        zoom 0.66

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg police_roof_night
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg police_roof_eve
    else:
        scene bg police_roof
    if (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]):
        show police_helicopter
        show police_officer_helicopter
    with fade
    call screen interact_roof

    label .talk:
        officer "Sorry, champ. The helicopter is for Police use only."
        call screen interact_roof

label helicopter:
    # Script
    hide screen help_button

    label .boarding:
        scene bg plain_white with fade
        show cutscene_top enter onlayer screens zorder 101
        show cutscene_bottom enter onlayer screens zorder 101
        scene crash_boarding
        show boarding_officer:
            align (0.5, 1.0)
            pos (0.42, 1.0)
        with fade
        officer "You made it! Quick, get in!{w=2}{nw}"
    
    label .running:
        image crash_skyline:
            "crash/running_buildings.png"
            align (1.0, 0.25)
            pos (1.0, 0.0)
            linear 2.0 xpos 1.5

        image player_legs:
            align (0.5, 0.0)
            pos (0.5, -0.2)
            "crash/running_player_legs_1.png"
            pause 0.1
            "crash/running_player_legs_2.png"
            pause 0.1
            "crash/running_player_legs_3.png"
            pause 0.1
            "crash/running_player_legs_4.png"
            pause 0.1
            repeat 5

        image zombie_legs:
            align (0.5, 0.0)
            pos (0.5, -0.2)
            "crash/running_zombie_legs_1.png"
            pause 0.1
            "crash/running_zombie_legs_2.png"
            pause 0.1
            "crash/running_zombie_legs_3.png"
            pause 0.1
            "crash/running_zombie_legs_4.png"
            pause 0.1
            repeat 5

        scene bg plain_navy
        show running_ground zorder 1
        show crash_skyline as player_skyline
        show player_legs zorder 1
        pause 2.0
        hide player_legs
        show crash_skyline as zombie_skyline
        show zombie_legs zorder 1
        pause 2.0

    label .shooting:
        scene crash_boarding
        show crash_muzzle_flash:
            align (0.5, 1.0)
            pos (0.7425, 0.5325)
            block:
                alpha 1.0
                pause 0.05
                alpha 0.5
                pause 0.05
                repeat
        show shooting_officer:
            align (0.5, 1.0)
            pos (0.42, 1.1)
        if inventory["sawnoff"]["active"]:
            show shooting_king_dash:
                align (0.5, 1.0)
                pos (1.0, 0.95)
                linear 0.25 xpos -0.2
        show shooting_player_dash:
            align (0.5, 1.0)
            pos (1.2, 1.1)
            linear 0.25 xpos -0.2
        officer "BURN IN HECK YOU MOTHERFLIPPERS!{w=2}{nw}"

    label .sitting:
        scene sitting_background
        if inventory["sawnoff"]["active"]:
            show shooting_king_dash:
                align (0.5, 1.0)
                pos (0.55, 1.0)
                linear 1.0 xpos 0.3
        show sitting_player:
            align (0.5, 1.0)
            pos (0.75, 1.0)
            linear 1.0 xpos 0.5
        show sitting_foreground:
            align (0.5, 1.0)
            pos (0.5, 1.12)
        pause 1.0
        "Get us out of here!{w=2}{nw}"

    label .takeoff:
        scene takeoff_background
        show takeoff_blades:
            align (0.5, 0.5)
            pos (0.5, 0.42)
            block:
                linear 0.05 rotate 0 zoom 1
                linear 0.05 rotate -3 zoom 3
                repeat
        pause 2.0

    label .liftoff:
        scene liftoff_background
        show liftoff_zombies:
            align (0.5, 1.0)
            pos (0.5, 0.5)
            zoom 0.25
            linear 2.0 zoom 1.0 ypos 1.1
        show liftoff_helicopter:
            align (1.0, 0.5)
            pos (1.05, 0.75)
            pause 0.5
            linear 1.5 ypos -1.0
        pause 2.5

    label .leaving:
        scene bg plain_navy
        show leaving_background:
            align (0.5, 0.5)
            pos (0.5, 0.9)
        show leaving_helicopter:
            align (0.5, 0.5)
            pos (0.5, 0.4)
            linear 1.0 pos (0.25, 0.25)
        show leaving_zombies:
            align (0.5, 0.5)
            pos (0.75, 0.65)
            linear 1.0 pos (0.5, 0.65)
        show leaving_foreground:
            align (1.0, 0.0)
            pos (1.1, 0.7)
        pause 1.0

    label .jumping:
        scene bg plain_navy
        show leaving_background:
            align (0.5, 0.5)
            pos (0.5, 1.0)
        show jumping_helicopter:
            align (0.5, 1.0)
            pos (0.5, 0.5)
            linear 0.5 pos (0.4, 0.35)
        show jumping_zombie:
            align (0.0, 0.0)
            pos (0.75, 0.5)
            linear 0.5 pos (0.39, 0.25)
        pause 0.75

    label .swaying:
        scene bg plain_navy
        show leaving_background:
            align (0.5, 0.5)
            pos (0.5, 1.1)
        show swaying_helicopter:
            align (0.5, 0.5)
            pos (0.75, 0.75)
            rotate 0
            linear 0.5 pos (0.65, 0.65) rotate 5
            linear 0.5 pos (0.55, 0.55) rotate 0
            linear 0.5 pos (0.45, 0.45) rotate -5
            linear 0.5 pos (0.35, 0.35) rotate 0
        pause 2.0

    label .pilot:
        scene bg plain_charcoal
        show pilot_background:
            align (0.5, 1.0)
            pos (0.35, 1.25)
        show pilot_hand:
            align (0.5, 0.5)
            pos (1.2, 0.35)
            pause 0.5
            linear 0.25 pos (0.9, 0.35)
        show pilot_shards:
            align (0.5, 0.5)
            pos (1.2, 0.35)
            alpha 1.0
            pause 0.5
            linear 0.25 pos (0.9, 0.35) alpha 0.0
        show pilot_foreground:
            align (0.5, 0.5)
            pos (0.71, 0.75)
        pause 0.75
        show pilot_blood:
            align (0.5, 0.5)
            pos (0.8, 0.36)
            linear 0.25 zoom 2
        pause 1.0

    label .spiralling:
        # Spirtes 
        image spinning_helicopter:
            "crash/spinning_helicopter_right.png"
            pause 0.1
            "crash/spinning_helicopter_front.png"
            pause 0.1
            "crash/spinning_helicopter_left.png"
            pause 0.1
            "crash/spinning_helicopter_back.png"
            pause 0.1
            repeat

        image spiralling_smoke:
            "crash/spiralling_smoke_1.png"
            pause 0.1
            "crash/spiralling_smoke_2.png"
            pause 0.1
            repeat

        # Script
        scene bg plain_navy
        show spiralling_background:
            align (1.0, 1.0)
            pos (1.0, 1.25)
            linear 3.0 xpos 2.0
        show spiralling_smoke:
            align (0.0, 1.0)
            pos (0.5, 0.5)
        show spinning_helicopter:
            align (0.5, 0.5)
            pos (0.5, 0.5)
        pause 3.0

    label .cockpit:
        scene bg plain_navy
        show spiralling_background:
            align (0.0, 1.0)
            pos (0.0, 1.0)
            linear 2.0 xpos -1.0
        show cockpit_foreground:
            align (0.5, 0.5)
            pos (0.5, 0.75)
        pause 2.0

    label .building:
        scene building_background
        show building_intact:
            align (1.0, 0.5)
            pos (1.0, 0.75)
        show building_hole:
            align (1.0, 0.5)
            pos (1.0, 0.75)
        show spinning_helicopter:
            align (0.5, 0.5)
            pos (-0.5, -0.5)
            rotate 10
            linear 1.0 pos (0.65, 0.5)
        pause 1.0
        hide building_intact
        play audio "audio/explosion.wav"
        show spinning_helicopter:
            align (0.5, 0.5)
            pos (0.65, 0.5)
            rotate -10
            linear 1.0 pos (-0.5, 1.5)
        show explosion_smoke:
            align (0.5, 0.5)
            pos (0.66, 0.55)
            zoom 2.0
            alpha 1.0
            linear 1.0 zoom 3 ypos 0.35 alpha 0.0
        show explosion_flash:
            align (0.5, 0.5)
            pos (0.66, 0.55)
            zoom 2.0
            alpha 1.0
            linear 0.25 zoom 3 alpha 0.0
        pause 1.0

    label .descent:
        scene bg plain_navy
        show descent_background:
            align (0.5, 1.0)
            pos (0.5, 1.3)
            linear 2.0 ypos 1.2
        show descent_treeline:
            align (0.5, 1.0)
            pos (0.5, 1.5)
            linear 2.0 ypos 1.25
        show spinning_helicopter:
            align (0.5, 0.5)
            pos (1.0, 0.0)
            rotate -10
            linear 2.0 pos (0.5, 0.5)
        show descent_tree zorder 1:
            align (0.5, 0.5)
            pos (0.0, 3.0)
            rotate 0
            linear 2.0 pos (0.5, 2.0)
            linear 1.0 rotate -90
        pause 2.0
        hide spinning_helicopter
        show rolling_helicopter:
            align (0.5, 0.5)
            pos (0.5, 0.75)
            rotate -10
            linear 1.0 pos (-0.25, 1.0) rotate -730
        show rolling_helicopter_blades:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            rotate -10
            linear 0.5 pos (-0.25, 0.0) rotate -20
        pause 1.0

    label .rolling_inside:
        scene bg plain_navy
        show rolling_inside_background:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            rotate 0
            linear 2.0 rotate -540
        show cockpit_foreground:
            align (0.5, 0.5)
            pos (0.5, 0.75)
        pause 2.0

    label .rolling_outside:
        scene rolling_outside_background
        show rolling_outside_buildings:
            align (1.0, 0.5)
            pos (1.25, 0.25)
            linear 2.0 xpos 2.0
        show rolling_outside_treeline:
            align (1.0, 0.5)
            pos (1.25, 0.25)
            linear 2.0 xpos 3.0
        show rolling_helicopter:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 3.0
            linear 2.0 rotate -1080
        pause 2.0

    label .gazebo:
        scene gazebo_background
        show rolling_helicopter:
            align (0.5, 0.5)
            pos (1.0, 0.15)
            rotate 0
            linear 1.0 rotate -540 pos (0.5, 0.45)
        show gazebo_foreground zorder 1
        pause 1.0
        hide rolling_helicopter
        show bg park_gazebo_northeast_night_z
        play audio "audio/explosion.wav"
        show explosion_smoke:
            align (0.5, 0.5)
            pos (0.5, 0.4)
            zoom 2.0
            alpha 1.0
            linear 1.0 zoom 3 ypos 0.35 alpha 0.0
        show explosion_flash:
            align (0.5, 0.5)
            pos (0.5, 0.4)
            zoom 2.0
            alpha 1.0
            linear 0.25 zoom 3 alpha 0.0
        pause 3.0

    label .lock_and_load:
        scene bg plain_black with fade
        pause 0.5
        if inventory["sawnoff"]["active"]:
            scene crash_lock_and_load_king
        else:
            scene crash_lock_and_load
        with fade
        show screen help_button
        show cutscene_top exit onlayer screens
        show cutscene_bottom exit onlayer screens
        pause 1.0
        "Heck.{w=2}{nw}"
        "{i}Click to continue...{/i}"
        jump gazebo_northeast