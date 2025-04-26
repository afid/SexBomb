init offset = -1

define gui.notify_ypos = 10

define gui.notify_text_size = 24

screen notification(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 22.25 action Hide('notify')


transform notify_appear:
    on appear:
        alpha 1.0
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    xalign 0.5
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    font "Arch_Condensed.ttf"
    size 20
    properties gui.text_properties("notify")
