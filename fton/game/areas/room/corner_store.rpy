label corner_store:
    # Settings
    if inventory["smoke"]["active"]:
        $ inventory["smoke"]["highlight"] = True

    screen interact_corner_store():
        frame:
            pos (0, 0.8)
            textbutton "downtown":
                xysize (1.0, 0.2)
                action [
                    Jump("downtown")
                ]
        frame:
            pos (0.47, 0.34)
            textbutton "shopkeeper":
                xysize (0.05, 0.15)
                action [
                    Jump("corner_store.shopkeeper")
                ]
        frame:
            pos (0.17, 0.46)
            textbutton "power_paint":
                xysize (0.045, 0.13)
                action [
                    Jump("corner_store.touch")
                ]
        frame:
            pos (0.41, 0.55)
            textbutton "harpoon":
                xysize (0.18, 0.06)
                action [
                    Jump("corner_store.touch")
                ]
        frame:
            pos (0.77, 0.71)
            textbutton "horn":
                xysize (0.19, 0.05)
                action [
                    Jump("corner_store.touch")
                ]

    screen interact_corner_store_shopkeeper():
        frame:
            pos (0, 0.8)
            textbutton "corner_store":
                xysize (1.0, 0.2)
                action [
                    Jump("corner_store")
                ]

    scene bg room_corner_store with fade
    "Hmmmm... Some of this stuff looks like it might come in handy.{w=2}{nw}"
    call screen interact_corner_store

    label .touch:
        ben "You going to pay for that? No? Then don't touch it.{w=2}{nw}"
        call screen interact_corner_store

    label .shopkeeper:    
        $ inventory["smoke"]["highlight"] = False
        scene bg room_corner_store_shopkeeper with fade
        ben "An Orange Narwhal? I don't have any of those.{w=2}{nw}"
        ben "I only have Red Herrings.{w=2}{nw}"
        call screen interact_corner_store_shopkeeper

label corner_store_smoke:
    screen interact_corner_store_smoke():
        button action NullAction()
        frame:
            pos (0, 0.8)
            textbutton "downtown":
                xysize (1.0, 0.2)
                action [
                    Hide(),
                    Jump("downtown")
                ]
        frame:
            pos (0.17, 0.46)
            textbutton "power_paint":
                xysize (0.045, 0.13)
                action [
                    Hide(),
                    Jump("corner_store_smoke.steal")
                ]
        frame:
            pos (0.41, 0.55)
            textbutton "harpoon":
                xysize (0.18, 0.06)
                action [
                    Hide(),
                    Jump("corner_store_smoke.steal")
                ]
        frame:
            pos (0.77, 0.71)
            textbutton "horn":
                xysize (0.19, 0.05)
                action [
                    Hide(),
                    Jump("corner_store_smoke.steal")
                ]

    $ inventory["smoke"]["active"] = False
    $ inventory["smoke"]["highlight"] = False
    $ print(renpy.current_screen())
    scene bg room_corner_store
    show screen interact_corner_store_smoke
    show smoke_thrown
    pause 0.75
    play audio "audio/pop.wav"
    hide smoke_thrown
    show smoke_plume
    show smoke_bang
    show smoke_cloud
    show smoke_veil_5
    show smoke_veil_4
    show smoke_veil_3
    show smoke_veil_2
    show smoke_veil_1
    ben "What the hell?{w=2}{nw}"
    pause 8
    hide screen interact_corner_store_smoke
    call screen interact_corner_store

    label .steal:
        image power_paint:
            "misc/power_paint.png"
            align (0.5, 0.2)
            pause 0.5
            linear 0.5 ypos 1.2

        image horn_1:
            "misc/horn.png"
            align (1.3, 2.2)
            zoom 0.8
            rotate 165

        image horn_2:
            "misc/horn.png"
            align (-0.5, -5.5)
            rotate -15

        image horn_3:
            "misc/horn.png"
            align (0.5, 0.9)
            zoom 0.9
            pause 0.5
            linear 0.5 ypos 1.3

        image store_harpoon:
            "misc/harpoon.png"
            align (0.5, 2.5)
            pause 0.5
            linear 0.5 ypos 4.0

        image swipe_arm:
            "misc/stealing_arm.png"
            align (0.5, 0.0)
            pos (0.5, 1.0)
            rotate 90
            linear 0.5 ypos 0.2
            linear 0.5 ypos 1.2


        scene bg room_corner_store_shelf
        show smoke_veil_10 zorder 2
        show smoke_veil_9 zorder 2
        show smoke_veil_8 zorder 2
        show smoke_veil_7 zorder 2
        show smoke_veil_6 zorder 2
        show power_paint
        show swipe_arm zorder 1
        pause 1.0
        hide power_paint
        show horn_1
        show horn_2
        show horn_3
        show swipe_arm zorder 1
        pause 1.0
        hide horn_1
        hide horn_2
        hide horn_3
        show store_harpoon
        show swipe_arm zorder 1
        pause 1.0
        scene bg street_police_west with fade
        show arrest_officer_left
        show arrest_officer_right
        officer "If you're going to rob a store, maybe don't pick the one right next to a Police station...{w=2}{nw}"
        jump arrested