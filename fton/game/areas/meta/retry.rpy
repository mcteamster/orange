label game_over:
    # Screens
    hide screen pumping
    hide screen reloading

    # Script
    scene bg plain_black
    show beer_empty:
        align (0.5, 1.0)
        pos (0.5, 0.66)
    show beer_full:
        align (0.5, 1.0)
        pos (0.5, 0.66)
        crop (0.0, 0.0, 1.0, 1.0)
        pause 0.5
        linear 1.0 crop (0.0, 1.0, 1.0, 0.0)
    with fade
    pause 1.0
    "Click to refill..."
    show beer_full:
        crop (0.0, 1.0, 1.0, 0.0)
        linear 0.5 crop (0.0, 0.0, 1.0, 1.0)
    $ progress["lives"] += 1
    $ beer_counter = "My Tab: "+str(progress["lives"])+" Beers..."
    "[beer_counter]"
    jump start