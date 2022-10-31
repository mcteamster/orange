label lobby:
    # Screens
    screen interact_lobby():
        frame:
            pos (0.8, 0.12)
            textbutton "hallway":
                xysize (0.1, 0.75)
                action [
                    Jump("hallway")
                ]
        if (progress["night"] or inventory["key"]["active"]) == False:
            frame:
                pos (0.62, 0.32)
                textbutton "mailbox":
                    xysize (0.14, 0.22)
                    action [
                        Jump("mailbox")
                    ]
        frame:
            pos (0.25, 0.36)
            textbutton "downtown":
                xysize (0.05, 0.30)
                action [
                    Jump("downtown")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg flats_lobby_night
    else:
        scene bg flats_lobby
    with fade
    call screen interact_lobby

label mailbox:
    # Screens
    screen interact_mailbox():
        frame:
            pos (0, 0.8)
            textbutton "lobby":
                xysize (1.0, 0.2)
                action [
                    Jump("lobby")
                ]

    # Script
    scene bg flats_mailbox with fade
    call screen interact_mailbox
