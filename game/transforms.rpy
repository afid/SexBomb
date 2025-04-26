transform place_right:
    pos (0.77, 1.0)
    anchor(0.3, 1.0)
    on appear:
        alpha 0.1
    on show:
        zoom .5
        linear 1.5 zoom 1.25 alpha 1.0
    on hide:
        linear 0.4 zoom 1.25 alpha 0.0

transform place_left:
    pos (0.1, 1.0)
    anchor(0.3, 1.0)
    on appear:
        alpha 0.1
    on show:
        zoom .5
        linear 1.5 zoom 1.25 alpha 1.0
    on hide:
        linear 0.4 zoom 1.25 alpha 0.0

transform dice_transform_2:
    alpha 0.0 pos (0.84, 0.1)
    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

transform achievement_transform:
    on show:
        xalign .98
        yalign -.3
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 1.9 yalign .02