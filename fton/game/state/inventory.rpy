default inventory = {
    "beer": {
        "active": False,
        "highlight": False,
    },
    "bomb": {
        "active": False,
        "highlight": False,
        "disabled": [
            "balcony.accepted",
            "pier.dive",
            "pier.harpoon",
            "ship.fight",
            "ship.shot_captain",
            "ship.shot_mermaid",
            "drowned",
            "pipe.quest",
            "pirate_quest_complete",
            "mermaids_revenge",
            "mermaid_quest_complete",
            "treasure",
            "ninja_quest_complete",
            "temple_raid_shootout",
            "temple_raid_shootout.beheaded",
            "temple_raid_shootout.clear",
            "monk_boss",
            "beheaded_death",
            "police_quest_complete",
            "jail",
            "arrested",
            "toilet.quest",
            "final_quest_start",
            "final_quest_start.talk",
            "final_quest_cutscene",
            "final_quest_cutscene.freed",
            "final_quest_cutscene.freed",
            "final_quest_cutscene.taken",
            "final_quest_cutscene.skyline",
        ]
    },
    "cash": {
        "active": False,
        "highlight": False,
    },
    "genie": {
        "active": False,
        "highlight": False,
        "actions": {
            "final_quest_start": [
                Jump("final_quest_cutscene")
            ],
            "final_quest_start.talk": [
                Jump("final_quest_cutscene")
            ],
        }
    },
    "helmet": {
        "active": False,
        "highlight": False,
    },
    "key": {
        "active": False,
        "highlight": False,
        "actions": {
            "cliefwood.locked_house": [
                Jump("cliefwood.unlocked")
            ],
        }
    },
    "letter": {
        "active": False,
        "highlight": False,
    },
    "noodles": {
        "active": False,
        "highlight": False,
    },
    "radio": {
        "active": False,
        "highlight": False,
        "actions": {
            "temple": [
                Hide("interact_temple"),
                Jump("temple_raid")
            ],
            "temple.talk": [
                Hide("interact_temple"),
                Jump("temple_raid")
            ],
        }
    },
    "sawnoff": {
        "active": False,
        "highlight": False,
        "ammo": 2,
    },
    "shotgun": {
        "active": False,
        "highlight": False,
        "ammo": 1,
    },
    "smoke": {
        "active": False,
        "highlight": False,
        "actions": {
            "pub": [
                Hide("interact_pub"),
                Jump("pub_smoke")
            ],
            "pub.shout": [
                Hide("interact_pub"),
                Jump("pub_smoke")
            ],
            "corner_store": [
                Jump("corner_store_smoke")
            ],
        }
    },
    "wrench": {
        "active": False,
        "highlight": False,
        "actions": {
            "hydrant": [
                Jump("mermaids_revenge")
            ],
            "hydrant.use": [
                Jump("mermaids_revenge")
            ],
        }
    },
}

screen hud_inventory():
    zorder 100
    hbox:
        align (1.0, 1.0)
        for i, item in enumerate(inventory):
            if progress["cheats"]:
                $ icon = (item+"_active" if inventory[item]["active"] else item)
                imagebutton:
                    padding (0, 0, 6, 6)
                    auto icon+"_%s"
                    if inventory[item]["highlight"]:
                        action inventory[item]["actions"].get(current_label, NullAction())
                    elif item == "bomb" and inventory["bomb"]["active"] and (progress["night"] == False):
                        if current_label not in inventory["bomb"]["disabled"]:
                            action Jump("explode")
                    else:
                        action ToggleDict(inventory[item], "active")
            elif inventory[item]["active"]:
                $ icon = (item+"_active" if inventory[item]["highlight"] else item)
                imagebutton:
                    padding (0, 0, 6, 6)
                    auto icon+"_%s"
                    if inventory[item]["highlight"]:
                        action inventory[item]["actions"].get(current_label, NullAction())
                    elif item == "bomb" and inventory["bomb"]["active"]:
                        action Jump("explode")