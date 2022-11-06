label pub:
    # Settings
    if inventory["smoke"]["active"]:
        $ inventory["smoke"]["highlight"] = True

    # Screens
    screen interact_pub():
        frame:
            pos (0.0, 0.8)
            textbutton "dock":
                xysize (1.0, 0.2)
                action [
                    Hide(),
                    Jump("dock")
                ]
        if progress["quests"]["mermaids"]["offered"] == False and inventory["helmet"]["active"] == False:
            frame:
                pos (0.0, 0)
                textbutton "balcony":
                    xysize (0.14, 0.7)
                    action [
                        Jump("balcony")
                    ]
            frame:
                pos (0.36, 0.22)
                textbutton "kiosk":
                    xysize (0.22, 0.14)
                    action [
                        Jump("kiosk")
                    ]
            frame:
                pos (0.65, 0)
                textbutton "porch":
                    xysize (0.2, 0.7)
                    action [
                        Jump("porch")
                    ]
        frame:
            pos (0.495, 0.54)
            textbutton "basement":
                xysize (0.12, 0.09)
                if inventory["noodles"]["active"]:
                    action [
                        Hide(),
                        Jump("basement")
                    ]
                else:
                    action [
                        Jump("pub.shout")
                    ]
    
    # Script
    $ pub_scene = "bg dock_pub"
    if progress["quests"]["pirates"]["complete"] or (inventory["beer"]["active"] and inventory["helmet"]["active"] == False):
        $ pub_scene += "_beer"
    if progress["quests"]["ninjas"]["complete"] or inventory["noodles"]["active"]:
        $ pub_scene += "_open"
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        $ pub_scene += "_eve"    
    scene expression pub_scene with fade
    if progress["quests"]["mermaids"]["offered"] or inventory["helmet"]["active"]:
        show screen interact_pub
        pirate "Hey! He's the guy that killed the captain!{w=2}{nw}"
        show pub_angry_pirate
        pause 1.0
        hide screen interact_pub
        jump hanged
    call screen interact_pub

    label .shout:
        pirate "Hey! You're not allowed down there!{w=2}{nw}"
        call screen interact_pub

label pub_smoke:
    # Settings
    $ inventory["smoke"]["active"] = False
    $ inventory["smoke"]["highlight"] = False

    # Screens
    screen interact_pub_smoke():
        button action NullAction()
        frame:
            pos (0.0, 0.8)
            textbutton "dock":
                xysize (1.0, 0.2)
                action [
                    Hide(),
                    Jump("dock")
                ]
        frame:
            pos (0.495, 0.54)
            textbutton "basement":
                xysize (0.12, 0.09)
                action [
                    Hide(),
                    Jump("basement")
                ]

    # Sprites
    image pub_angry_pirate:
        "pirate/pirate_angry.png"
        ypos 4.0
        linear 1.0 ypos 1.4

    # Script
    $ pub_scene = "bg dock_pub" + ("_beer" if inventory["beer"]["active"] else "") + ("_open" if inventory["noodles"]["active"] else "")
    scene expression pub_scene
    show screen interact_pub_smoke
    show smoke_thrown
    pause 0.75
    play audio "audio/pop.wav"
    hide smoke_thrown
    show smoke_plume
    show smoke_bang
    show smoke_cloud
    show smoke_veil_5
    show smoke_veil_4
    show smoke_veil_3
    show smoke_veil_2
    show smoke_veil_1
    pirate "What the-? Who did that?{w=2}{nw}"
    pause 8
    hide screen interact_pub_smoke
    show pub_angry_pirate
    pirate "There he is! Get him!{w=2}{nw}}"
    jump hanged

label hanged:
    # Settings
    $ inventory["smoke"]["highlight"] = False

    # Sprites
    image dock_flagpole:
        "pirate/flagpole.png"
        zoom 1.0
        align (0.35, 0.5)
        ease 4.5 zoom 0.66

    image dock_noose:
        "pirate/noose.png"
        ypos 0.75
        zoom 1.0
        rotate 1
        ease 1.5 zoom 0.9 rotate -1
        ease 1.5 zoom 0.8 rotate 1
        ease 1.5 zoom 0.7 rotate -1
    
    # Script
    scene bg dock_water 
    show dock_flagpole
    show dock_noose
    with fade
    play audio "audio/bell.wav"
    pause 3.5
    jump game_over

label kiosk:
    # Settings
    $ inventory["smoke"]["highlight"] = False

    screen interact_kiosk():
        frame:
            pos (0.0, 0.8)
            textbutton "pub":
                xysize (1.0, 0.2)
                action [
                    Jump("pub")
                ]
        frame:
            pos (0.43, 0.16)
            textbutton "kiosk_talk":
                xysize (0.15, 0.52)
                action [
                    Jump("kiosk.talk")
                ]

    scene bg dock_kiosk with fade
    if inventory["beer"]["active"]:
        cook "Thanks for recovering our {i}beer{/i}!"
    else:
        cook "We've got fish and chips. But alas no {i}beer{/i}."
    call screen interact_kiosk

    label .talk:
        cook "The Orange Narwhal? You should talk to the captain upstairs."
        call screen interact_kiosk

label porch:
    # Settings
    $ inventory["smoke"]["highlight"] = False

    screen interact_porch():
        frame:
            pos (0.0, 0.8)
            textbutton "pub":
                xysize (1.0, 0.2)
                action [
                    Jump("pub")
                ]

    $ porch_scene = "bg dock_porch"
    if progress["quests"]["pirates"]["complete"] or (inventory["beer"]["active"] and inventory["helmet"]["active"] == False):
        $ porch_scene += "_beer"
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        $ porch_scene += "_eve"    
    scene expression porch_scene with fade
    call screen interact_porch

label basement:
    screen interact_basement():
        if inventory["noodles"]["active"]:
            frame:
                pos (0.56, 0.0)
                textbutton "pub":
                    xysize (0.19, 0.12)
                    action [
                        Jump("pub")
                    ]
        else:
            frame:
                pos (0.19, 0.5)
                textbutton "treasure":
                    xysize (0.23, 0.33)
                    action [
                        Jump("treasure")
                    ]

    image basement_treasure:
        "pirate/treasure.png"
        align (0.25, 0.75)

    scene bg dock_basement 
    if inventory["noodles"]["active"] == False:
        show basement_treasure
    with fade
    call screen interact_basement

label treasure:
    scene bg plain_white with fade
    scene bg plain_charcoal with fade
    centered "You leg it back to Chinatown..."
    jump ninja_quest_complete
