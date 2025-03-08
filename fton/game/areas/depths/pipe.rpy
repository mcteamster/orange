label pipe:
    screen interact_pipe():
        frame:
            pos (0.0, 0.0)
            textbutton "pier":
                xysize (1.0, 0.2)
                action [
                    Jump("pier")
                ]
        frame:
            pos (0.85, 0.0)
            textbutton "ship":
                xysize (0.15, 1.0)
                action [
                    Call("ship", "pipe")
                ]
        if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
            frame:
                pos (0.38, 0.11)
                textbutton "use_drain":
                    xysize (0.24, 0.4)
                    action [
                        Jump("drain")
                    ]

    if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
        scene bg depths_pipe_open
    elif progress["quests"]["mermaids"]["offered"] and progress["quests"]["mermaids"]["accepted"] == False:
        jump pipe.quest
    else:
        scene bg depths_pipe_closed
        show waste
    show sunbeam_a
    show sunbeam_b
    show fish_green
    show fish_purple
    show fish_red
    show fish_yellow
    show seaweed as seaweed_1 at left
    show seaweed as seaweed_2 at right
    with fade
    call screen interact_pipe

    label .quest:
        screen interact_pipe_quest():
            button action NullAction()
            frame:
                pos (0.0, 0.0)
                textbutton "pier":
                    xysize (1.0, 0.2)
                    action [
                        Hide(),
                        Jump("pier")
                    ]
            frame:
                pos (0.85, 0.0)
                textbutton "ship":
                    xysize (0.15, 1.0)
                    action [
                        Hide(),
                        Call("ship", "pipe")
                    ]
            frame:
                pos (0.4, 0.48)
                textbutton "take_wrench":
                    xysize (0.1, 0.14)
                    action [
                        Hide(),
                        SetDict(inventory["wrench"], "active", True),
                        SetDict(progress["quests"]["mermaids"], "accepted", True),
                        Jump("pier")
                    ]

        $ progress["quests"]["mermaids"]["offered"] = True
        scene bg depths_pipe_closed
        show waste
        show sunbeam_a
        show sunbeam_b
        show fish_green
        show fish_purple
        show fish_red
        show fish_yellow
        show seaweed as seaweed_1 at left
        show seaweed as seaweed_2 at right
        show mermaid_purple_no_arm:
            align (0.5, 1.0)
            pos (0.25, 0.9)
        show mermaid_arm:
            align (0.0, 0.0)
            pos (0.375, 0.525)
        show mermaid_green:
            align (0.5, 1.0)
            pos (0.1, 0.97)
        show mermaid_blue:
            align (0.5, 1.0)
            pos (0.8, 0.9)
        with fade
        arianne "Someone is tipping toxic waste down the drain!"
        shelly "It's polluting our waters and killing the fish!"
        coral "Find whoever is responsible and help us stop them!"
        hide mermaid_arm
        show arm_wrench_glow:
            align (0.0, 0.0)
            pos (0.375, 0.47)
        show screen interact_pipe_quest
        arianne "Here, you might need this {i}tool{/i}."
        pause

label mermaid_quest_complete:
    $ achievement.grant("mermaids")
    $ achievement.sync()
    screen interact_mermaid_quest_complete():
        button action NullAction()
        frame:
            pos (0.27, 0.45)
            textbutton "take_beer":
                xysize (0.08, 0.16)
                action [
                    Hide(),
                    SetDict(inventory["beer"], "active", True),
                    SetDict(progress["quests"]["mermaids"], "complete", True),
                    Jump("mermaid_quest_complete.mermaids_leave")
                ]

    scene bg plain_white with fade
    scene bg plain_charcoal with fade
    centered "You deal with the last of the toxic waste..."
    scene bg depths_pipe_open
    show sunbeam_a
    show sunbeam_b
    show fish_green
    show fish_purple
    show fish_red
    show fish_yellow
    show seaweed as seaweed_1 at left
    show seaweed as seaweed_2 at right
    show mermaid_purple_no_arm:
        align (0.5, 1.0)
        pos (0.25, 0.9)
    show mermaid_arm:
        align (0.0, 0.0)
        pos (0.375, 0.525)
    show mermaid_green:
        align (0.5, 1.0)
        pos (0.1, 0.97)
    show mermaid_blue:
        align (0.5, 1.0)
        pos (0.8, 0.9)
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
    shelly "Thank you for your help."
    coral "Now our water is nice and clean."
    show screen interact_mermaid_quest_complete
    hide mermaid_arm
    show arm_beer_glow:
        align (0.0, 0.0)
        pos (0.27, 0.44)
    arianne "Here. Accept this {i}beer{/i} as a token of our appreciation."

    label .mermaids_leave:
        hide arm_beer_glow
        hide mermaid_purple_no_arm
        show mermaid_purple:
            align (0.5, 1.0)
            pos (0.27, 0.9)
            linear 1.0 xpos 1.5
        show mermaid_green:
            align (0.5, 1.0)
            pos (0.1, 0.97)
            linear 1.5 xpos 1.5
        show mermaid_blue:
            align (0.5, 1.0)
            pos (0.8, 0.9)
            linear 0.5 xpos 1.5 xzoom -1
        call screen interact_pipe