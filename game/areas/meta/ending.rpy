init python:
    import requests

label evaluation:
    # Settings
    $ attempts = "Final Tab:\n"+str(progress["lives"])+(" Beers" if progress["lives"] > 1 else " Beer")
    $ pirates_result = "{color=#ff0}EXPLOITED{/color}" if (progress["quests"]["pirates"]["complete"] or inventory["helmet"]["active"]== False) else "{color=#f00}BETRAYED{/color}"
    $ ninjas_result = "{color=#f00}BETRAYED{/color}" if (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]) else "{color=#0f0}HELPED{/color}"
    
    if (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]) and (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]):
        $ police_result = "{color=#ff0}EXPLOITED{/color}"
    elif (progress["quests"]["police"]["complete"] or inventory["shotgun"]["active"]):
        $ police_result = "{color=#0f0}HELPED{/color}"
    else:
        $ police_result = "{color=#f00}KILLED{/color}"
    
    if (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]) and (progress["quests"]["mermaids"]["complete"] or inventory["helmet"]["active"]):
        $ clowns_result = "{color=#ff0}EXPLOITED{/color}"
    elif (progress["quests"]["clowns"]["complete"] or inventory["sawnoff"]["active"]):
        $ clowns_result = "{color=#0f0}HELPED{/color}"
    elif (progress["quests"]["mermaids"]["complete"] or inventory["helmet"]["active"]):
        $ clowns_result = "{color=#f00}KILLED{/color}"
    else:
        $ clowns_result = "{color=#ff0}IGNORED{/color}"

    $ mermaids_result = "{color=#0f0}HELPED{/color}" if (progress["quests"]["mermaids"]["complete"] or inventory["helmet"]["active"]) else "{color=#f00}NEGLECTED{/color}"

    python:
        try:
            requests.post("https://fton-service.ohnomer.com/track", json={ 'event': 'fton-endgame', 'attempts': progress["lives"], 'quests': progress["quests"] }, timeout=3)
        except Exception as e:
            print(e)

    # Screens
    screen evaluation_results():
        text "[attempts]":
            pos (0.15, 0.2)
            text_align 0.5
            size 100
        vbox:
            align (0.85, 0.5)
            spacing 150
            text "You [pirates_result] the Pirates"
            text "You [ninjas_result] the Ninjas"
            text "You [police_result] the Police"
            text "You [clowns_result] the Clowns"
            text "You [mermaids_result] the Mermaids"

    # Sprites
    image endgame_crown:
        "meta/crown.png"
        align (0.5, 0.5)
        pos (0.25, 0.475)
        rotate 0
        xzoom 1.14

    # Script
    scene bg plain_charcoal
    hide screen hud_inventory
    hide screen help_button
    show faction_faces:
        align (0.0, 0.5)
        pos (0.55, 0.5)
    show beer_empty:
        align (0.5, 1.0)
        pos (0.25, 0.85) 
    if inventory["shotgun"]["active"] and inventory["sawnoff"]["active"]:
        show endgame_crown
    show beer_full:
        align (0.5, 1.0)
        pos (0.25, 0.85)
        crop (0.0, 0.0, 1.0, 1.0)
    show screen evaluation_results
    with fade
    show beer_full:
        linear 4.0 crop (0.0, 1.0, 1.0, 0.0)
    pause
    hide screen evaluation_results
    scene bg meta_endgame_couch
    hide screen hud_inventory
    show cutscene_top onlayer screens
    show cutscene_bottom onlayer screens
    with fade
    pause 1.0
    purple_duck "So are we having another big one tonight?{w=4}{nw}"
    $ renpy.full_restart()