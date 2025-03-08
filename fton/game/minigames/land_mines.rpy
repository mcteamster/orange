label land_mines:
    # Script
    scene bg plain_charcoal
    hide screen hud_inventory
    with fade


    label .play:
        # Settings
        $ minefield = []
        $ land_mines_time = 0.0
        $ progress["minigames"]["land_mines"]["tripped"] = False
        $ progress["minigames"]["land_mines"]["remaining"] = 81
        $ progress["minigames"]["land_mines"]["victory"] = False
        python:
            # Init Squares
            for y in range(0, 9):
                row = []
                for x in range(0, 9):
                    row.append({
                        "row": y,
                        "col": x,
                        "revealed": False,
                        "value": "0"
                    })
                minefield.append(row)

            # Seed Mines
            mines = 10
            while mines > 0:
                x = renpy.random.randint(0, 8)
                y = renpy.random.randint(0, 8)
                if minefield[y][x]["value"] != "-1":
                    minefield[y][x]["value"] = "-1" # -1 is a Mine
                    mines -= 1

            # Seed Values
            for y in range(0, 9):
                for x in range(0, 9):
                    if minefield[y][x]["value"] != "-1":
                        adjacent = 0
                        for a in range(x-1, x+2):
                            for b in range(y-1, y+2):
                                if a >= 0 and a <=8 and b >=0 and b <= 8:
                                    if minefield[b][a]["value"] == "-1":
                                        adjacent += 1
                        minefield[y][x]["value"] = str(adjacent)

        # Reveal
        init python:
            def reveal(x, y):
                if progress["minigames"]["land_mines"]["tripped"] == False:
                    minefield[y][x]["revealed"] = True
                    if minefield[y][x]["value"] == "-1":
                        progress["minigames"]["land_mines"]["tripped"] = True
                        renpy.music.play("audio/explosion.wav", channel="audio")
                    else:
                        progress["minigames"]["land_mines"]["remaining"] -= 1
                        if minefield[y][x]["value"] == "0":
                            for a in range(x-1, x+2):
                                for b in range(y-1, y+2):
                                    if a >= 0 and a <=8 and b >=0 and b <= 8:
                                        if minefield[b][a]["revealed"] != True:
                                            reveal(a, b)
                        if progress["minigames"]["land_mines"]["remaining"] <= 10:
                            progress["minigames"]["land_mines"]["victory"] = True
                            if land_mines_time < progress["minigames"]["land_mines"]["highscore"]:
                                progress["minigames"]["land_mines"]["highscore"] = land_mines_time

            # Check for victory
                # total = 0
                # for y in range(0, 9):
                #     total += functools.reduce(lambda remaining, square : remaining + 1 if square["revealed"] == False, minefield[y], 0)

        # Screens
        screen land_mines_field():
            button action NullAction()
            frame:
                pos (0.02, 0.8625)
                textbutton "play":
                    xysize (0.11, 0.09)
                    action [
                        Jump("land_mines.play")
                    ]
            frame:
                pos (0.865, 0.8625)
                textbutton "quit":
                    xysize (0.11, 0.09)
                    action [
                        Hide("land_mines_timer"),
                        Hide(),
                        Jump("land_mines.quit")
                    ]
            frame:
                align (0.5, 0.5)
                pos (0.5, 0.5)
                vbox:
                    for row in minefield:
                        hbox:
                            for square in row:
                                frame:
                                    if square["revealed"] == False:
                                        imagebutton:
                                            idle "unrevealed"
                                            action [
                                                Function(reveal, square["col"], square["row"])
                                            ]
                                    else:
                                        imagebutton:
                                            idle square["value"]
                                            action NullAction()

        screen land_mines_timer():
            timer 0.1:
                repeat True
                if progress["minigames"]["land_mines"]["victory"] == True:
                    action [
                        Hide(),
                        Jump("land_mines.win")
                    ]
                elif progress["minigames"]["land_mines"]["tripped"] == False:
                    action [
                        SetVariable('land_mines_time', land_mines_time + 0.1),
                    ]
            text "TIME: [land_mines_time:0.1f]":
                align (0.37, 0.02)
            $ highscore = progress["minigames"]["land_mines"]["highscore"]
            text "RECORD: [highscore:0.1f]":
                align (0.63, 0.02)

        scene land_mines_title
        show screen land_mines_field
        show screen land_mines_timer
        pause

    label .win:
        pause 1.0
        scene land_mines_win
        hide screen land_mines_field
        pause 2.0
        jump land_mines.play

    label .quit:
        scene bg plain_charcoal 
        show screen hud_inventory
        with None
        jump arcade

