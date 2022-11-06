label downtown_bus:
    screen interact_downtown_bus():
        frame:
            pos (0, 0.8)
            textbutton "downtown":
                xysize (1.0, 0.2)
                action [
                    Jump("downtown")
                ]
        frame:
            pos (0.29, 0.15)
            textbutton "bus_ride":
                xysize (0.2, 0.8)
                action [
                    Call("bus_ride", "junction")
                ]

    scene bg street_downtown_bus with fade
    if progress["bus_ticket"] == False:
        rob "Been clean for 5 years now. Last trip was way too crazy."
        rob "But I owe you one. Hop aboard and I'll take you across town if you want."
        $ progress["bus_ticket"] = True
    call screen interact_downtown_bus

label junction_bus:
    screen interact_junction_bus():
        frame:
            pos (0, 0.8)
            textbutton "junction":
                xysize (1.0, 0.2)
                action [
                    Jump("junction")
                ]
        frame:
            pos (0.505, 0.15)
            textbutton "bus_ride":
                xysize (0.2, 0.8)
                action [
                    Call("bus_ride", "downtown")
                ]

    scene bg street_junction_bus with fade
    if progress["bus_ticket"] == False:
        rob "Been clean for 5 years now. Last trip was way too crazy."
        rob "But I owe you one. Hop aboard and I'll take you across town if you want."
        $ progress["bus_ticket"] = True
    call screen interact_junction_bus

label bus_ride(destination):
    image bus_road downtown:
        "street/bus_road.png"
        align (0.0, 0.0)
        pause 0.25
        ease 3.0 xalign 1.0
    image bus_road junction:
        "street/bus_road.png"
        align (1.0, 0.0)
        pause 0.25
        ease 3.0 xalign 0.0
    image bus_window:
        "street/bus_window.png"
        align(0.5, 0.5)
        pos (0.5, 0.475)

    if progress["evening"] or (inventory["beer"]["active"] and inventory["cash"]["active"] and inventory["noodles"]["active"]):
        scene bg street_bus_ride_eve
    else:
        scene bg street_bus_ride
    show expression "bus_road " + destination
    show bus_window
    play audio "audio/bus.wav"
    with fade
    pause 3.0
    jump expression destination