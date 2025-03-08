# Thrown Grenade
image smoke_thrown:
    "ninja/smoke.png"
    pos (1.0, 1.0)
    rotate 0
    zoom 2.0
    easein 1.0 pos (0.5, 0.7) clockwise rotate -270 zoom 0.25

image smoke_bang:
    "ninja/smoke_bang.png"
    pos (0.5, 1.0)
    alpha 0.0
    ease 0.1 alpha 1.0
    ease 0.1 alpha 0.0

# Smoke Base
image smoke_plume:
    "ninja/smoke_plume.png"
    zoom 0.8
    align (0.5, 0.25)
    ease 1.0 alpha 0.0 yalign 0.2
image smoke_cloud:
    "ninja/smoke_cloud.png"
    zoom 0.8
    align (0.5, 0.8)
    ease 1.0 alpha 0.0 yalign 0.75

# Smoke Veil
transform expand_a:
    align (0.45, 0.0)
    xzoom 0.1
    ease 0.5 xzoom 1.0

transform expand_b:
    align (0.55, 0.0)
    xzoom 0.1
    ease 0.5 xzoom 1.0

transform fog_a:
    align (0.45, 0.0)
    ease 1.5 xalign 0.55
    ease 1.5 xalign 0.45
    repeat 3

transform fog_b:
    align (0.55, 0.0)
    ease 1.5 xalign 0.45
    ease 1.5 xalign 0.55
    repeat 3

transform dissipate:
    ease 1.0 alpha 0.0 yalign -0.1

image smoke_veil_1:
    "ninja/smoke_veil_1.png"
    expand_a
    fog_a
    dissipate

image smoke_veil_2:
    "ninja/smoke_veil_2.png"
    expand_b
    fog_b
    dissipate

image smoke_veil_3:
    "ninja/smoke_veil_3.png"
    expand_a
    fog_a
    dissipate

image smoke_veil_4:
    "ninja/smoke_veil_4.png"
    expand_b
    fog_b
    dissipate

image smoke_veil_5:
    "ninja/smoke_veil_5.png"
    fog_a
    dissipate

image smoke_veil_6:
    "ninja/smoke_veil_1.png"
    fog_a
    dissipate

image smoke_veil_7:
    "ninja/smoke_veil_2.png"
    fog_b
    dissipate

image smoke_veil_8:
    "ninja/smoke_veil_3.png"
    fog_a
    dissipate

image smoke_veil_9:
    "ninja/smoke_veil_4.png"
    fog_b
    dissipate

image smoke_veil_10:
    "ninja/smoke_veil_5.png"
    fog_a
    dissipate