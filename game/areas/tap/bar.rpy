label tavern:
    # Screens
    screen interact_tavern():
        frame:
            pos (0.0, 0.8)
            textbutton "downtown":
                xysize (1.0, 0.2)
                action [
                    Jump("downtown")
                ]
        frame:
            pos (0.16, 0.2)
            textbutton "storeroom":
                xysize (0.08, 0.26)
                action [
                    Jump("storeroom")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.04, 0.25)
                textbutton "jerry":
                    xysize (0.04, 0.27)
                    action [
                        Jump("jerry")
                    ]

            frame:
                pos (0.315, 0.175)
                textbutton "bartender":
                    xysize (0.37, 0.355)
                    action [
                        Jump("bartender")
                    ]
            frame:
                pos (0.81, 0.45)
                textbutton "pool":
                    xysize (0.19, 0.35)
                    action [
                        Jump("pool")
                    ]
                    
    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg tap_tavern_night
    else:
        scene bg tap_tavern
    with fade
    call screen interact_tavern

label jerry:
    # Screens
    screen interact_jerry():
        frame:
            pos (0, 0.8)
            textbutton "tavern":
                xysize (1.0, 0.2)
                action [
                    Jump("tavern")
                ]

    # Script
    scene bg tap_jerry with fade
    jerry "Mad party last night, man!{w=2}{nw}"
    call screen interact_jerry

label bartender:
    # Screens
    screen interact_bartender():
        frame:
            pos (0, 0.8)
            textbutton "tavern":
                xysize (1.0, 0.2)
                action [
                    Jump("tavern")
                ]
        frame:
            pos (0.435, 0.25)
            textbutton "bartender_talk":
                xysize (0.135, 0.35)
                action [
                    Jump("bartender.talk")
                ]

    # Script
    scene bg tap_bartender with fade
    pat "Sorry, mate. We've just run out of {i}beer{/i}."
    pat "The Pirates usually import it for me. You should talk to them."
    call screen interact_bartender

    label .talk:
        pat "My brothers keep telling people that they're twins.{w=2}{nw}"
        pat "We're actually triplets.{w=2}{nw}"
        pat "How do you think that makes me feel?{w=2}{nw}"
        call screen interact_bartender

label pool:
    # Screens
    screen interact_pool():
        frame:
            pos (0, 0.8)
            textbutton "tavern":
                xysize (1.0, 0.2)
                action [
                    Jump("tavern")
                ]
        frame:
            pos (0.435, 0.23)
            textbutton "pool_talk":
                xysize (0.135, 0.37)
                action [
                    Jump("pool.talk")
                ]

    # Script
    scene bg tap_pool with fade
    call screen interact_pool

    label .talk:
        brian "I got out last week on good behaviour.{w=2}{nw}"
        brian "I don't wear shoes anymore.{w=2}{nw}"
        brian "I was going to ask if you wanted to play...{w=2}{nw}"
        brian "But creating the game mechanics in Ren'Py was too difficult.{w=2}{nw}"
        call screen interact_pool