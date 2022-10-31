label pats_house:
    screen interact_pats_house():
        frame:
            pos (0, 0.8)
            textbutton "cliefwood":
                xysize (1.0, 0.2)
                action [
                    Jump("cliefwood")
                ]

    scene bg room_pats_house with fade
    "Nobody is home.{w=2}{nw}"
    call screen interact_pats_house

label empty_house:
    screen interact_empty_house():
        frame:
            pos (0, 0.8)
            textbutton "cliefwood":
                xysize (1.0, 0.2)
                action [
                    Jump("cliefwood")
                ]

    scene bg room_empty_house with fade
    "Nobody is home.{w=2}{nw}"
    call screen interact_empty_house

label cliefwoods_house:
    # Sprites
    image bg room_cliefwoods_house:
        "bg room_cliefwoods_1.png"
        pause 0.25
        "bg room_cliefwoods_2.png"
        pause 0.25
        repeat
    
    scene bg room_cliefwoods_house with fade
    orange_narwhal "Do you mind?"
    scene bg plain_charcoal with fade
    centered "The End."
    jump evaluation