# Harpoon
image ship_harpoon:
    "pirate/harpoon_wield.png"
    align (1.0, 1.0)
    pos (1.05, 2.0)
    easein 1.0 ypos 1.05

image ship_harpoon empty:
    "pirate/harpoon_wield_empty.png"
    align (1.0, 1.0)
    pos (1.05, 1.05)
    pause 1.0
    easeout 1.0 ypos 2.0

image ship_harpoon_stream:
    "pirate/harpoon_stream.png"
    zoom 0.8
    alpha 1.0
    align (0.0, 0.0)
    pos (0.5, 0.38)
    linear 0.25 alpha 0.0
    
# Sawnoff
image sawnoff:
    "misc/wield_sawnoff.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)

image sawnoff equip:
    "misc/wield_sawnoff.png"
    align (0.5, 0.5)
    pos (0.85, 2.0)
    easein 0.5 ypos 0.85

image sawnoff unequip:
    "misc/wield_sawnoff.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)
    easeout 0.5 ypos 2.0

image sawnoff shoot:
    "misc/wield_sawnoff.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)
    zoom 1
    easeout 0.1 rotate 5 zoom 1.1
    easeout 0.1 rotate 0 zoom 1

image sawnoff_base:
    "misc/reload_sawnoff_base.png"
    align (0.5, 0.5)
    pos (0.8, 0.8)

image sawnoff_barrel:
    "misc/reload_sawnoff_barrel.png"
    align (0.5, 0.5)
    pos (0.825, 0.46)

image sawnoff_shells:
    "misc/reload_sawnoff_shells.png"
    align (0.5, 0.5)
    pos (0.8425, 0.61)
    linear 0.25 pos (0.95, 1.1)
    pause 0.25
    linear 0.5 pos (0.8425, 0.61)

image sawnoff_hand:
    "misc/reload_sawnoff_hand.png"
    align (0.5, 0.5)
    pos (1.2, 1.5)
    pause 0.5
    linear 0.5 pos (1.0, 0.8)
    linear 0.5 pos (1.2, 1.5)

image sawnoff_flash:
    "misc/muzzle_flash.png"
    align (0.5, 0.5)
    pos (0.75, 0.6)
    alpha 1.0
    pause 0.1 alpha 0.0

label sawnoff:
    label .shoot(origin, target, enemies, damage=1):
        if inventory["sawnoff"]["ammo"] > 0:
            $ inventory["sawnoff"]["ammo"] -= 1
            if target is not None: 
                if isinstance(enemies, list):
                    $ enemies.remove(target)
                elif isinstance(enemies, dict):
                    if enemies[target] >= damage:
                        $ enemies[target] -= damage
                        $ enemies["total"] -= damage
                    else:
                        $ enemies["total"] -= enemies[target]
                        $ enemies[target] = 0
            show sawnoff_flash onlayer screens zorder 50
            show sawnoff shoot onlayer screens zorder 51
            if inventory["sawnoff"]["ammo"]//2 == 1:
                play audio "audio/sawnoff.wav"
            else:
                play audio "audio/sawnoff.wav"
            if len(enemies) == 0:
                pause 0.5
                jump expression origin+".clear"
            return
        else:
            jump sawnoff.reload

    label .reload:
        screen reloading():
            button action NullAction()

        $ inventory["sawnoff"]["ammo"] = 2
        show screen reloading
        hide sawnoff onlayer screens
        show sawnoff_base onlayer screens zorder 52
        show sawnoff_shells onlayer screens zorder 52
        show sawnoff_barrel onlayer screens zorder 52
        show sawnoff_hand onlayer screens zorder 52
        play audio "audio/reload.wav"
        pause 1.5
        show sawnoff onlayer screens zorder 50
        hide sawnoff_base onlayer screens zorder 52
        hide sawnoff_shells onlayer screens zorder 52
        hide sawnoff_barrel onlayer screens zorder 52
        hide sawnoff_hand onlayer screens zorder 52
        hide screen reloading
        return

# Shotgun
image shotgun:
    "misc/wield_shotgun.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)

image shotgun equip:
    "misc/wield_shotgun.png"
    align (0.5, 0.5)
    pos (0.85, 2.0)
    easein 0.5 ypos 0.85

image shotgun unequip:
    "misc/wield_shotgun.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)
    easeout 0.5 ypos 2.0

image shotgun shoot:
    "misc/wield_shotgun.png"
    align (0.5, 0.5)
    pos (0.85, 0.85)
    zoom 1
    easeout 0.1 rotate 5 zoom 1.1
    easeout 0.1 rotate 0 zoom 1

image shotgun pump:
    "misc/pump_shotgun.png"
    align (0.5, 0.5)
    pos (0.8585, 0.8639)
    zoom 1

image shotgun_flash:
    "misc/muzzle_flash.png"
    align (0.5, 0.5)
    pos (0.75, 0.6)
    alpha 1.0
    pause 0.1 alpha 0.0

label shotgun:
    label .shoot(origin, target, enemies, damage=1):
        screen pumping():
            button action NullAction()

        show screen pumping
        if target is not None: 
            if origin != "temple_raid_shootout":
                if isinstance(enemies, list):
                    $ enemies.remove(target)
                elif isinstance(enemies, dict):
                    if enemies[target] >= damage:
                        $ enemies[target] -= damage
                        $ enemies["total"] -= damage
                    else:
                        $ enemies["total"] -= enemies[target]
                        $ enemies[target] = 0
            elif (temple_raid_shootout_time % 6)//2 == int(target[-1])-1:
                $ enemies.remove(target)

        show shotgun_flash onlayer screens zorder 50
        show shotgun shoot onlayer screens zorder 51
        play audio "audio/shotgun.wav"
        pause 0.5
        show shotgun pump onlayer screens zorder 50
        pause 0.5
        $ inventory["shotgun"]["ammo"] = 1
        show shotgun onlayer screens zorder 50
        hide screen pumping
        if len(enemies) == 0:
            pause 0.5
            jump expression origin+".clear"
        return

# Bomb
label explode:
    screen interact_explode():
        button action NullAction()

    $ inventory["bomb"]["active"] = False
    scene bg plain_black
    show screen interact_explode
    play audio "audio/explosion.wav"
    show self_exploded:
        align (0.5, 0.5)
        pos (0.5, 1.5)
        zoom 1
        pause 0.25
        linear 4.0 zoom 0.5 ypos 0.8
    show explosion_smoke:
        align (0.5, 0.5)
        pos (0.5, 0.55)
        zoom 2
        alpha 1.0
        linear 2.0 zoom 2.5 ypos 0.35 alpha 0.0
    show explosion_flash:
        align (0.5, 0.5)
        pos (0.5, 0.55)
        zoom 3
        alpha 1.0
        linear 0.25 zoom 4.5 alpha 0.0
    with vpunch
    pause 0.5
    play audio "audio/bell.wav"
    pause 4.0
    hide screen interact_explode
    $ inventory["bomb"]["active"] = True
    jump game_over