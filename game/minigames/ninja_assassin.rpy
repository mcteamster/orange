label ninja_assassin:
    # Screens
    screen interact_ninja_assassin_menu():
        frame:
            pos (0.02, 0.8625)
            textbutton "play":
                xysize (0.11, 0.09)
                action [
                    Jump("ninja_assassin.play")
                ]
        frame:
            pos (0.865, 0.8625)
            textbutton "quit":
                xysize (0.11, 0.09)
                action [
                    Jump("ninja_assassin.quit")
                ]
        if progress["minigames"]["ninja_assassin"]["attempts"] >= 3 and progress["minigames"]["ninja_assassin"]["complete"] == False:
            imagebutton:
                pos (0.14, 0.864)
                idle "ninja_assassin_skip_button"
                action [
                    SetDict(progress["minigames"]["ninja_assassin"], "complete", True),
                    Jump("ninja_assassin.quit")
                ]

    # Sprites
    image ninja_assassin_skip_button:
        "minigames/ninja_assassin_skip.png"
        zoom 0.967

    image ninja_assassin_sword_death:
        "minigames/ninja_assassin_sword.png"

    # Script
    scene bg plain_charcoal
    hide screen hud_inventory
    with fade
    scene ninja_assassin_title
    call screen interact_ninja_assassin_menu

    label .play:
        # Settings
        $ progress["minigames"]["ninja_assassin"]["attempts"] += 1
        $ ninja_assassin_ticks = 0
        $ end_tick = False;
        $ ninja_assassin_enemies = [
            {"time": 150, "active": True, "angle": 120, "start_pos": (0.9, -0.2)},
            {"time": 200, "active": True, "angle": 135, "start_pos": (1.2, 0.0)},
            {"time": 200, "active": True, "angle": 165, "start_pos": (1.2, 0.4)},
            {"time": 250, "active": True, "angle": 105, "start_pos": (0.7, -0.2)},
            {"time": 300, "active": True, "angle": 90, "start_pos": (0.5, -0.2)},
            {"time": 400, "active": True, "angle": 150, "start_pos": (1.2, 0.2)},
            {"time": 450, "active": True, "angle": 180, "start_pos": (1.2, 0.6)},
            {"time": 450, "active": True, "angle": 15, "start_pos": (-0.2, 0.4)},
            {"time": 500, "active": True, "angle": 0, "start_pos": (-0.2, 0.6)},
            {"time": 600, "active": True, "angle": 45, "start_pos": (-0.2, 0.0)},
            {"time": 650, "active": True, "angle": 60, "start_pos": (0.1, -0.2)},
            {"time": 600, "active": True, "angle": 75, "start_pos": (0.3, -0.2)},
            {"time": 700, "active": True, "angle": 30, "start_pos": (-0.2, 0.2)},
        ]

        # Screens
        screen ninja_assassin_play_timer():
            timer 0.02:
                repeat True
                if [a for a in ninja_assassin_enemies if a["active"]]:
                    if ninja_assassin_ticks >= (sorted([a for a in ninja_assassin_enemies if a["active"]], key = lambda assassin: assassin["time"])[0]["time"] - 10):
                        action [
                            Hide(),
                            Jump("ninja_assassin.death")
                        ]
                    else:
                        action [
                            SetVariable("ninja_assassin_ticks", ninja_assassin_ticks + 1)
                        ]
                elif end_tick == False:
                    action [
                        SetVariable("ninja_assassin_ticks", ninja_assassin_ticks + 1),
                        SetVariable("end_tick", ninja_assassin_ticks + 10)
                    ]
                elif ninja_assassin_ticks > end_tick:
                    action [
                        Hide(),
                        Jump("ninja_assassin.win")
                    ]
                else:
                    action [
                        SetVariable("ninja_assassin_ticks", ninja_assassin_ticks + 1)
                    ]

        screen interact_ninja_assassin_play():
            button action NullAction()
            for (i, assassin) in enumerate(ninja_assassin_enemies):
                $ assassin_image =  Image("minigames/assassin_" + str(assassin["angle"]) + ".png")
                $ ticks_away = (assassin["time"] - ninja_assassin_ticks)
                if assassin["active"] and ticks_away < 100:
                    $ position = (0.5 + (assassin["start_pos"][0]-0.5)*0.01*ticks_away, 0.7 + (assassin["start_pos"][1]-0.7)*0.01*ticks_away)
                elif assassin["active"] == False:
                    $ hit_tick = (assassin["time"] - assassin["hit_time"])
                    $ hit_delta = ninja_assassin_ticks - assassin["hit_time"]
                    if hit_delta < 10:
                        $ position = (0.5 + (assassin["start_pos"][0]-0.5)*0.01*ticks_away, 0.7+ (assassin["start_pos"][1]-0.7)*0.01*ticks_away)
                    else:
                        $ assassin_image = At(assassin_image, assassin_death)
                        $ position = (0.5 + (assassin["start_pos"][0]-0.5)*0.01*(hit_tick-10), 0.7 + (assassin["start_pos"][1]-0.7)*0.01*(hit_tick-10))
                else:
                    $ position = assassin["start_pos"]
                imagebutton:
                    align (0.5, 0.5)
                    if assassin["active"]:
                        pos position
                    else:
                        pos position
                    idle assassin_image
                    selected assassin["active"] == False
                    sensitive assassin["active"]
                    action [
                        Play("audio", "audio/whoosh.wav"),
                        SetDict(assassin, "active", False),
                        SetDict(assassin, "hit_time", ninja_assassin_ticks),
                    ]
                if assassin["active"] == False:
                    if hit_delta < 10:
                        $ shuriken_position = (0.5 + (position[0] - 0.5)*0.1*hit_delta, 0.7 + (position[1] - 0.7)*0.1*hit_delta)
                        imagebutton:
                            align (0.5, 0.5)
                            pos shuriken_position
                            idle "minigames/ninja_assassin_shuriken.png"

        # Sprites
        transform assassin_death:
            alpha 0.1

        # Script
        scene bg plain_charcoal
        show screen ninja_assassin_play_timer
        show screen interact_ninja_assassin_play
        show ninja_assassin_ninja onlayer screens zorder 1
        pause

    label .death:
        scene ninja_assassin_death
        hide screen interact_ninja_assassin_play
        hide ninja_assassin_ninja onlayer screens
        if progress["minigames"]["ninja_assassin"]["attempts"] >= 1:
            show ninja_assassin_sword_death as sword_1:
                align (0.5, 0.5)
                pos (0.5, 0.8)
        if progress["minigames"]["ninja_assassin"]["attempts"] >= 2:
            show ninja_assassin_sword_death as sword_2:
                align (0.5, 0.5)
                pos (0.49, 0.8)
        if progress["minigames"]["ninja_assassin"]["attempts"] >= 3:
            show ninja_assassin_sword_death as sword_3:
                align (0.5, 0.5)
                pos (0.48, 0.8)
        call screen interact_ninja_assassin_menu

    label .win:
        $ progress["minigames"]["ninja_assassin"]["complete"] = True
        pause 0.5
        scene ninja_assassin_win
        hide screen interact_ninja_assassin_play
        hide ninja_assassin_ninja onlayer screens
        pause 3.0
        jump ninja_assassin.quit

    label .quit:
        scene bg plain_charcoal 
        show screen hud_inventory
        with None
        if progress["minigames"]["ninja_assassin"]["complete"] and (progress["quests"]["ninjas"]["offered"] == False):
            jump arcade.quest
        else:
            jump arcade

