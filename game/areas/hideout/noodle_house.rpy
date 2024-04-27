label noodle_house(origin="chinatown_east"):
    # Screens
    screen interact_noodle_house():
        frame:
            pos (0.0, 0.8)
            textbutton "chinatown":
                xysize (1.0, 0.2)
                action [
                    Jump(origin)
                ]
        frame:
            pos (0.36, 0.2)
            textbutton "checkout":
                xysize (0.14, 0.34)
                action [
                    Jump("checkout")
                ]
        frame:
            pos (0.15, 0.145)
            textbutton "kitchen":
                xysize (0.155, 0.56)
                if progress["quests"]["ninjas"]["complete"] or inventory["noodles"]["active"]:
                    action [
                        Jump("kitchen")
                    ]
                else:
                    action [
                        Jump("noodle_house.shout")
                    ]

    # Script
    scene bg hideout_noodle_house with fade
    call screen interact_noodle_house

    label .shout:
        chow "Hey you can't go back there!{w=2}{nw}"
        call screen interact_noodle_house

label ninja_quest_complete:
    # Screens
    $ achievement.grant("ninjas")
    $ achievement.sync()
    screen interact_ninja_quest_complete():
        modal True
        frame:
            pos (0.59, 0.5)
            textbutton "take_noodles":
                xysize (0.07, 0.15)
                action [
                    Hide(),
                    SetDict(inventory["noodles"], "active", True),
                    SetDict(progress["quests"]["ninjas"], "complete", True),
                    Jump("noodle_house")
                ]

    # Script
    scene bg hideout_checkout with fade
    chow "Congratulations!"
    chow "You have demonstrated your loyalty to the league."
    chow "You are now authorised to enter the temple of the dragon."
    scene bg hideout_checkout_noodles
    show screen interact_ninja_quest_complete
    chow "Oh, and here is your complimentary {i}noodle{/i} box."
    pause

label checkout:
    # Screens
    screen interact_checkout:
        frame:
            pos (0.0, 0.8)
            textbutton "noodle_house":
                xysize (1.0, 0.2)
                action [
                    Call("noodle_house")
                ]
        frame:
            pos (0.36, 0.09)
            textbutton "talk_checkout":
                xysize (0.19, 0.67)
                action [
                    Jump("checkout.talk")
                ]

    # Script
    scene bg hideout_checkout with fade
    
    label .talk:
        chow "Um, no. We don't serve Narwhal here."
        chow "We just do {i}noodles{/i}."
        if inventory["noodles"]["active"] == False:
            chow "But if you become a member you get a free {i}noodle{/i} box."
            chow "To become a member you'll need to demonstrate your dexterity and reflexes."
        call screen interact_checkout

label kitchen:
    # Screens
    screen interact_kitchen():
        frame:
            pos (0.0, 0.8)
            textbutton "noodle_house":
                xysize (1.0, 0.2)
                action [
                    Jump("noodle_house")
                ]
        frame:
            pos (0.33, 0.285)
            textbutton "temple_path":
                xysize (0.09, 0.29)
                action [
                    Jump("temple_path")
                ]

    # Sprites
    image bg hidekout_kitchen:
        "bg hideout_kitchen_1"
        pause 0.25
        "bg hideout_kitchen_2"
        pause 0.25
        repeat

    # Script
    scene bg hidekout_kitchen with fade
    call screen interact_kitchen