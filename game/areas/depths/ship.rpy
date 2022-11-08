label ship(origin="pier"):
    screen interact_ship():
        frame:
            pos (0.0, 0.0)
            textbutton "pier":
                xysize (1.0, 0.2)
                action [
                    Jump("pier")
                ]
        frame:
            pos (0.0, 0.0)
            textbutton "pipe":
                xysize (0.15, 1.0)
                action [
                    Jump("pipe")
                ]
        frame:
            pos (0.2, 0.23)
            textbutton "talk_mermaid":
                xysize (0.58, 0.45)
                action [
                    Jump("ship.talk")
                ]

    image bg depths_ship:
        "bg depths_ship_1"
        pause 0.5
        "bg depths_ship_2"
        pause 0.5
        repeat

    scene bg depths_ship
    show sunbeam_a
    show sunbeam_b
    show fish_green
    show fish_purple
    show fish_red
    show fish_yellow
    show mermaid_purple:
        align (0.5, 1.0)
        pos (0.43, 0.9)
    show mermaid_green:
        align (0.5, 1.0)
        pos (0.2, 0.97)
    show mermaid_blue:
        align (0.5, 1.0)
        pos (0.8, 0.9)
    show seaweed as seaweed_1 at left
    show seaweed as seaweed_2 at right
    if origin == "pier":
        show bubbles_float_1
        show bubbles_float_2
        show bubbles_float_3
        show bubbles_float_4
        show bubbles_float_5
        show bubbles_float_6
        show bubbles_float_7
        show bubbles_float_8
        play audio "audio/bubbles.wav"
    with fade
    call screen interact_ship

    label .talk:
        define mermaid_talk_counter = 0
        $ mermaid_talk_counter += 1
        if (mermaid_talk_counter % 3) == 1:
            arianne "Thank you for your help!{w=2}{nw}"
        elif (mermaid_talk_counter % 3) == 2:
            arianne "Girls, now we finally have time for the important things.{w=2}{nw}"
            shelly "I've already got plans for how to flood the earth.{w=2}{nw}"
            coral "I can't wait for the day that Mermaids rule the world.{w=2}{nw}"
        else: 
            arianne "You didn't hear any of that did you?{w=2}{nw}"
            $ mermaid_talk_counter = 0
        call screen interact_ship

    label .fight:
        screen interact_ship_fight():
            button action NullAction()
            frame:
                pos (0.39, 0.25)
                textbutton "captain":
                    xysize (0.09, 0.45)
                    action [
                        Hide(),
                        Jump("ship.shot_captain")
                    ]
            frame:
                pos (0.44, 0.29)
                textbutton "mermaid":
                    xysize (0.1, 0.6)
                    action [
                        Hide(),
                        Jump("ship.shot_mermaid")
                    ]

        image ship_pirate_vs_mermaid:
            "mermaid/pirate_vs_mermaid.png"
            align (0.0, 0.0)
            pos (0.25, 0.25)

        image ship_mermaid_angry:
            "mermaid/mermaid_angry.png"
            ypos 4.0
            linear 1.0 ypos 1.55

        scene bg plain_white with fade
        scene bg depths_ship
        show sunbeam_a
        show sunbeam_b
        show fish_green
        show fish_purple
        show fish_red
        show fish_yellow
        show seaweed as seaweed_1 at left
        show seaweed as seaweed_2 at right
        show ship_pirate_vs_mermaid
        show ship_harpoon
        show bubbles_float_1
        show bubbles_float_2
        show bubbles_float_3
        show bubbles_float_4
        show bubbles_float_5
        show bubbles_float_6
        show bubbles_float_7
        show bubbles_float_8
        play audio "audio/bubbles.wav"
        with fade
        show screen interact_ship_fight
        pause 0.5
        captain "Arr! Matey! I've got her! Quick harpoon the wench!{w=2}{nw}"
        pause 2
        captain "What are yer waiting for? Shoot her!{w=2}{nw}"
        pause 2
        hide screen interact_ship_fight
        show ship_mermaid_angry
        pause 1.5
        $ inventory["helmet"]["active"] = False
        jump drowned
    
    label .shot_mermaid:
        image ship_captain:
            "pirate/captain_helmet.png"
            align (0.0, 0.0)
            pos (0.35, 0.25)

        image ship_mermaid shot:
            "mermaid/mermaid_shot.png"
            align (0.75, 0.66)
            pos (0.55, 0.74)
            linear 0.1 zoom 0.5

        image ship_mermaid dead:
            "mermaid/mermaid_dead.png"
            zoom 0.5
            align (0.75, 0.66)
            pos (0.55, 0.74)

        image ship_harpoon_bubbles:
            "underwater/bubbles.png"
            zoom 0.1
            align (0, 0)
            pos (0.6, 0.5)
            linear 1.5 ypos -1.0

        play audio "audio/harpoon.wav"
        hide ship_pirate_vs_mermaid
        show ship_harpoon empty
        show ship_harpoon_stream
        show ship_harpoon_bubbles
        show ship_mermaid shot
        show ship_captain
        pause 0.1
        show ship_mermaid dead
        captain "Great shooting matey!"
        scene bg plain_white with fade
        scene bg plain_charcoal with fade
        centered "You salvage the cargo and return to the surface..."
        jump pirate_quest_complete

    label .shot_captain:
        image ship_captain shot:
            "pirate/captain_shot.png"
            align (0.25, 0.66)
            pos (0.42, 0.75)
            linear 0.1 zoom 0.5
        
        image ship_captain dead:
            "pirate/captain_dead.png"
            zoom 0.75
            align (0.25, 0.66)
            pos (0.42, 0.75)

        image ship_mermaid_scared:
            "mermaid/mermaid_scared.png"
            align (0.25, 0.66)
            pos (0.3235, 0.707)

        image ship_blood:
            "pirate/blood.png"
            align (0.25, 0.0)
            pos (0.4, 0.25)
            alpha 1.0
            linear 0.25 ypos 0.15 alpha 0.0

        $ progress["quests"]["pirates"]["disabled"] = True
        play audio "audio/harpoon.wav"
        hide ship_pirate_vs_mermaid
        show ship_harpoon empty
        show ship_harpoon_stream
        show ship_harpoon_bubbles
        show ship_captain shot
        show ship_blood
        show ship_mermaid_scared
        pause 0.25
        show ship_captain dead
        hide ship_mermaid_scared
        show mermaid_purple:
            align (0.5, 1.0)
            pos (0.45, 0.9)
        show mermaid_green:
            align (0.5, 1.0)
            pos (-0.5, 0.97)
            ease 1.0 xpos 0.2
        show mermaid_blue:
            align (0.5, 1.0)
            pos (1.5, 0.9)
            ease 1.0 xpos 0.8
        pause 1.5
        arianne "Thank you for not killing me!"
        arianne "An Orange Narwhal? Not in these waters."
        shelly "But we do have some {i}beer{/i}."
        coral "If you help us, we'll give it to you."
        pause 0.5
        show mermaid_purple:
            xzoom -1
            linear 1.5 xpos -0.2
        show mermaid_green:
            xzoom -1
            linear 0.75 xpos -0.2
        show mermaid_blue:
            linear 2.25 xpos -0.2
        pause 2.0
        jump pipe.quest

label drowned:
    image depths_deep_water:
        "mermaid/deep_water.png"
        alpha 0.5
        linear 6.0 alpha 1.0

    image depths_drowned closeup:
        "mermaid/drowned_closeup.png"
        align (0.5, 0.5)
        zoom 1.0
        linear 4.0 zoom 0.5

    image depths_drowned:
        "mermaid/drowned.png"
        align (0.5, 0.75)
        pos (0.5, 0.66)
        zoom 1.0
        linear 4.0 zoom 0.8

    scene bg plain_black with fade
    scene bg depths_drowned
    show sunbeam_a
    show sunbeam_b
    show depths_drowned closeup
    show bubbles_float_1
    show bubbles_float_2
    show bubbles_float_3
    show bubbles_float_4
    show bubbles_float_5
    show bubbles_float_6
    show bubbles_float_7
    show bubbles_float_8
    play audio "audio/bubbles.wav"
    show depths_deep_water
    play audio "audio/bell.wav"
    pause 3.0
    show depths_drowned -closeup
    pause 3.0
    jump game_over