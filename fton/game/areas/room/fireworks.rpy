label fireworks(origin="chinatown_east"):
    screen interact_fireworks():
        frame:
            pos (0, 0.8)
            textbutton "chinatown":
                xysize (1.0, 0.2)
                action [
                    Jump(origin)
                ]
        frame:
            pos (0.46, 0.15)
            textbutton "fireworks_talk":
                xysize (0.1, 0.36)
                action [
                    Jump("fireworks.talk")
                ]

    scene bg room_fireworks with fade
    call screen interact_fireworks
    
    label .talk:
        screen interact_fireworks_talk():
            button action NullAction()
            frame:
                pos (0.67, 0.53)
                textbutton "take_bomb":
                    xysize (0.1, 0.1)
                    action [
                        Hide(),
                        SetDict(inventory["letter"], "active", False),
                        SetDict(inventory["bomb"], "active", True),
                        Jump("fireworks")
                    ]
                    
        if inventory["letter"]["active"]:
            scene bg room_fireworks_counter with fade
            wei "You bring letter?"
            wei "Ok. I give you package."
            scene bg  room_fireworks_counter_offer
            show screen interact_fireworks_talk
            wei "Here. You take."
            pause
        else:
            wei "No Narwhals. Only fireworks.{w=2}{nw}"
            if progress["quests"]["clowns"]["complete"] or inventory["cash"]["active"]:
                wei "I already gave you fireworks.{w=2}{nw}"
            else:
                wei "No money, no fireworks.{w=2}{nw}"
            call screen interact_fireworks