label evaluation:
    # Settings
    $ achievement.grant("found")
    $ achievement.sync()

    $ attempts = "Final Tab:\n"+str(progress["lives"])+(" Beers" if progress["lives"] > 1 else " Beer")
    if (progress["lives"] == 1):
        $ achievement.grant("perfect")
        $ achievement.sync()

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

    # Screens
    screen evaluation_results():
        text "[attempts]":
            pos (0.15, 0.2)
            text_align 0.5
            size 100
        text "Stats Online":
            pos (0.87, 0.93)
            size 40
        vbox:
            align (0.85, 0.5)
            spacing 150
            text "You [pirates_result] the Pirates"
            text "You [ninjas_result] the Ninjas"
            text "You [police_result] the Police"
            text "You [clowns_result] the Clowns"
            text "You [mermaids_result] the Mermaids"
        frame:
            pos (0.85, 0.9)
            textbutton "open_stats":
                xysize (0.15, 0.1)
                action [
                    Jump("evaluation.open_stats")
                ]

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
        $ achievement.grant("king")
        $ achievement.sync()
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
    jump couch

    label .open_stats:
        python:
            try:
                # Have to use urllib for web support
                from urllib import request, parse
                params = parse.urlencode({
                    'event': 'fton/endgame',
                    'meta': {
                        'attempts': progress["lives"],
                        'quests': progress["quests"],
                    }
                })
                url = f"https://orange.mcteamster.com/stats.html?{params}"
                renpy.run(OpenURL(url))
            except Exception as e:
                print(e)
        jump couch

label couch:
    hide screen evaluation_results
    scene bg meta_endgame_couch
    hide screen hud_inventory
    show cutscene_top onlayer screens
    show cutscene_bottom onlayer screens
    with fade
    pause 1.0
    purple_duck "So are we having another big one tonight?"
    $ renpy.full_restart()