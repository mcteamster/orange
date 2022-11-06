label temple:
    # Screens
    screen interact_temple():
        frame:
            pos (0.0, 0.8)
            textbutton "temple_path":
                xysize (1.0, 0.2)
                action [
                    Jump("temple_path")
                ]
        frame:
            pos (0.47, 0.47)
            textbutton "talk_monk":
                xysize (0.055, 0.35)
                action [
                    Jump("temple.talk")
                ]

    # Sprites
    image temple_monk:
        "ninja/monk.png"
        align (0.5, 0.5)
        pos (0.5, 0.65)

    image alcove_ninja_1:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.1, 0.2)

    image alcove_ninja_2:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.22, 0.27)
        zoom 0.66

    image alcove_ninja_3:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.26, 0.29)
        zoom 0.66

    image alcove_ninja_4:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.34, 0.37)
        zoom 0.33

    image alcove_ninja_5:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.66, 0.37)
        zoom 0.33

    image alcove_ninja_6:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.74, 0.29)
        zoom 0.66

    image alcove_ninja_7:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.78, 0.27)
        zoom 0.66

    image alcove_ninja_8:
        "ninja/alcove_ninja.png"
        align (0.5, 0.5)
        pos (0.9, 0.2)

    # Scripts
    scene bg hideout_temple
    show temple_interior zorder 1
    show temple_roof_sky:
        align (0.5, 0.04)
        pos (0.5, 0)
        alpha 1.0
    show temple_roof_shards:
        align (0.5, 0)
        pos (0.5, 0)
        alpha 1.0
    show temple_roof:
        align (0.5, 0.04)
        pos (0.5, 0)
        alpha 1.0
    show temple_monk zorder 2
    show alcove_ninja_4
    show alcove_ninja_5
    show alcove_ninja_3
    show alcove_ninja_6
    show alcove_ninja_2
    show alcove_ninja_7
    show alcove_ninja_1
    show alcove_ninja_8
    with fade
    if inventory["radio"]["active"]:
        $ inventory["radio"]["highlight"] = True
    xiao "Welcome to our temple.{w=2}{nw}"
    call screen interact_temple

    label .talk:
        # Script
        xiao "No, there aren't any Narwhals here.{w=2}{nw}"
        xiao "Only worthy warriors are allowed here.{w=2}{nw}"
        call screen interact_temple

label temple_path:
    # Settings
    $ inventory["radio"]["highlight"] = False

    # Screens
    screen interact_temple_path():
        frame:
            pos (0.0, 0.8)
            textbutton "kitchen":
                xysize (1.0, 0.2)
                action [
                    Jump("kitchen")
                ]
        frame:
            pos (0.31, 0.06)
            textbutton "temple":
                xysize (0.38, 0.29)
                action [
                    Jump("temple")
                ]

    # Script
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg hideout_temple_path_eve
    else:
        scene bg hideout_temple_path
    with fade
    call screen interact_temple_path

label temple_raid:
    # Settings
    $ inventory["radio"]["highlight"] = False

    # Screens
    screen interact_temple_raid():
        button action NullAction()
        frame:
            pos (0.34, 0.13)
            textbutton "take_shotgun":
                xysize (0.08, 0.87)
                action [
                    Hide(),
                    SetDict(inventory["shotgun"], "active", True),
                    Jump("temple_raid_shootout")
                ]

    # Sprites
    transform flashing:
        pause 0.1
        alpha 1.0
        pause 0.1
        alpha 0.0

    image temple_raid_shotgun:
        "police/police_shotgun_offer.png"
        align (0.5, 0.5)
        pos (0.0, 0.65)
        linear 0.5 xpos 0.25

    image strike_1:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.3, -0.2)
        zoom 1
        rotate 0
        pause 0.3
        linear 0.5 ypos 0.25
        pause 1.0
        easeout 0.25 ypos 0.8 rotate 60
        rotate 0
        "police/strike_police_dead.png"
    image rappel_1:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.33, -0.2)
        pause 0.3
        linear 0.5 ypos 0.25
    image flash_1:
        "police/assault_flash.png"
        align (1.0, 1.0)
        pos (0.28, 0.22)
        alpha 0.0
        pause 0.8
        block:
            flashing
            repeat 5
    image blood_1:
        zoom 0
        pause 2.0
        "police/blood_puddle.png"
        align (0.5, 0.5)
        pos (0.3, 0.78)
        linear 1.0 zoom 1
    image shuriken_1:
        "ninja/shuriken.png"
        align (0.5, 0.5)
        pos (-0.1, 0.3)
        zoom 0.5
        alpha 0.0
        pause 1.5
        alpha 1.0
        linear 0.25 pos (0.3, 0.25)
        alpha 0.0

    image strike_2:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.39, -0.2)
        zoom 0.66
        pause 0.15
        linear 0.5 ypos 0.3
    image rappel_2:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.41, -0.2)
        pause 0.15
        linear 0.5 ypos 0.3
    image flash_2:
        "police/assault_flash.png"
        align (1.0, 1.0)
        pos (0.38, 0.28)
        zoom 0.66
        alpha 0.0
        pause 0.65
        block:
            flashing
            repeat

    image strike_3:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.45, -0.2)
        zoom 0.33
        linear 0.5 ypos 0.35
    image rappel_3:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.465, -0.2)
        linear 0.5 ypos 0.35
    image flash_3:
        "police/assault_flash.png"
        align (1.0, 1.0)
        pos (0.44, 0.34)
        zoom 0.33
        alpha 0.0
        pause 0.5
        block:
            flashing
            repeat

    image strike_4:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.55, -0.2)
        zoom 0.33
        xzoom -1
        linear 0.5 ypos 0.35
        pause 2.5
        easeout 0.1 ypos 0.5 rotate -30
        easeout 0.15 pos (0.51, 0.6) rotate -60
        rotate 0
        "police/strike_police_dead.png"
    image rappel_4:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.545, -0.2)
        linear 0.5 ypos 0.35
    image flash_4:
        "police/assault_flash.png"
        align (1.0, 1.0)
        pos (0.57, 0.34)
        zoom 0.33
        alpha 0.0
        pause 0.5
        block:
            flashing
            repeat 12
    image blood_4:
        zoom 0
        pause 3.25
        "police/blood_puddle.png"
        align (0.5, 0.5)
        pos (0.51, 0.595)
        linear 1.0 zoom 0.33
    image shuriken_4:
        "ninja/shuriken.png"
        align (0.5, 0.5)
        pos (-0.1, 0.8)
        zoom 1.0
        alpha 0.0
        pause 2.5
        alpha 1.0
        linear 0.5 pos (0.54, 0.35) zoom 0.25
        alpha 0.0

    image strike_5:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.61, -0.2)
        zoom 0.66
        xzoom -1
        pause 0.15
        linear 0.5 ypos 0.3
        easeout 0.25 ypos 0.7 rotate -60
        rotate 0
        "police/strike_police_dead.png"
    image rappel_5:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.59, -0.2)
        pause 0.15
        linear 0.5 ypos 0.3
    image blood_5:
        zoom 0
        pause 1.0
        "police/blood_puddle.png"
        align (0.5, 0.5)
        pos (0.61, 0.69)
        linear 1.0 zoom 0.66
    image shuriken_5:
        "ninja/shuriken.png"
        align (0.5, 0.5)
        pos (0.78, 0.23)
        zoom 0.5
        alpha 0.0
        pause 0.25
        alpha 1.0
        linear 0.25 pos (0.6, 0.2)
        alpha 0.0

    image strike_6:
        "police/strike_police.png"
        align (0.5, 0.5)
        pos (0.7, -0.2)
        zoom 1
        xzoom -1
        rotate 0
        pause 0.3
        linear 0.5 ypos 0.25
        pause 0.5
        "police/ninja_vs_police.png"
        pos (0.66, -0.1)
        xzoom 1
        linear 0.5 rotate 20
        "police/strike_police_dead_swing.png"
        rotate 10
        block:
            ease 2.0 rotate -30
            ease 2.0 rotate 10
            repeat
    image rappel_6:
        "police/rappel.png"
        align (1.0, 1.0)
        pos (0.67, -0.2)
        alpha 1.0
        pause 0.3
        linear 0.5 ypos 0.25
        pause 0.5
        alpha 0.0

    transform ninja_wound:
        "ninja/ninja_wounded.png"
        pause 0.25
        "ninja/alcove_ninja.png"

    # Script
    show temple_roof_shards:
        align (0.5, 0)
        pos (0.5, 0)
        ease 1.0 yalign 0.2 alpha 0.0
    show temple_roof:
        align (0.5, 0.04)
        pos (0.5, 0)
        ease 0.5 yalign 0.1 alpha 0.0
    show strike_3 zorder 2 # Back Left
    show rappel_3 zorder 1
    show flash_3 zorder 1
    show strike_4 zorder 2 # Back Right
    show shuriken_4 zorder 2
    show blood_4 zorder 1
    show rappel_4 zorder 1
    show flash_4 zorder 1
    show strike_2 zorder 2 # Middle Left
    show rappel_2 zorder 1
    show flash_2 zorder 1
    show strike_5 zorder 2 # Middle Right
    show shuriken_5 zorder 2
    show blood_5 zorder 1
    show rappel_5 zorder 1
    show strike_1 zorder 2 # Front Left
    show shuriken_1 zorder 2
    show blood_1 zorder 1
    show rappel_1 zorder 1
    show flash_1 zorder 1
    show strike_6 zorder 2 # Front Right
    show rappel_6 zorder 1
    pause 0.25
    play audio "audio/whoosh.wav"
    play music "audio/rifle.wav"
    pause 0.75
    show smoke_plume zorder 2
    show smoke_cloud zorder 2
    play audio "audio/pop.wav"
    show alcove_ninja_1:
        ninja_wound
        linear 1.0 ypos 0.7
    show alcove_ninja_2:
        zoom 0.66
        ninja_wound
        linear 1.0 xpos -0.1
    show alcove_ninja_3:
        linear 1.0 ypos 0.7
    show alcove_ninja_4:
        zoom 0.33
        ninja_wound
        linear 1.0 ypos 0.7
    show alcove_ninja_5:
        linear 1.0 xpos 1.1
    show alcove_ninja_6:
        zoom 0.66
        ninja_wound
        linear 1.0 ypos 0.7
    show alcove_ninja_7:
        pause 0.25
        linear 1.0 xpos 1.1
    hide temple_monk
    show assault_rifle zorder 2:
        alpha 0.0
        pause 0.75
        alpha 1.0
        align (0.5, 0.5)
        pos (0.62, 0.25)
        rotate 0
        easeout 0.25 ypos 0.8 rotate 180
    show alcove_ninja_8 zorder 2:
        "ninja/alcove_ninja_leap.png"
        alpha 1.0
        linear 0.25 pos (0.7, 0.25)      
        alpha 0.0
        pos (0.65, 0.25)
        pause 0.5
        "ninja/alcove_ninja_run.png"     
        alpha 1.0
        linear 1.0 pos (-0.2, 0.8)
    pause 0.5
    play audio "audio/whoosh.wav"
    pause 1.0
    play audio "audio/whoosh.wav"
    pause 2.5
    show temple_raid_shotgun zorder 3
    pause 0.5
    show screen interact_temple_raid
    officer "We're outnumbered! Here, take this and follow me! Hurry!"
    pause

label temple_raid_shootout:
    # Settings
    $ temple_raid_shootout_enemies = [
        "ninja_a1",
        "ninja_b2",
        "ninja_c1",
        "ninja_d2",
        "ninja_e3",
        "ninja_f3",
    ]
    $ temple_raid_shootout_time = 0

    # Screens
    screen temple_raid_timer():
        timer 1:
            repeat True
            action [
                SetVariable('temple_raid_shootout_time', temple_raid_shootout_time + 1),
            ]
        timer 15:
            if len(temple_raid_shootout_enemies) > 0:
                action Jump("temple_raid_shootout.beheaded")

    screen interact_temple_raid_shootout():
        button:
            if len(temple_raid_shootout_enemies) > 0:
                action [
                    Call("shotgun.shoot", "temple_raid_shootout", None, temple_raid_shootout_enemies, from_current=True)
                ]
            else:
                action NullAction()
        imagebutton:
            align (0.5, 0.5)
            pos (0.0675, 0.7)
            idle "ninja attacking_right_1"
            insensitive "ninja shot_center_right"
            selected_idle "ninja shot_center_right"
            selected "ninja_a1" not in temple_raid_shootout_enemies
            sensitive "ninja_a1" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_a1", temple_raid_shootout_enemies, from_current=True)
            ]
        imagebutton:
            align (0.5, 0.5)
            pos (0.4075, 0.7)
            idle "ninja attacking_right_2" 
            insensitive "ninja shot_center_right"
            selected_idle "ninja shot_center_right"
            selected "ninja_b2" not in temple_raid_shootout_enemies
            sensitive "ninja_b2" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_b2", temple_raid_shootout_enemies, from_current=True)
            ]
        imagebutton:
            align (0.5, 0.5)
            pos (0.5925, 0.7)
            idle "ninja attacking_left_1" 
            insensitive "ninja shot_center_left"
            selected_idle "ninja shot_center_left"
            selected "ninja_c1" not in temple_raid_shootout_enemies
            sensitive "ninja_c1" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_c1", temple_raid_shootout_enemies, from_current=True)
            ]
        imagebutton:
            align (0.5, 0.5)
            pos (0.2525, 0.22)
            idle "ninja attacking_left_2"
            insensitive "ninja shot_left"
            selected_idle "ninja shot_left"
            selected "ninja_d2" not in temple_raid_shootout_enemies
            sensitive "ninja_d2" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_d2", temple_raid_shootout_enemies, from_current=True)
            ]
        imagebutton:
            align (0.5, 0.5)
            pos (0.5925, 0.22)
            idle "ninja attacking_left_3" 
            insensitive "ninja shot_left"
            selected_idle "ninja shot_left"
            selected "ninja_e3" not in temple_raid_shootout_enemies
            sensitive "ninja_e3" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_e3", temple_raid_shootout_enemies, from_current=True)
            ]
        imagebutton:
            align (0.5, 0.5)
            pos (0.7475, 0.22)
            idle "ninja attacking_right_3" 
            insensitive "ninja shot_right"
            selected_idle "ninja shot_right"
            selected "ninja_f3" not in temple_raid_shootout_enemies
            sensitive "ninja_f3" in temple_raid_shootout_enemies
            action [
                Call("shotgun.shoot", "temple_raid_shootout", "ninja_f3", temple_raid_shootout_enemies, from_current=True)
            ]

    # Sprites
    image pillars:
        "ninja/temple_pillars.png"
        align (0.5, 0.5)
        pos (0.5, 0.45)

    # Script
    scene bg plain_white with fade
    scene bg hideout_temple_side
    show pillars onlayer screens zorder 1
    with fade
    stop music fadeout 0.5
    show screen interact_temple_raid_shootout
    show screen temple_raid_timer
    show shotgun equip onlayer screens zorder 50
    pause

    label .beheaded:
        # Sprites
        image ninja_ambush:
            "enemies/ninja_closeup.png"
            align (0.5, 0.5)
            pos (0.5, 2.0)
            linear 0.25 ypos 0.6

        # Script
        hide screen temple_raid_timer
        show bg hideout_temple_side
        show ninja_ambush onlayer screens zorder 1
        play audio "audio/sword.wav"
        pause 0.5
        jump beheaded_death

    label .clear:
        # Script
        jump monk_boss

label beheaded_death:
    # Script
    scene bg plain_brown
    hide ninja_ambush onlayer screens
    hide screen interact_temple_raid_shootout
    hide pillars onlayer screens
    hide shotgun onlayer screens
    hide shotgun_flash onlayer screens
    show beheaded_death:
        align (0.5, 0.5)
        pos (0.33, 0.5)
        zoom 1
        rotate 0
        linear 5.0 zoom 0.33 rotate -90
    with fade
    play audio "audio/bell.wav"
    pause 4.5
    $ inventory["shotgun"]["active"] = False
    jump game_over

label monk_boss:
    # Settings
    $ monk_health = 5
    $ monk_pos = {
        5: (0.5, 0.75),
        4: (0.15, 0.75),
        3: (0.5, 0.25),
        2: (0.85, 0.25),
        1: (0.5, 0.75),
        0: (0.5, 0.75),
    }
    $ dash_idle = {
        5: "null_dash",
        4: "horizontal_dash",
        3: "diagonal_dash",
        2: "horizontal_dash",
        1: "diagonal_dash",
        0: "null_dash",
    }
    $ dash_pos = {
        5: (0, 0),
        4: (0.325, 0.75),
        3: (0.325, 0.5),
        2: (0.675, 0.25),
        1: (0.675, 0.5),
        0: (0, 0),
    }

    # Screens
    screen interact_temple_raid_boss():
        button:
            if monk_health > 0:
                action [
                    Call("shotgun.shoot", "monk_boss", None, [None], from_current=True)
                ]
            else:
                action NullAction()
        imagebutton:
            align (0.5, 0.5)
            pos dash_pos[monk_health]
            idle dash_idle[monk_health]
            sensitive False
        imagebutton:
            align (0.5, 0.5)
            pos monk_pos[monk_health]
            idle "monk"
            insensitive "monk shot"
            selected_idle "monk shot"
            selected monk_health <= 0
            sensitive monk_health > 0
            action [
                SetVariable("monk_health", monk_health - 1),
                If(monk_health == 1,
                    Call("shotgun.shoot", "monk_boss", "monk", ["monk"], from_current=True),
                    Call("shotgun.shoot", "monk_boss", None, [None], from_current=True)
                )
            ]

    # Sprites
    image null_dash:
        alpha 0.0

    image horizontal_dash:
        "ninja/horizontal_dash.png"
        alpha 1.0
        linear 0.25 alpha 0.0

    image diagonal_dash:
        "ninja/diagonal_dash.png"
        alpha 1.0
        linear 0.25 alpha 0.0

    # Script
    hide screen temple_raid_timer
    show screen interact_temple_raid_boss
    show smoke_cloud onlayer screens zorder 1:
        zoom 0.75
        yalign 1.0
    show smoke_plume onlayer screens zorder 1:
        zoom 0.75
        yalign 0.75
    pause

    label .clear:
        # Script
        show shotgun unequip onlayer screens zorder 50
        pause 0.5
        hide shotgun onlayer screens
        hide shotgun_flash onlayer screens
        scene bg plain_white
        hide screen interact_temple_raid_boss
        hide screen interact_temple_raid_shootout
        hide pillars onlayer screens
        with fade
        jump police_quest_complete

label police_quest_complete:
    # Screens
    screen interact_police_quest_complete():
        button action NullAction()
        frame:
            pos (0.44, 0.40)
            textbutton "take_cash":
                xysize (0.15, 0.40)
                action [
                    Hide(),
                    Jump("police_quest_complete.accepted")
                ]

    # Sprites
    image strike_swinging:
        "police/strike_police_dead_swing.png"
        align (0.5, 0.5)
        pos (0.66, -0.1)
        rotate 10
        block:
            ease 2.0 rotate -30
            ease 2.0 rotate 10
            repeat

    # Script
    scene bg hideout_temple_bloody
    show strike_swinging
    show police_no_arm:
        align (0.5, 0.5)
        ypos 0.6
    show police_arm:
        align (0, 0)
        pos (0.605, 0.75)
    with fade
    officer "Thanks for your help!"
    officer "That was our most successful operation yet!"
    officer "Now we'll be able to shut down their entire syndicate!"
    hide police_arm
    show police_cash_arm:
        align (0, 0)
        pos (0.41, 0.39)
    show screen interact_police_quest_complete
    officer "Here's your {i}cash{/i} reward."
    pause

    label .accepted:
        # Settings
        $ inventory["cash"]["active"] = True
        $ inventory["radio"]["active"] = False
        $ progress["quests"]["police"]["complete"] = True
        $ progress["quests"]["clowns"]["disabled"] = True

        # Script
        hide police_cash_arm
        show police_arm:
            align (0, 0)
            pos (0.605, 0.75)
        officer "Now I must ask you to leave the crime scene."
        scene bg plain_white with fade
        scene bg plain_charcoal with fade
        centered "You get escorted back to Chinatown..."
        jump chinatown_west