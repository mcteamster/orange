label tent:
    # Settings
    $ inventory["wrench"]["highlight"] = False

    # Screens
    screen interact_tent():
        frame:
            pos (0.0, 0.8)
            textbutton "junction":
                xysize (1.0, 0.2)
                action [
                    Jump("junction")
                ]
        frame:
            pos (0.0, 0.0)
            textbutton "hydrant":
                xysize (0.1, 0.67)
                action [
                    Jump("hydrant")
                ]
        frame:
            pos (0.8, 0.5)
            textbutton "drain":
                xysize (0.2, 0.25)
                action [
                    Jump("drain")
                ]
        if progress["quests"]["clowns"]["disabled"] == False and ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]) == False:
            frame:
                pos (0.18, 0.54)
                textbutton "plans":
                    xysize (0.64, 0.09)
                    action [
                        Jump("plans")
                    ]
            if (inventory["bomb"]["active"] or progress["night"]) == False:
                frame:
                    pos (0.445, 0.17)
                    textbutton "talk_clown":
                        xysize (0.1, 0.36)
                        action [
                            Jump("tent.talk")
                        ]

    # Script
    if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
        scene bg circus_tent_flushed
    elif inventory["bomb"]["active"] or progress["night"]:
        scene bg circus_tent_empty
    else:
        scene bg circus_tent
    with fade
    call screen interact_tent

    label .talk:
        if progress["quests"]["clowns"]["complete"]:
            clown "Great work on the heist."
            clown "Spend your {i}cash{/i} wisely."
            clown "And make sure you don't go near the Police."
            call screen interact_tent
        elif progress["quests"]["clowns"]["accepted"] or inventory["letter"]["active"]:
            jump tent.accepted
        else:
            jump tent.quest

    label .quest:
        screen interact_tent_quest():
            button action NullAction()
            frame:
                pos (0.0, 0.8)
                textbutton "tent":
                    xysize (1.0, 0.2)
                    action [
                        Hide(),
                        Jump("tent")
                    ]
            frame:
                pos (0.62, 0.3)
                textbutton "take_letter":
                    xysize (0.09, 0.11)
                    action [
                        Hide(),
                        Jump("tent.accepted")
                    ]

        scene bg circus_tent_table with fade
        clown "Are you the new guy?"
        if progress["quests"]["clowns"]["disabled"] or inventory["shotgun"]["active"]:
            clown "It's too late. We have to call off the heist."
            clown "The guy with the package got busted by the Police earlier."
            clown "Maybe next time."
            jump tent
        else:
            clown "We don't have time to chit chat. We're running behind schedule."
            scene bg circus_tent_table_offer
            $ progress["quests"]["clowns"]["offered"] = True
            show screen interact_tent_quest
            clown "Here, take this {i}letter{/i} and we'll go first."
            pause
    
    label .accepted:
        scene bg circus_tent_table
        if progress["quests"]["clowns"]["accepted"] == True:
            with fade
        $ progress["quests"]["clowns"]["accepted"] = True
        $ inventory["letter"]["active"] = True
        clown "Take that {i}letter{/i} to the man in the fireworks store."
        clown "Give him the {i}letter{/i} and he'll give you the package."
        clown "Then bring the package to the meeting place like we discussed on the phone."
        clown "Understand? Good. Hurry, we're running late."
        jump tent
        pause

label plans:
    screen interact_plans():
        frame:
            pos (0.0, 0.8)
            textbutton "tent":
                xysize (1.0, 0.2)
                action [
                    Jump("tent")
                ]

    scene bg circus_plans with fade
    call screen interact_plans

label hydrant:
    # Settings
    if inventory["wrench"]["active"]:
        $ inventory["wrench"]["highlight"] = True

    screen interact_hydrant():
        frame:
            pos (0.9, 0.0)
            textbutton "tent":
                xysize (0.1, 1.0)
                action [
                    Jump("tent")
            ]
        frame:
            pos (0.19, 0.39)
            textbutton "use_hydrant":
                xysize (0.14, 0.48)
                action [
                    Jump("hydrant.use")
                ]

    $ hydrant_scene = "bg circus_hydrant"
    if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
        $ hydrant_scene += "_flushed"
    if (progress["night"] or inventory["key"]["active"]):
        $ hydrant_scene += "_night"
    elif progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        $ hydrant_scene += "_eve"
    scene expression hydrant_scene with fade
    call screen interact_hydrant

    label .use:
        if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
            if inventory["beer"]["active"]:
                "I sure hope there aren't any fires today."
            elif inventory["key"]["active"]:
                "Oops..."
                "Don't waste water."
        else:
            "It's bolted tight."
            "I'd need a {i}tool{/i} to open it."
        call screen interact_hydrant

label drain:
    # Screens
    screen interact_drain():
        frame:
            pos (0.0, 0.0)
            textbutton "tent":
                xysize (0.15, 1.0)
                action [
                    Jump("tent")
            ]
        frame:
            pos (0.38, 0.76)
            textbutton "use_drain":
                xysize (0.215, 0.16)
                action [
                    Jump("drain.use")
                ]

    # Script
    if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
        scene bg circus_drain_flushed
    else:
        scene bg circus_drain
    with fade
    call screen interact_drain

    label .use:
        if progress["quests"]["mermaids"]["complete"] or ((inventory["beer"]["active"] or inventory["key"]["active"]) and inventory["helmet"]["active"]):
            jump pipe
        else:
            "That doesn't look healthy. I wonder how the fish feel about that."
            call screen interact_drain

label mermaids_revenge:
    # Sprites
    image bg circus_hydrant_open:
        "bg circus_hydrant_open_1.png"
        pause 0.05
        "bg circus_hydrant_open_2.png"
        pause 0.05
        repeat

    image tent_rising_water_a:
        "underwater/rising_water.png"
        align (0.8, 0)
        pos (1.0, 0.75)
        linear 2.0 pos (0.7, 0.25)
    
    image tent_rising_water_b:
        "underwater/rising_water.png"
        align (0.2, 0)
        pos (0.0, 0.75)
        linear 2.0 pos (0.3, 0.25)

    # Script
    $ inventory["wrench"]["highlight"] = False
    if progress["quests"]["clowns"]["accepted"] and progress["quests"]["clowns"]["complete"] == False:
        "I probably shouldn't piss off these crazy clowns just yet."
        call screen interact_hydrant
    $ inventory["wrench"]["active"] = False
    scene bg circus_hydrant_open with fade
    pause 2.0
    scene bg circus_tent
    show tent_rising_water_a
    show tent_rising_water_b
    with fade
    pause 1.5
    scene bg circus_drain
    show deep_water zorder 3:
        alpha 0.5
    with fade 
    show drain_hole:
        align (0.5, 0.5)
        pos (0.49, 0.84)
    show drain_edge zorder 1
    show drain_grate zorder 2:
        align (0.5, 0.5)
        pos (0.49, 0.84)
        rotate 0
        linear 0.5 pos (-0.1, -0.1) rotate -360
    show mermaid_blue:
        align (0.5, 0.5)
        pos (0.55, 1.2)
        easeout 0.5 pos (0.55, 0.8)
    pause 1.0
    scene bg circus_tent_attacked
    show deep_water zorder 3:
        alpha 0.5
    show tent_table zorder 2:
        align (0.5, 0.5)
        ypos 1.0
    show clown_drowned zorder 1:
        align (0.0, 0.0)
        pos (0.2, 0.2)
        linear 2.0 ypos 0.1
    with fade
    show mermaid_blue_attack:
        align (0.0, 0.0)
        pos (1.2, 0.1)
        linear 1.0 xpos -1.0
    pause 0.25
    show mermaid_purple_attack zorder 2:
        align (0.0, 0.0)
        pos (1.2, 0.1)
        linear 1.0 xpos -1.0
    pause 0.25
    show mermaid_green_attack zorder 1:
        align (0.0, 0.0)
        pos (1.2, 0.1)
        linear 0.5 xpos 0.4
    pause 0.4
    hide clown_drowned
    hide mermaid_green_attack
    show mermaid_vs_clown:
        align (0.0, 0.0)
        pos (0.22, 0.1)
        linear 0.75 pos (0.18, 0.05)
    show blood:
        align (0.0, 0.0)
        pos (0.35, 0.25)
        linear 0.75 pos (0.34, 0.22) alpha 0.5
    pause 0.5
    scene bg plain_charcoal
    show deep_water zorder 3:
        alpha 0.5
    show drain_hole_above:
        align (0.5, 0.5)
        pos (0.5, 0.5)
        linear 4.0 zoom 4
    show water_vortex:
        align (0.5, 0.5)
        pos (0.5, 0.5)
        linear 4.0 rotate -2000
    with fade
    pause 3.5
    jump mermaid_quest_complete

label clown_quest_complete:
    screen interact_clown_quest_complete():
        button action NullAction()
        frame:
            pos (0.43, 0.28)
            textbutton "take_cash":
                xysize (0.12, 0.29)
                action [
                    Hide(),
                    SetDict(inventory["cash"], "active", True),
                    Jump("tent")
                ]

    scene bg plain_white
    hide bank_wall_overlay onlayer screens
    hide clown_van onlayer screens
    hide screen interact_bank_south_shootout
    with fade
    stop music fadeout 1.0
    scene bg plain_charcoal with fade
    centered "You speed across town..."
    scene bg circus_tent_table with fade
    clown "Great work!"
    clown "That was our most successful heist yet!"
    scene bg circus_tent_table_complete
    $ progress["quests"]["clowns"]["complete"] = True
    show screen interact_clown_quest_complete
    clown "Here is your cut of the {i}cash{/i}."
    pause