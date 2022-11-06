transform small:
    zoom 0.5

transform medium:
    zoom 0.75

# SWAT Team
image swat shooting:
    "enemies/swat.png"
    pause renpy.random.randint(2, 5)/10
    "enemies/swat_shooting.png"
    pause 0.1
    repeat

image swat shot_left:
    "enemies/swat_shot.png"
    linear 0.1 zoom 0.8
    "enemies/swat_dead_left.png"

image swat shot_center:
    "enemies/swat_shot.png"
    linear 0.1 zoom 0.8
    "enemies/swat_dead_center.png"

image swat shot_right:
    "enemies/swat_shot.png"
    linear 0.1 zoom 0.8
    "enemies/swat_dead_right.png"

image shot_death:
    "clown/police_shot_death.png"
    align (0.5, 0.5)
    pos (0.55, 1.25)
    zoom 1
    rotate 0
    linear 6.0 zoom 0.6 rotate 45 ypos 0.8

# Ninjas
transform peek_left:
    linear 0.5 xanchor 0.0
    pause 1.0
    linear 0.5 xanchor -1.0

transform peek_right:
    linear 0.5 xanchor 0.0
    pause 1.0
    linear 0.5 xanchor 1.0

image ninja attacking_left_1:
    animation
    "enemies/ninja_attacking_left.png"
    xanchor -1.0
    peek_left
    pause 4.0
    repeat

image ninja attacking_left_2:
    animation
    "enemies/ninja_attacking_left.png"
    xanchor -1.0
    pause 2.0
    peek_left
    pause 2.0
    repeat

image ninja attacking_left_3:
    animation
    "enemies/ninja_attacking_left.png"
    xanchor -1.0
    pause 4.0
    peek_left
    repeat


image ninja attacking_right_1:
    animation
    "enemies/ninja_attacking_right.png"
    xanchor 1.0
    peek_right
    pause 4.0
    repeat

image ninja attacking_right_2:
    animation
    "enemies/ninja_attacking_right.png"
    xanchor 1.0
    pause 2.0
    peek_right
    pause 2.0
    repeat

image ninja attacking_right_3:
    animation
    "enemies/ninja_attacking_right.png"
    xanchor 1.0
    pause 4.0
    peek_right
    repeat

image ninja shot_center_left:
    "enemies/ninja_shot_left.png"
    linear 0.1 zoom 0.8
    "enemies/ninja_dead_center.png"
    xzoom -1
    ypos 0.8

image ninja shot_center_right:
    "enemies/ninja_shot_right.png"
    linear 0.1 zoom 0.8
    "enemies/ninja_dead_center.png"
    ypos 0.8

image ninja shot_left:
    "enemies/ninja_shot_left.png"
    linear 0.1 zoom 0.8
    "enemies/ninja_dead_left.png"
    ypos 1.2

image ninja shot_right:
    "enemies/ninja_shot_right.png"
    linear 0.1 zoom 0.8
    "enemies/ninja_dead_right.png"
    ypos 1.2

image monk:
    "ninja/monk.png"
    align (0.5, 0.5)

image monk shot:
    "ninja/monk_shot.png"
    linear 0.1 zoom 0.8
    "ninja/monk_dead.png"
    pos (-0.1, 1.2)

# Zombies
# Horde Death
label horde:
    # Settings
    $ progress["zombies"]["clear"] = []

    # Script
    scene bg plain_black
    show horde_backrow:
        align (0.5, 0.0)
        pos (0.5, 0.15)
        alpha 0.0
        zoom 0.7
        pause 4
        linear 2.0 alpha 1.0 zoom 0.55
    show horde_midrow:
        align (0.5, 0.0)
        pos (0.5, 0.1)
        alpha 0.0
        zoom 0.85
        pause 2
        linear 2.0 alpha 1.0 zoom 0.70
        linear 2.0 zoom 0.55
    show horde_player:
        align (0.5, 0.0)
        pos (0.5, 0.05)
        alpha 0.0
        zoom 1
        linear 2.0 alpha 1.0 zoom 0.85
        linear 4.0 zoom 0.55
    play audio "audio/bell.wav"
    pause 6.0
    jump game_over

# Generic Zombies
image zombie_a full:
    "enemies/zombie_a_full.png"

image zombie_a half = VBox(
    "zombie_a half_body",
    "zombie_a half_splat",
)

image zombie_a half_body:
    "enemies/zombie_a_half.png"

image zombie_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_a dead = VBox(
    "zombie_a dead_blood",
    "zombie_a dead_leg",
    "zombie_a dead_arm",
    "zombie_a dead_head",
    "zombie_a dead_splat",
    )

image zombie_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_a dead_head:
    "enemies/zombie_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.75, 0.8) rotate 90

image zombie_a dead_arm:
    "enemies/zombie_a_dead_arm.png"
    pos (-0.25, 0.0)
    rotate 0
    linear 0.1 pos (-0.5, 1.1) rotate 90

image zombie_a dead_leg:
    "enemies/zombie_a_dead_leg.png"
    pos (0.2, 2.0)
    rotate 0
    linear 0.1 rotate 90 pos (0.3, 2.25)

image zombie_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_b full:
    "enemies/zombie_b_full.png"

image zombie_b half = VBox(
    "zombie_b half_body",
    "zombie_b half_splat",
)

image zombie_b half_body:
    "enemies/zombie_b_half.png"
    pos (0.03, 0.0)

image zombie_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_b dead = VBox(
    "zombie_b dead_blood",
    "zombie_b dead_leg",
    "zombie_b dead_arm",
    "zombie_b dead_head",
    "zombie_b dead_splat",
    )

image zombie_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_b dead_head:
    "enemies/zombie_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_b dead_arm:
    "enemies/zombie_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_b dead_leg:
    "enemies/zombie_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 2.0)

image zombie_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_c full:
    "enemies/zombie_c_full.png"

image zombie_c half = VBox(
    "zombie_c half_body",
    "zombie_c half_splat",
)

image zombie_c half_body:
    "enemies/zombie_c_half.png"
    pos (-0.01, 0.0)

image zombie_c half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.1, -2.4)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_c dead = VBox(
    "zombie_c dead_blood",
    "zombie_c dead_leg",
    "zombie_c dead_arm",
    "zombie_c dead_head",
    "zombie_c dead_splat",
    )

image zombie_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.5)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_c dead_head:
    "enemies/zombie_c_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_c dead_arm:
    "enemies/zombie_c_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_c dead_leg:
    "enemies/zombie_c_dead_leg.png"
    pos (-0.1, 1.8)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.1)

image zombie_c dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 10.0)

# Police Zombies
image zombie_police_a full:
    "enemies/zombie_police_a_full.png"

image zombie_police_a half = VBox(
    "zombie_police_a half_body",
    "zombie_police_a half_splat",
)

image zombie_police_a half_body:
    "enemies/zombie_police_a_half.png"

image zombie_police_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_a dead = VBox(
    "zombie_police_a dead_blood",
    "zombie_police_a dead_leg",
    "zombie_police_a dead_arm",
    "zombie_police_a dead_head",
    "zombie_police_a dead_splat",
    )

image zombie_police_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_a dead_head:
    "enemies/zombie_police_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.75, 0.8) rotate 90

image zombie_police_a dead_arm:
    "enemies/zombie_police_a_dead_arm.png"
    pos (-0.25, 0.0)
    rotate 0
    linear 0.1 pos (-0.5, 1.1) rotate 90

image zombie_police_a dead_leg:
    "enemies/zombie_police_a_dead_leg.png"
    pos (0.2, 2.0)
    rotate 0
    linear 0.1 rotate 90 pos (0.3, 2.25)

image zombie_police_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_police_b full:
    "enemies/zombie_police_b_full.png"

image zombie_police_b half = VBox(
    "zombie_police_b half_body",
    "zombie_police_b half_splat",
)

image zombie_police_b half_body:
    "enemies/zombie_police_b_half.png"
    pos (0.03, 0.0)

image zombie_police_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_b dead = VBox(
    "zombie_police_b dead_blood",
    "zombie_police_b dead_leg",
    "zombie_police_b dead_arm",
    "zombie_police_b dead_head",
    "zombie_police_b dead_splat",
    )

image zombie_police_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_b dead_head:
    "enemies/zombie_police_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_police_b dead_arm:
    "enemies/zombie_police_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_police_b dead_leg:
    "enemies/zombie_police_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 2.0)

image zombie_police_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_police_c full:
    "enemies/zombie_police_c_full.png"

image zombie_police_c half = VBox(
    "zombie_police_c half_body",
    "zombie_police_c half_splat",
)

image zombie_police_c half_body:
    "enemies/zombie_police_c_half.png"
    pos (-0.01, 0.0)

image zombie_police_c half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.1, -2.4)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_c dead = VBox(
    "zombie_police_c dead_blood",
    "zombie_police_c dead_leg",
    "zombie_police_c dead_arm",
    "zombie_police_c dead_head",
    "zombie_police_c dead_splat",
    )

image zombie_police_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.5)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_police_c dead_head:
    "enemies/zombie_police_c_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_police_c dead_arm:
    "enemies/zombie_police_c_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_police_c dead_leg:
    "enemies/zombie_police_c_dead_leg.png"
    pos (-0.1, 1.8)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.1)

image zombie_police_c dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 10.0)

# Clown Zombies
image zombie_clown_a full:
    "enemies/zombie_clown_a_full.png"

image zombie_clown_a half = VBox(
    "zombie_clown_a half_body",
    "zombie_clown_a half_splat",
)

image zombie_clown_a half_body:
    "enemies/zombie_clown_a_half.png"
    pos (0.05, 0.0)

image zombie_clown_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_a dead = VBox(
    "zombie_clown_a dead_blood",
    "zombie_clown_a dead_shoe",
    "zombie_clown_a dead_leg",
    "zombie_clown_a dead_arm",
    "zombie_clown_a dead_head",
    "zombie_clown_a dead_splat",
    )

image zombie_clown_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_a dead_head:
    "enemies/zombie_clown_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.75, 0.8) rotate 90

image zombie_clown_a dead_arm:
    "enemies/zombie_clown_a_dead_arm.png"
    pos (-0.25, 0.0)
    rotate 0
    linear 0.1 pos (-0.5, 1.1) rotate 90

image zombie_clown_a dead_leg:
    "enemies/zombie_clown_a_dead_leg.png"
    pos (0.2, 2.0)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.25)

image zombie_clown_a dead_shoe:
    "enemies/zombie_clown_a_dead_shoe.png"
    pos (0.3, 15.0)

image zombie_clown_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_clown_b full:
    "enemies/zombie_clown_b_full.png"

image zombie_clown_b half = VBox(
    "zombie_clown_b half_body",
    "zombie_clown_b half_splat",
)

image zombie_clown_b half_body:
    "enemies/zombie_clown_b_half.png"
    pos (0.0, 0.0)

image zombie_clown_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_b dead = VBox(
    "zombie_clown_b dead_blood",
    "zombie_clown_b dead_leg",
    "zombie_clown_b dead_arm",
    "zombie_clown_b dead_head",
    "zombie_clown_b dead_splat",
    )

image zombie_clown_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_b dead_head:
    "enemies/zombie_clown_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_clown_b dead_arm:
    "enemies/zombie_clown_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_clown_b dead_leg:
    "enemies/zombie_clown_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 2.0)

image zombie_clown_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_clown_c full:
    "enemies/zombie_clown_c_full.png"

image zombie_clown_c half = VBox(
    "zombie_clown_c half_body",
    "zombie_clown_c half_splat",
)

image zombie_clown_c half_body:
    "enemies/zombie_clown_c_half.png"
    pos (0.0, 0.0)

image zombie_clown_c half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.1, -2.4)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_c dead = VBox(
    "zombie_clown_c dead_blood",
    "zombie_clown_c dead_leg",
    "zombie_clown_c dead_arm",
    "zombie_clown_c dead_head",
    "zombie_clown_c dead_tie",
    "zombie_clown_c dead_splat",
    )

image zombie_clown_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.5)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_clown_c dead_tie:
    "enemies/zombie_clown_c_dead_tie.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.25, 0.6) rotate -360

image zombie_clown_c dead_head:
    "enemies/zombie_clown_c_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_clown_c dead_arm:
    "enemies/zombie_clown_c_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_clown_c dead_leg:
    "enemies/zombie_clown_c_dead_leg.png"
    pos (-0.1, 1.8)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.1)

image zombie_clown_c dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 10.0)

# Ninja Zombies
image zombie_ninja_a full:
    "enemies/zombie_ninja_a_full.png"

image zombie_ninja_a half = VBox(
    "zombie_ninja_a half_body",
    "zombie_ninja_a half_splat",
)

image zombie_ninja_a half_body:
    "enemies/zombie_ninja_a_half.png"
    pos (0.01, 0.0)

image zombie_ninja_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_a dead = VBox(
    "zombie_ninja_a dead_blood",
    "zombie_ninja_a dead_shoe",
    "zombie_ninja_a dead_leg",
    "zombie_ninja_a dead_arm",
    "zombie_ninja_a dead_head",
    "zombie_ninja_a dead_splat",
    )

image zombie_ninja_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_a dead_head:
    "enemies/zombie_ninja_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.75, 0.8) rotate 90

image zombie_ninja_a dead_arm:
    "enemies/zombie_ninja_a_dead_arm.png"
    pos (-0.25, 0.0)
    rotate 0
    linear 0.1 pos (-0.5, 1.1) rotate 90

image zombie_ninja_a dead_leg:
    "enemies/zombie_ninja_a_dead_leg.png"
    pos (0.4, 2.0)
    rotate 0
    linear 0.1 rotate 90 pos (0.6, 2.25)

image zombie_ninja_a dead_shoe:
    "enemies/zombie_ninja_a_dead_shoe.png"
    pos (0.1, 9.0)

image zombie_ninja_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_ninja_b full:
    "enemies/zombie_ninja_b_full.png"

image zombie_ninja_b half = VBox(
    "zombie_ninja_b half_body",
    "zombie_ninja_b half_splat",
)

image zombie_ninja_b half_body:
    "enemies/zombie_ninja_b_half.png"
    pos (0.04, 0.0)

image zombie_ninja_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_b dead = VBox(
    "zombie_ninja_b dead_blood",
    "zombie_ninja_b dead_shoe",
    "zombie_ninja_b dead_leg",
    "zombie_ninja_b dead_arm",
    "zombie_ninja_b dead_head",
    "zombie_ninja_b dead_splat",
    )

image zombie_ninja_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_b dead_head:
    "enemies/zombie_ninja_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_ninja_b dead_arm:
    "enemies/zombie_ninja_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_ninja_b dead_leg:
    "enemies/zombie_ninja_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 2.0)

image zombie_ninja_b dead_shoe:
    "enemies/zombie_ninja_b_dead_shoe.png"
    pos (0.3, 13.0)

image zombie_ninja_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_ninja_c full:
    "enemies/zombie_ninja_c_full.png"

image zombie_ninja_c half = VBox(
    "zombie_ninja_c half_body",
    "zombie_ninja_c half_splat",
)

image zombie_ninja_c half_body:
    "enemies/zombie_ninja_c_half.png"
    pos (0.05, 0.0)

image zombie_ninja_c half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.1, -2.4)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_c dead = VBox(
    "zombie_ninja_c dead_blood",
    "zombie_ninja_c dead_leg",
    "zombie_ninja_c dead_arm",
    "zombie_ninja_c dead_head",
    "zombie_ninja_c dead_hat",
    "zombie_ninja_c dead_splat",
    )

image zombie_ninja_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.5)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_ninja_c dead_hat:
    "enemies/zombie_ninja_c_dead_hat.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (-0.25, -0.5) rotate -560

image zombie_ninja_c dead_head:
    "enemies/zombie_ninja_c_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_ninja_c dead_arm:
    "enemies/zombie_ninja_c_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_ninja_c dead_leg:
    "enemies/zombie_ninja_c_dead_leg.png"
    pos (-0.1, 1.8)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.1)

image zombie_ninja_c dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 10.0)

# Pirate Zombies
image zombie_pirate_a full:
    "enemies/zombie_pirate_a_full.png"

image zombie_pirate_a half = VBox(
    "zombie_pirate_a half_body",
    "zombie_pirate_a half_splat",
)

image zombie_pirate_a half_body:
    "enemies/zombie_pirate_a_half.png"
    pos (0.03, 0.0)

image zombie_pirate_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_a dead = VBox(
    "zombie_pirate_a dead_blood",
    "zombie_pirate_a dead_sword",
    "zombie_pirate_a dead_leg",
    "zombie_pirate_a dead_arm",
    "zombie_pirate_a dead_head",
    "zombie_pirate_a dead_splat",
    )

image zombie_pirate_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_a dead_head:
    "enemies/zombie_pirate_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.9, 0.0) rotate 90

image zombie_pirate_a dead_arm:
    "enemies/zombie_pirate_a_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.75, 1.2) rotate -90

image zombie_pirate_a dead_leg:
    "enemies/zombie_pirate_a_dead_leg.png"
    pos (0.3, 1.0)
    rotate 0
    linear 0.1 rotate 90 pos (0.5, 1.2)

image zombie_pirate_a dead_sword:
    "enemies/zombie_pirate_a_dead_sword.png"
    pos (0.5, 0.5)
    rotate 0
    linear 0.1 pos (-0.25, 1.7) rotate 90

image zombie_pirate_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_pirate_b full:
    "enemies/zombie_pirate_b_full.png"

image zombie_pirate_b half = VBox(
    "zombie_pirate_b half_body",
    "zombie_pirate_b half_splat",
)

image zombie_pirate_b half_body:
    "enemies/zombie_pirate_b_half.png"
    pos (0.03, 0.0)

image zombie_pirate_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_b dead = VBox(
    "zombie_pirate_b dead_blood",
    "zombie_pirate_b dead_leg",
    "zombie_pirate_b dead_arm",
    "zombie_pirate_b dead_head",
    "zombie_pirate_b dead_hat",
    "zombie_pirate_b dead_splat",
    )

image zombie_pirate_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_b dead_hat:
    "enemies/zombie_pirate_b_dead_hat.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (-0.25, -0.5) rotate -560

image zombie_pirate_b dead_head:
    "enemies/zombie_pirate_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_pirate_b dead_arm:
    "enemies/zombie_pirate_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.5) rotate -90

image zombie_pirate_b dead_leg:
    "enemies/zombie_pirate_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 2.0)

image zombie_pirate_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_pirate_c full:
    "enemies/zombie_pirate_c_full.png"

image zombie_pirate_c half = VBox(
    "zombie_pirate_c half_body",
    "zombie_pirate_c half_splat",
)

image zombie_pirate_c half_body:
    "enemies/zombie_pirate_c_half.png"
    pos (0.0, 0.0)

image zombie_pirate_c half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.1, -2.4)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_c dead = VBox(
    "zombie_pirate_c dead_blood",
    "zombie_pirate_c dead_shoe",
    "zombie_pirate_c dead_leg",
    "zombie_pirate_c dead_arm",
    "zombie_pirate_c dead_head",
    "zombie_pirate_c dead_splat",
    )

image zombie_pirate_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.5)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_pirate_c dead_head:
    "enemies/zombie_pirate_c_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.85, 0.8) rotate 90

image zombie_pirate_c dead_arm:
    "enemies/zombie_pirate_c_dead_arm.png"
    pos (-0.25, 0.0)
    rotate 0
    linear 0.1 pos (-0.5, 1.5) rotate 90

image zombie_pirate_c dead_leg:
    "enemies/zombie_pirate_c_dead_leg.png"
    pos (0.1, 1.8)
    rotate 0
    linear 0.1 rotate 90 pos (0.3, 2.5)

image zombie_pirate_c dead_shoe:
    "enemies/zombie_pirate_c_dead_shoe.png"
    pos (0.0, 10.5)

image zombie_pirate_c dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 10.0)

# Tap Zombies
image zombie_tap_a full:
    "enemies/zombie_tap_a_full.png"

image zombie_tap_a half = VBox(
    "zombie_tap_a half_body",
    "zombie_tap_a half_splat",
)

image zombie_tap_a half_body:
    "enemies/zombie_tap_a_half.png"
    pos (0.04, 0.0)

image zombie_tap_a half_splat:
    "enemies/zombie_blood_small.png"
    pos (0.0, -2.0)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_tap_a dead = VBox(
    "zombie_tap_a dead_blood",
    "zombie_tap_a dead_leg",
    "zombie_tap_a dead_arm",
    "zombie_tap_a dead_head",
    "zombie_tap_a dead_splat",
    )

image zombie_tap_a dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.3)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_tap_a dead_head:
    "enemies/zombie_tap_a_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.9, 0.0) rotate 90

image zombie_tap_a dead_arm:
    "enemies/zombie_tap_a_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.0) rotate -90

image zombie_tap_a dead_leg:
    "enemies/zombie_tap_a_dead_leg.png"
    pos (-0.1, 2.0)
    rotate 0
    linear 0.1 rotate -90 pos (-0.3, 2.25)

image zombie_tap_a dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.25, 8.0)

image zombie_tap_b full:
    "enemies/zombie_tap_b_full.png"

image zombie_tap_b half = VBox(
    "zombie_tap_b half_body",
    "zombie_tap_b half_splat",
)

image zombie_tap_b half_body:
    "enemies/zombie_tap_b_half.png"
    pos (0.03, 0.0)

image zombie_tap_b half_splat:
    "enemies/zombie_blood_small.png"
    pos (-0.2, -1.8)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_tap_b dead = VBox(
    "zombie_tap_b dead_blood",
    "zombie_tap_b dead_shoe",
    "zombie_tap_b dead_leg",
    "zombie_tap_b dead_arm",
    "zombie_tap_b dead_head",
    "zombie_tap_b dead_splat",
    )

image zombie_tap_b dead_splat:
    "enemies/zombie_blood_large.png"
    pos (-0.2, -1.2)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_tap_b dead_head:
    "enemies/zombie_tap_b_dead_head.png"
    pos (0.0, -4.0)
    rotate 0
    linear 0.25 pos (0.75, 0.7) rotate 90

image zombie_tap_b dead_arm:
    "enemies/zombie_tap_b_dead_arm.png"
    pos (0.25, 0.0)
    rotate 0
    linear 0.1 pos (0.5, 1.0) rotate -90

image zombie_tap_b dead_leg:
    "enemies/zombie_tap_b_dead_leg.png"
    pos (0.0, 1.5)
    rotate 0
    linear 0.1 rotate -90 pos (-0.2, 1.7)

image zombie_tap_b dead_shoe:
    "enemies/zombie_tap_b_dead_shoe.png"
    pos (0.2, 8.0)

image zombie_tap_b dead_blood:
    "enemies/zombie_dead_blood.png"
    pos (-0.3, 6.0)

image zombie_tap_c full:
    "enemies/zombie_tap_c_full.png"

image zombie_tap_c dead = VBox(
    "zombie_tap_c dead_body",
    "zombie_tap_c dead_arm",
    "zombie_tap_c dead_splat",
    )

image zombie_tap_c dead_splat:
    "enemies/zombie_blood_large.png"
    pos (0.0, -6.75)
    alpha 1.0
    linear 0.25 alpha 0.0

image zombie_tap_c dead_body:
    "enemies/zombie_tap_c_dead_body.png"
    pos (-0.514, -0.01475)
    rotate 0
    pause 2.0
    easeout 1.5 pos (-0.45, -0.13) rotate 90

image zombie_tap_c dead_arm:
    "enemies/zombie_tap_c_dead_arm.png"
    pos (-0.332, -1.038)
    rotate 0
    pause 0.5
    easeout 1.0 pos (-0.36, -1.12) rotate 90