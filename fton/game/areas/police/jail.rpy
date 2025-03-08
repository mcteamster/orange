label jail:
    # Screens
    screen interact_jail():
        frame:
            pos (0.0, 0.22)
            textbutton "roof":
                xysize (0.105, 0.69)
                action [
                    Jump("roof")
                ]
        frame:
            pos (0.89, 0.22)
            textbutton "station":
                xysize (0.105, 0.7)
                action [
                    Jump("station")
                ]
        if inventory["shotgun"]["active"] and ((progress["night"] or inventory["key"]["active"]) == False):
            frame:
                pos (0.48, 0.34)
                textbutton "talk_monk":
                    xysize (0.06, 0.41)
                    action [
                        Jump("jail.talk_monk")
                    ]
            frame:
                pos (0.78, 0.33)
                textbutton "talk_officer":
                    xysize (0.08, 0.48)
                    action [
                        Jump("jail.talk_officer")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg police_jail_night
    elif inventory["shotgun"]["active"]:
        scene bg police_jail_monk
    else:
        scene bg police_jail_empty
    with fade
    call screen interact_jail

    label .talk_monk():
        define monk_talk_counter = 0
        $ monk_talk_counter += 1
        if (monk_talk_counter % 3) == 1:
            xiao "You have dishonoured the league of Ninjas.{w=2}{nw}"
        elif (monk_talk_counter % 3) == 2:
            xiao "Did you think I was dead?{w=2}{nw}"
            xiao "I cannot be killed!{w=2}{nw}"
        else: 
            xiao "I don't like it in here.{w=2}{nw}"
            $ monk_talk_counter = 0
        call screen interact_jail

    label .talk_officer:
        officer "Hello.{w=2}{nw}"
        call screen interact_jail

label arrested:
    # Sprites
    image jail_behind_bars:
        "police/behind_bars.png"
        align (0.5, 0.5)
        linear 5.0 zoom 0.75

    # Script
    scene bg plain_charcoal
    show jail_behind_bars
    with fade
    play audio "audio/bell.wav"
    pause 4.0
    $ achievement.grant("jail")
    $ achievement.sync()
    jump game_over