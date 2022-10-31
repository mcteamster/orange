label stairs:
    # Screens
    screen interact_stairs():
        frame:
            pos (0.0, 0.13)
            textbutton "vault":
                xysize (0.245, 0.66)
                action [
                    Jump("vault")
                ]
        frame:
            pos (0.33, 0.13)
            textbutton "foyer_exit":
                xysize (0.34, 0.69)
                action [
                    Jump("foyer_exit")
                ]
        frame:
            pos (0.75, 0.13)
            textbutton "vault":
                xysize (0.245, 0.66)
                action [
                    Jump("vault")
                ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg bank_stairs_night
    else:
        scene bg bank_stairs
    with fade
    call screen interact_stairs

label vault:
    # Screens
    screen interact_vault():
        frame:
            pos (0.19, 0.25)
            textbutton "stairs":
                xysize (0.15, 0.38)
                action [
                    Jump("stairs")
                ]
        frame:
            pos (0.655, 0.25)
            textbutton "stairs":
                xysize (0.15, 0.38)
                action [
                    Jump("stairs")
                ]
        frame:
            pos (0.4, 0.22)
            textbutton "inspect":
                xysize (0.195, 0.35)
                if (progress["night"] or inventory["key"]["active"]):
                    action [
                        Jump("inner_vault")
                    ]
                else:
                    action [
                        Jump("vault.inspect")
                    ]

    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg bank_vault_night
    else:
        scene bg bank_vault 
    with fade
    call screen interact_vault

    label .inspect:
        "Maybe the Orange Narwhal is in there?{w=2}{nw}"
        call screen interact_vault

label inner_vault:
    # Screens
    screen interact_inner_vault():
        button action NullAction()
        frame:
            pos (0.62, 0.05)
            textbutton "take_sawnoff":
                xysize (0.1, 0.59)
                action [
                    Hide(),
                    Jump("inner_vault.armed")
                ]
    
    screen interact_inner_vault_night():
            frame:
                pos (0.4, 0.22)
                textbutton "vault":
                    xysize (0.195, 0.35)
                    action [
                        Jump("vault")
                    ]
            if (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]):
                frame:
                    pos (0, 0.8)
                    textbutton "backroom":
                        xysize (1.0, 0.20)
                        action [
                            Jump("backroom")
                        ]

    # Sprites
    image inner_vault_clown:
        "clown/clown_no_arm.png"
        align (1.0, 0)
        pos (0.0, 0.03)
        linear 0.5 xpos 0.64

    image inner_vault_clown_arm:
        "clown/clown_arm.png"
        align (1.0, 0)
        pos (0.0, 0.67)
        linear 0.5 xpos 0.64

    image inner_vault_clown_sawnoff_arm:
        "clown/clown_sawnoff_arm.png"
        align (0, 0)
        pos (0.6, 0.04)
        
    # Script
    if (progress["night"] or inventory["key"]["active"]):
        scene bg bank_inner_vault_night with fade
        call screen interact_inner_vault_night
    else:
        scene bg bank_inner_vault with fade
        show clown_no_arm:
            align (1.0, 0)
            pos (0.0, 0.03)
            linear 0.5 xpos 0.64
        show clown_arm:
            align (1.0, 0)
            pos (0.0, 0.67)
            linear 0.5 xpos 0.64
        clown "We've hit the jackpot!"
        clown "But we're going to need an extra pair of hands up front."
        hide clown_arm
        show clown_sawnoff_arm:
            align (0, 0)
            pos (0.6, 0.04)
        show screen interact_inner_vault
        clown "Here, take this!"
        pause

    label .armed:
        screen interact_inner_vault_armed():
            button action NullAction()
            frame:
                pos (0.4, 0.22)
                textbutton "bank_foyer_shootout":
                    xysize (0.195, 0.35)
                    action [
                        Hide(),
                        Jump("inner_vault.leave")
                    ]

        $ inventory["sawnoff"]["active"] = True
        hide clown_sawnoff_arm
        show clown_arm:
            align (1.0, 0)
            pos (0.64, 0.67)
            linear 0.5 xpos 0.0
        show clown_no_arm:
            align (1.0, 0)
            pos (0.64, 0.03)
            linear 0.5 xpos 0.0
        pause 0.5
        show screen interact_inner_vault_armed
        show sawnoff equip onlayer screens zorder 50
        pause

    label .leave:
        show sawnoff unequip onlayer screens zorder 50
        pause 0.5
        hide sawnoff onlayer screens
        hide sawnoff_flash onlayer screens
        $ inventory["sawnoff"]["ammo"] = 2
        jump bank_foyer_shootout