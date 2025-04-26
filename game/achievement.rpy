# $ notification_level("Commençons", "Vous êtes au premier niveau", 1)
# h "Niveau 1"

screen src_achievement(title, text, icon):
    timer 6 action Hide("src_achievement")
    window:
        at achievement_transform
        background "#231F20"
        xalign .99
        yalign .02
        xysize (420, 115)

        hbox:
            spacing 5
            xoffset 5
            yoffset 5

            vbox:
                spacing 5
                xalign 0.5
                yalign 0.5
                image icon
            vbox:
                spacing 5
                xoffset 0
                xsize 270
                xalign 0.5
                yalign 0.5
                text title:
                    size 32
                    id title
                    style "achievement_text"
                text text:
                    size 25
                    id text
                    style "achievement_text"


style achievement_text:
    color "#E7BC66"


init python:
    def notification_level(title, text, level):
        renpy.show_screen(_screen_name='src_achievement', title=title, text=text, icon=f"images/level_{level}.png")
