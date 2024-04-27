label balcony:
    # Settings
    $ inventory["smoke"]["highlight"] = False

    screen interact_balcony():
        frame:
            pos (0.0, 0.8)
            textbutton "pub":
                xysize (1.0, 0.2)
                action [
                    Jump("pub")
                ]
        if (inventory["beer"]["active"] == False and progress["quests"]["pirates"]["complete"] == False):
            frame:
                pos (0.38, 0.22)
                textbutton "quest_captain":
                    xysize (0.085, 0.41)
                    action [
                        Jump("balcony.quest")
                    ]

    $ balcony_scene = "bg dock_balcony"
    if progress["quests"]["pirates"]["complete"] or (inventory["beer"]["active"] and inventory["helmet"]["active"] == False):
        $ balcony_scene += "_beer"
    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        $ balcony_scene += "_eve"    
    scene expression balcony_scene with fade
    call screen interact_balcony

    label .quest:
        screen interact_balcony_quest():
            modal True
            frame:
                pos (0.0, 0.8)
                textbutton "balcony":
                    xysize (1.0, 0.2)
                    action [
                        Hide(),
                        Jump("balcony")
                    ]
            frame:
                pos (0.2, 0.3)
                textbutton "take_helmet":
                    xysize (0.175, 0.43)
                    action [
                        Hide(),
                        Jump("balcony.accepted")
                    ]

        image balcony_captain:
            "pirate/captain.png"
            zoom 0.8
            align (0.61, 0.0)
            ypos 0.06
        image balcony_hook_hand:
            "pirate/hook_hand.png"
            zoom 0.8
            align (0.37, 0.83)
        image balcony_hook_hand bent:
            "pirate/hook_hand.png"
            zoom 0.8
            rotate 60
            align (0.30, 0.70)
        image balcony_helmet:
            "pirate/helmet_glow.png"
            zoom 0.8
            align (0.245, 0.53)

        show bg dock_balcony_empty
        show balcony_captain
        show balcony_hook_hand
        with fade
        captain "Arr. The Orange Narwhal? She be but a myth dreamt up by a weary sailor surely."
        captain "Mermaids, on the other hook, be real and dangerous."
        captain "Arr, dastardly Mermaids sunk our ship whilst it lay docked in port."
        captain "All our cargo was sent to the bottom of the ocean."
        captain "But with these here {i}helmets{/i} we can venture to the depths and reclaim our {i}beer{/i}."
        captain "Help me kill the retched Mermaids and ye be greatly rewarded!"
        show balcony_hook_hand bent
        show balcony_helmet
        show screen interact_balcony_quest
        $ progress["quests"]["pirates"]["offered"] = True
        captain "Here. Take this {i}helmet{/i} if yer be brave enough to dive with me!"
        pause

    label .accepted:
        $ progress["quests"]["pirates"]["accepted"] = True
        if inventory["beer"]["active"] == False:
            $ inventory["helmet"]["active"] = True
        hide interact_balcony_quest
        show balcony_hook_hand -bent
        hide balcony_helmet
        captain "Arr! I knew yer be the scallywag for the job!"
        captain "Meet me down by the dock and we shall grab us some wretched Mermaids!"
        jump pier.dive

label pirate_quest_complete:
    $ achievement.grant("pirates")
    $ achievement.sync()
    screen interact_pirate_quest_complete():
        modal True
        frame:
            pos (0.21, 0.35)
            textbutton "take_beer":
                xysize (0.15, 0.35)
                action [
                    Hide(),
                    SetDict(inventory["beer"], "active", True),
                    SetDict(progress["quests"]["pirates"], "complete", True),
                    SetDict(progress["quests"]["mermaids"], "disabled", True),
                    Jump("balcony")
                ]

    image balcony_beer:
        "pirate/beer_glow.png"
        align (0.245, 0.55)

    $ inventory["helmet"]["active"] = False
    scene bg dock_balcony_empty
    show balcony_captain
    show balcony_hook_hand
    with fade
    captain "Yo Ho! We've returned with our stolen {i}beer{/i}!"
    captain "You, good matey, are a true friend of the Pirates!"
    show balcony_hook_hand bent
    show balcony_beer
    show screen interact_pirate_quest_complete
    captain "Here. Have a keg of our finest {i}beer{/i}!"
    pause