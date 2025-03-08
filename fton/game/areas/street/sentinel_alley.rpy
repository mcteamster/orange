label sentinel_alley:
    screen interact_sentinel_alley():
        frame:
            pos (0, 0)
            textbutton "corner_store_south":
                xysize (0.23, 1.0)
                action [
                    Jump("corner_store_south")
                ]
        frame:
            pos (0.57, 0.38)
            textbutton "club_stairs":
                xysize (0.04, 0.27)
                action [
                    Jump("club_stairs")
                ]
        frame:
            pos (0.77, 0)
            textbutton "dock":
                xysize (0.23, 1.0)
                action [
                    Jump("dock")
                ]

    # Script
    scene bg street_sentinel_alley
    with fade
    call screen interact_sentinel_alley
