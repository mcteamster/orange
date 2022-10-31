label splashscreen:
    # Screens
    screen skip_splash():
        button action [
            Hide(),
            Jump("splashscreen.title")
        ]
    
    # Script
    show cutscene_top onlayer screens
    show cutscene_bottom onlayer screens
    show screen skip_splash

    label .tv:
        scene bg splash_tv
        show tv_static:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            linear 4.0 xpos 0.45
        with fade
        pause 3.0
    
    label .table:
        scene bg splash_table
        show table_bottles:
            align (0.5, 0.5)
            pos (0.5, 0.5)
            linear 4.0 xpos 0.45
        pause 4.0

    label .couch:
        scene bg splash_couch
        show couch_sleeping:
            align (0.5, 0.5)
            pos (0.55, 0.45)
            linear 4.0 xpos 0.45
        show couch_table:
            align (0.5, 1.0)
            pos (0.5, 1.0)
            linear 4.0 xpos 0.35
        pause 4.0

    label .tv_reach:
        scene bg plain_darkgrey
        show tv_angled:
            align (0.5, 0.5)
            pos (0.55, 0.75)
            linear 4.0 xpos 0.75
        show reaching_hand:
            align (0.5, 0.5)
            pos (0.4, 0.5)
            crop (0, 0, 0.0, 1.0)
            linear 4.0 crop (0, 0, 1.0, 1.0)
        pause 4.0

    label .wake:
        scene bg splash_wake
        show looming_shadow:
            align (0.5, 0.5)
            pos (1.0, 0.75)
            linear 2.5 xpos 0.75
        pause 3.0
        show bg splash_wake_open
        pause 1.0
        
    label .neighbour:
        scene bg splash_neighbour
        pause 1.0
        "Where {w=0.75}{nw}"
        extend "the {w=0.75}{nw}"
        extend "HECK {w=1}{nw}" with vpunch
        extend "is {w=0.25}{nw}"
        extend "my {w=0.25}{nw}"
        extend "Orange {w=1}{nw}" with vpunch
        extend "Narwhal?{w=2}{nw}" with vpunch

    label .panic:
        scene bg splash_panic
        "Oh heck! What did we do with that Narwhal?{w=2}{nw}"
        "I don't remember a thing from last night!{w=2}{nw}"

    label .ohnomer:
        scene bg plain_charcoal
        show cutscene_top exit onlayer screens
        show cutscene_bottom exit onlayer screens
        centered "Ohnomer presents...{w=4}{nw}"

    label .title:
        scene bg splash_title
        hide screen skip_splash
        hide cutscene_top onlayer screens
        hide cutscene_bottom onlayer screens
        pause 2.0