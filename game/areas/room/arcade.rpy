label arcade(origin="chinatown_east"):
    # Screens
    screen interact_arcade():
        frame:
            pos (0.0, 0.8)
            textbutton "chinatown":
                xysize (1.0, 0.2)
                action [
                    Jump(origin)
                ]
        frame:
            pos (0.23, 0.24)
            textbutton "arcade_land_mines":
                xysize (0.11, 0.24)
                action [
                    Jump("arcade_land_mines")
                ]
        frame:
            pos (0.1, 0.2)
            textbutton "arcade_do_or_die":
                xysize (0.12, 0.4)
                action [
                    Jump("arcade_do_or_die")
                ]
        frame:
            pos (0.65, 0.24)
            textbutton "arcade_out_of_order":
                xysize (0.11, 0.24)
                action [
                    Jump("arcade_out_of_order")
                ]
        frame:
            pos (0.79, 0.23)
            textbutton "ninja_assassin":
                xysize (0.11, 0.3)
                action [
                    Jump("ninja_assassin")
                ]

    # Script
    if progress["quests"]["ninjas"]["offered"] and progress["quests"]["ninjas"]["complete"] == False and inventory["smoke"]["active"] == False:
        jump arcade.quest
    else:
        scene bg room_arcade
        with fade
        call screen interact_arcade

    label .quest:
        # Settings
        $ progress["quests"]["ninjas"]["offered"] = True

        screen interact_arcade_quest():
            modal True
            frame:
                pos (0.0, 0.8)
                textbutton "chinatown":
                    xysize (1.0, 0.2)
                    action [
                        Hide(),
                        Jump(origin)
                    ]
            frame:
                pos (0.56, 0.40)
                textbutton "take_smoke":
                    xysize (0.03, 0.06)
                    action [
                        Hide(),
                        Jump("arcade.accepted")
                    ]

        image arcade_ninja:
            "ninja/ninja.png"
            zoom 0.95
            align (0.5, 0.0)
            ypos 0.13
        image arcade_ninja_arm:
            "ninja/ninja_arm.png"
            zoom 0.9
            align (0.535, 0.345)
        image arcade_ninja_arm bent:
            "ninja/ninja_arm.png"
            xzoom -0.9
            yzoom 0.9
            rotate -25
            align (0.56, 0.345)
        image arcade_smoke:
            "ninja/smoke_glow.png"
            zoom 0.8
            align (0.58, 0.43)

        # Script
        scene bg room_arcade
        show arcade_ninja
        show arcade_ninja_arm
        with fade
        ninja "You have proven your dexterity and reflexes."
        ninja "You have been invited to join the league of Ninjas."
        ninja "And will receive a complimentary box of noodles."
        ninja "But first you must demonstrate your loyalty to the league."
        ninja "You must retrieve the treasures from our mortal enemies..."
        ninja "The Pirates."
        show arcade_ninja_arm bent
        show arcade_smoke
        show screen interact_arcade_quest
        ninja "Take this {i}smoke{/i} grenade and return once you've stolen the Pirates' booty."
        pause

    label .accepted:
        $ progress["quests"]["ninjas"]["accepted"] = True
        scene bg room_arcade
        show smoke_cloud
        show smoke_plume
        if inventory["smoke"]["active"] == False:
            $ inventory["smoke"]["active"] = True
        pause 1.0
        scene bg room_arcade
        call screen interact_arcade

label arcade_land_mines:
    screen interact_arcade_land_mines():
        frame:
            pos (0.0, 0.8)
            textbutton "arcade":
                xysize (1.0, 0.2)
                action [
                    Jump("arcade")
                ]

    # TODO: v4.1.0
    scene bg room_arcade_out_of_order with fade
    call screen interact_arcade_out_of_order

label arcade_do_or_die:
    screen interact_arcade_do_or_die():
        frame:
            pos (0.0, 0.8)
            textbutton "arcade":
                xysize (1.0, 0.2)
                action [
                    Jump("arcade")
                ]

    # TODO: v4.1.0
    scene bg room_arcade_do_or_die with fade
    call screen interact_arcade_do_or_die

label arcade_out_of_order:
    screen interact_arcade_out_of_order():
        frame:
            pos (0.0, 0.8)
            textbutton "arcade":
                xysize (1.0, 0.2)
                action [
                    Jump("arcade")
                ]

    scene bg room_arcade_out_of_order with fade
    call screen interact_arcade_out_of_order