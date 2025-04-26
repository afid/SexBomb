# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


# Déclarez les personnages utilisés dans le jeu.
define h = Character(_("Hitomi"), window_background="gui/textbox_hitomi.png", image="hitomi.png", who_color="#cc0692bb", who_font="Arch_Condensed_Bold", what_outlines=[(3, "#00000055", 0, 0)], what_color="#efefefbf", what_font="Arch_Regular_5", what_size=28)
define t = Character("Manuel", image="guide_f.png", color="#00f0f0bb", kind=bubble)
define narrator = Character(image="guide_f.png", what_italic=True)
define d = Character(who_font="Arch_Condensed_Bold", who_size=10, what_color="#efefefbf", what_font="Arch_Regular_5", what_size=10)



# Le jeu commence ici
label start:
    call intro
