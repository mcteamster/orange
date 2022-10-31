label storeroom:
    # Screens
    screen interact_storeroom():
        frame:
            pos (0, 0)
            textbutton "tap_alley":
                xysize (0.1, 1.0)
                action [
                    Jump("tap_alley")
                ]
        frame:
            pos (0.32, 0.04)
            textbutton "toilet":
                xysize (0.05, 0.63)
                action [
                    Jump("toilet")
                ]
        frame:
            pos (0.69, 0)
            textbutton "tavern":
                xysize (0.14, 0.94)
                action [
                    Jump("tavern")
                ]

    # Script
    scene bg tap_storeroom with fade
    call screen interact_storeroom
    
label toilet:
    # Screens
    screen interact_toilet():
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0, 0.5)
                textbutton "king_talk":
                    xysize (0.2, 0.5)
                    action [
                        Call("toilet.talk")
                    ]
        frame:
            pos (0.67, 0.11)
            textbutton "storeroom":
                xysize (0.155, 0.595)
                action [
                    Jump("storeroom")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg tap_toilet_night with fade
    else:
        scene bg tap_toilet with fade
        king "What am I doing with my life?{w=2}{nw}"
    call screen interact_toilet

    label .talk:
        # Script
        if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
            jump toilet.quest
        king "An Orange Narwhal? Yeah, I can help you find it."
        king "But first I need a drink. Can you shout me a {i}beer{/i}?"
        king "Also, I'm really hungry. Do you have some food?"
        king "I'm in the mood for {i}noodles{/i}."
        king "Be a sport and grab me some {i}beer{/i} and {i}noodles{/i}, would ya?"
        king "And also a big bag of {i}cash{/i}... For the bus."
        king "And then I'll help you find your narwhal."
        call screen interact_toilet
    
    label .quest:
        # Screens
        screen interact_toilet_quest():
            button action NullAction()
            frame:
                pos (0.49, 0.25)
                textbutton "take_genie":
                    xysize (0.06, 0.27)
                    action [
                        Hide(),
                        Call("final_quest_start")
                    ]

        # Script
        scene bg plain_white with fade
        $ inventory["beer"]["active"] = False
        $ inventory["cash"]["active"] = False
        $ inventory["noodles"]["active"] = False
        scene bg tap_king with fade
        king "Mmm. This is exactly what I needed. Thanks man."
        king "Oh yeah, that's right. The Orange Narwhal."
        scene bg tap_king_offer
        show screen interact_toilet_quest
        king "Here, this should help you find it."
        pause

label final_quest_start:
    # Screens
    screen interact_final_quest_start():
        frame:
            pos (0.67, 0.11)
            textbutton "storeroom":
                xysize (0.155, 0.595)
                action [
                    Jump("final_quest_start.talk")
                ]

    # Script
    $ inventory["genie"]["active"] = True
    $ inventory["genie"]["highlight"] = True
    scene bg tap_toilet_final with fade
    call screen interact_final_quest_start

    label .talk:
        king "Don't run away with it! Spark it up here."
        call screen interact_final_quest_start

label final_quest_cutscene:
    # Screens
    screen interact_final_quest_cutscene():
        frame:
            pos (0.44, 0.42)
            textbutton "shackles":
                xysize (0.145, 0.04)
                action [
                    Jump("final_quest_cutscene.freed")
                ]

    # Script
    $ inventory["genie"]["active"] = False
    $ inventory["genie"]["highlight"] = False
    scene bg tap_toilet_final
    show genie_bottle zorder 1 with None:
        align (0.5, 0.5)
        pos (0.4, 0.85)
    show genie_plume:
        align (0.5, 0.5)
        pos (0.5, 0.42)
    show genie_clouds:
        align (0.5, 0.5)
        pos (0.5, 0.5)
        alpha 0.0
        pause 0.25
        linear 0.5 alpha 1.0 yalign 0.4
        linear 0.5 alpha 0.0 yalign 0.3
    with wipeup
    genie "Hey mon."
    genie "You want to find the Orange Narwhal?"
    genie "Your wish is my command."
    genie "But I cannot use my powers with these shackles on."
    genie "Set me free and I shall grant your wish."
    show genie_shackles:
        align (0.5, 0.5)
        pos (0.5155, 0.445)
    call screen interact_final_quest_cutscene

    label .freed:
        # Screens
        screen interact_final_quest_cutscene_freed():
            frame:
                pos (0.46, 0.51)
                textbutton "take_key":
                    xysize (0.07, 0.08)
                    action [
                        Jump("final_quest_cutscene.taken")
                    ]

        # Sprites
        image genie_shackle_left:
            "endgame/genie_shackle.png"
            align (0.5, 0.5)
            pos (0.59, 0.37)
            rotate 0
            alpha 1.0
            pause 0.5
            linear 0.5 rotate -90 ypos 0.67 alpha 0.0

        image genie_shackle_right:
            "endgame/genie_shackle.png"
            align (0.5, 0.5)
            pos (0.4, 0.67)
            rotate 0
            alpha 1.0
            pause 0.5
            linear 0.5 rotate -90 ypos 1.0 alpha 0.0

        image genie_hand_left:
            "endgame/genie_hand_glow.png"
            align (0.5, 0.5)
            pos (0.22, 0.43)
            alpha 0.0
            linear 4.0 alpha 1.0
        
        image genie_hand_right:
            "endgame/genie_hand_glow.png"
            align (0.5, 0.5)
            pos (0.78, 0.43)
            alpha 0.0
            linear 4.0 alpha 1.0

        image urinals:
            "endgame/toilet_urinals.png"
            align (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
            rotate 0
            linear 1.0 zoom 0.95 rotate 5
            linear 1.0 zoom 0.9 rotate -5
            linear 0.75 zoom 0.85 rotate 5
            linear 0.75 zoom 0.8 rotate -5
            linear 0.5 zoom 0.75 rotate 5
            linear 0.5 zoom 0.7 rotate -5
            linear 0.25 zoom 0.65 rotate 5
            linear 0.25 zoom 0.6 rotate 0

        image darkness:
            "bg plain_black"
            alpha 0.0
            linear 5.0 alpha 1.0

        image lightning:
            "bg plain_white"
            alpha 0.0
            block:
                pause 0.8
                linear 0.1 alpha 0.5
                linear 0.1 alpha 0.0
                repeat 4

        # Script
        scene bg plain_charcoal
        show genie_arm as genie_left:
            align (0.5, 0.5)
            pos (0.5, 0.0)
        show genie_shackle_left
        show genie_arm as genie_right:
            align (0.5, 0.5)
            pos (0.3, 0.3)
        show genie_shackle_right
        with fade
        pause 1.0
        scene bg plain_white with fade
        scene bg plain_charcoal
        show urinals
        show darkness
        show lightning
        show genie_unleashed:
            align (0.5, 0.5)
            pos (0.5, 0.6)
        show genie_unleashed_eyes:
            align (0.5, 0.5)
            pos (0.504, 0.258)
            alpha 1.0
            linear 4.0 alpha 0.0
        show genie_hand_left
        show genie_hand_right
        with fade
        show cutscene_top enter onlayer screens zorder 101
        show cutscene_bottom enter onlayer screens zorder 101
        genie "AT LAST! I AM FREE!{w=2}{nw}"
        genie "BEHOLD MY POWER AS I TURN THIS WORLD TO ASHES!{w=2}{nw}"
        scene bg plain_charcoal
        show toilet_urinals:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            zoom 1
        show genie_offering:
            align (0.5, 0.5)
            pos (0.48, 0.7)
        show key_glow:
            align (0.5, 0.5)
            pos (0.5, 0.56)
        show cutscene_top exit onlayer screens zorder 101
        show cutscene_bottom exit onlayer screens zorder 101
        genie "Oh, I nearly forgot. The Orange Narwhal is in Cliefwood."
        genie "You'll need this {i}key{/i} to get inside."
        call screen interact_final_quest_cutscene_freed
        pause
    
    label .taken:
        # Sprites
        image rocket:
            "endgame/genie_rocket.png"
            align (0.5, 0.5)
            pos (0.515, 0.5)
            zoom 1
            easeout 0.5 zoom 1.5 ypos -1.0 

        # Script
        hide key_glow
        $ inventory["key"]["active"] = True
        genie "Alright. Where was I?"
        genie "Oh yeah, that's right. The apocalypse."
        scene bg tap_toilet_final
        show genie_bottle zorder 1:
            align (0.5, 0.5)
            pos (0.4, 0.85)
        show genie_plume:
            align (0.5, 0.5)
            pos (0.5, 0.42)
        with fade
        pause 1.0
        hide genie_plume
        show rocket
        show genie_bottle:
            rotate 0
            linear 0.25 rotate 90 pos (0.43, 0.89)
        pause 0.5
        play audio "audio/explosion.wav"
        show toilet_roof_cloud:
            align (0.5, 0.5)
            pos (0.5, 0)
            zoom 1
            alpha 1.0
            linear 0.25 zoom 1.5
            linear 0.75 alpha 0.0 ypos -0.5
        show toilet_roof_explosion zorder 1:
            align (0.5, 0.5)
            pos (0.5, 0)
            zoom 1
            alpha 1.0
            linear 0.1 zoom 1.5
            alpha 0.0
        pause 1.0

    label .skyline:
        # Spirtes
        image dusk:
            "bg plain_orange"
            alpha 1.0
            linear 3.0 alpha 0.0
        
        # Script
        scene bg plain_navy
        show screen help_button
        show cutscene_top enter onlayer screens zorder 101
        show cutscene_bottom enter onlayer screens zorder 101
        hide screen hud_inventory
        show dusk
        show skyline_hills:
            align (0.5, 0.5)
            pos (0.5, 0.5)
        show skyline_distant:
            align (0.5, 0.5)
            pos (0.55, 0.5)
            linear 4.0 xpos 0.45
        show skyline_close:
            align (0.5, 1.0)
            pos (0.7, 1.0)
            linear 4.0 xpos 0.5
        with fade
        pause 3.0

    label .park:
        # Script
        scene bg plain_navy
        show park_background:
            align (0.5, 0.5)
            pos (0.5, 0.7)
            linear 4.0 ypos 0.6
        show park_foreground:
            align (0.5, 0.5)
            pos (0.6, 0.5)
            linear 4.0 ypos 0.3
        pause 4.0

    label .rising:
        # Script
        scene bg plain_navy
        show rising_ground
        show rising_buildings:
            align (0.0, 0.5)
            pos (0.0, 0.1)
            linear 4.0 xpos -0.05
        show rising_river:
            align (0.0, 0.5)
            pos (0.0, 0.3)
            linear 4.0 xpos -0.1
        show rising_tree:
            align (0.5, 0.5)
            pos (1.0, 0.2)
            linear 4.0 xpos 0.8
        show rising_dirt_hole:
            align (0.0, 0.0)
            pos (0.5, 0.8)
            alpha 0.0
            pause 2
            alpha 1.0
            linear 2 xpos 0.4
        show rising_zombie_hand:
            align (0.0, 0.0)
            pos (0.48, 0.8)
            alpha 0.0
            pause 2
            alpha 1.0
            linear 2 pos (0.38, 0.2)
        show rising_front_grass:
            align (0.0, 0.0)
            pos (0.45, 0.82)
            alpha 0.0
            pause 2
            alpha 1.0
            linear 2 xpos 0.35
        pause 5.0

    label .horde:
        # Script
        scene bg plain_navy
        show horde_buildings:
            align (0.5, 0.0)
            pos (0.5, 0.15)
        show horde_background:
            align (0.5, 0.65)
            pos (0.6, 1.0)
            linear 4.0 xpos 0.5
        show horde_foreground:
            align (0.5, 0.7)
            pos (0.65, 1.0)
            linear 4.0 xpos 0.5
        pause 4.0

    label .bank:
        # Script
        scene bg plain_navy
        show bank_background:
            align (0.5, 0.5)
            pos (0.6, 0.3)
            linear 4.0 xpos 0.55
        show bank_foreground:
            align (0.5, 0.5)
            pos (0.65, 0.75)
            linear 4.0 xpos 0.55
        pause 4.0

    label .dock:
        # Script
        scene bg plain_navy
        show dock_background:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            linear 4.0 xpos 0.45
        show dock_flank:
            align (0.5, 0.5)
            pos (0.3, 0.8)
            linear 4.0 xpos 0.2
        show dock_attack:
            align (0.5, 0.5)
            pos (0.7, 0.7)
            linear 4.0 xpos 0.55
        show dock_foreground:
            align (0.5, 0.0)
            pos (0.9, 0.6)
            linear 4.0 xpos 0.7
        pause 4.0

    label .police:
        # Script
        scene bg plain_navy
        show police_background:
            align (0.0, 0.5)
            pos (0.0, 0.57)
            linear 4.0 xpos -0.05
        show police_foreground:
            align (0.5, 0.5)
            pos (0.6, 0.8)
            linear 4.0 xpos 0.5
        pause 4.0

    label .tap:
        # Script
        scene bg plain_navy
        show tap_background:
            align (0.0, 0.5)
            pos (0.0, 0.5)
            linear 4.0 xpos -0.05
        show tap_attack:
            align (0.5, 0.5)
            pos (0.8, 0.5)
            linear 4.0 xpos 0.7
        show tap_foreground:
            align (0.5, 0.5)
            pos (0.1, 0.8)
            linear 4.0 xpos -0.1
        pause 4.0

    label .bus:
        # Script
        scene bg plain_navy
        show bus_background:
            align (0.0, 1.0)
            pos (0.0, 1.0)
            linear 4.0 xpos -0.05
        show bus_driver_crash:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            linear 4.0 xpos 0.4
        show bus_window_shards:
            align (0.5, 0.5)
            pos (0.65, 0.5)
            linear 4.0 xpos 0.5
        show bus_foreground:
            align (0.0, 0.5)
            pos (0.0, 0.75)
            linear 4.0 xpos -0.2
        pause 4.0

    label .lock_and_load:
        # Settings
        $ progress["night"] = True
        if inventory["shotgun"]["active"]:
            if inventory["sawnoff"]["active"]:
                $ lock_and_load_image = "lock_and_load_king"
            else:
                $ lock_and_load_image = "lock_and_load_shotgun"
        else:
            $ lock_and_load_image = "lock_and_load_sawnoff"

        # Script
        show screen help_button
        scene bg endgame_lock_and_load
        show expression lock_and_load_image:
            align (0.0, 0.5)
            pos (0.33, 0.9)
        with fade
        show screen hud_inventory
        show cutscene_top exit onlayer screens
        show cutscene_bottom exit onlayer screens
        pause 1.0
        "Heck.{w=2}{nw}"
        pause 1.0
        "{i}Click to continue...{/i}"
        jump downtown