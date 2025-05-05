# Liste d'accessoires que les joueurs auront sélectionnés
default selected_accessoires = []


init python:
    """
    Classe représentant un accessoire.

    Attributes:
        name (str): Le nom de l'accessoire.
        image (str): Le chemin de l'image de l'accessoire.
        image_hover (str): Le chemin de l'image de l'accessoire lorsqu'il est survolé.
    """

    class Accessoire:
        def __init__(self, name, image, image_hover):
            """
            Initialise un nouvel objet Accessoire.

            Args:
                name (str): Le nom de l'accessoire.
                image (str): Le chemin de l'image de l'accessoire.
                image_hover (str): Le chemin de l'image de l'accessoire lorsqu'il est survolé.
            """
            self.name: string = name
            self.image: string = image
            self.image_hover: string = image_hover

    # Ces variables sont placées dans le store et seront accessibles partout.
    available_accessoires = [
        Accessoire("Appareil photo", "accessoires/appareil-photo.png", "accessoires/appareil-photo_hover.png"),
        Accessoire("Bâillon", "accessoires/baillon.png", "accessoires/baillon_hover.png"),
        Accessoire("Bougie", "accessoires/bougie.png", "accessoires/bougie_hover.png"),
        Accessoire("Champagne", "accessoires/champagne.png", "accessoires/champagne_hover.png"),
        Accessoire("Chantilly", "accessoires/chantilly.png", "accessoires/chantilly_hover.png"),
        Accessoire("Cravache", "accessoires/cravache.png", "accessoires/cravache_hover.png"),
        Accessoire("Double gode", "accessoires/double-gode.png", "accessoires/double-gode_hover.png"),
        Accessoire("Fouet", "accessoires/fouet.png", "accessoires/fouet_hover.png"),
        Accessoire("Fraise", "accessoires/fraise.png", "accessoires/fraise_hover.png"),
        Accessoire("Gants en latex", "accessoires/gants-en-latex.png", "accessoires/gants-en-latex_hover.png"),
        Accessoire("Glaçons", "accessoires/glacons.png", "accessoires/glacons_hover.png"),
        Accessoire("Gode", "accessoires/gode.png", "accessoires/gode_hover.png"),
        Accessoire("Gode anal", "accessoires/gode-anal.png", "accessoires/gode-anal_hover.png"),
        Accessoire("Gode ceinture", "accessoires/gode-ceinture.png", "accessoires/gode-ceinture_hover.png"),
        Accessoire("Huile de massage", "accessoires/huile-de-massage.png", "accessoires/huile-de-massage_hover.png"),
        Accessoire("Laisse", "accessoires/laisse.png", "accessoires/laisse_hover.png"),
        Accessoire("Lubrifiant", "accessoires/lubrifiant.png", "accessoires/lubrifiant_hover.png"),
        Accessoire("Masque ou Bandeau", "accessoires/masque-bandeau.png", "accessoires/masque-bandeau_hover.png"),
        Accessoire("Menottes", "accessoires/menottes.png", "accessoires/menottes_hover.png"),
        Accessoire("Musique", "accessoires/musique.png", "accessoires/musique_hover.png"),
        Accessoire("Pinces à seins", "accessoires/pinces-a-seins.png", "accessoires/pinces-a-seins_hover.png"),
        Accessoire("Plug anal", "accessoires/plug-anal.png", "accessoires/plug-anal_hover.png"),
        Accessoire("Plume", "accessoires/plume.png", "accessoires/plume_hover.png"),
        Accessoire("Smartphone", "accessoires/smartphone.png", "accessoires/smartphone_hover.png"),
        Accessoire("Vibromasseur", "accessoires/vibromasseur.png", "accessoires/vibromasseur_hover.png"),
        Accessoire("Vin", "accessoires/vin.png", "accessoires/vin_hover.png")
    ]

    def create_imagebutton(idle_image, hover_image, name, action):
        """
        Crée et retourne un imagebutton Ren'Py.

        Args:
            idle_image (str): Chemin de l'image à afficher lorsque le bouton est au repos.
            hover_image (str): Chemin de l'image à afficher lorsque le bouton est survolé.
            action (list): Liste des actions à exécuter lorsque le bouton est cliqué.

        Returns:
            renpy.ui.imagebutton: Un objet imagebutton Ren'Py.
        """

        return renpy.ui.imagebutton(
            style="acc_button",
            idle=idle_image,
            hover=hover_image,
            unhovered=Play("sound", "audio/close.wav"),
            action=action,
        )


    def add_to_selected_accessoires(accessoire):
        """
        Ajoute un accessoire au panier et le retire de la liste des accessoire disponibles.

        Args:
            accessoire (Accessoire): L'accessoire à ajouter au panier.

        Raises:
            ValueError: Si l'accessoire n'est pas dans la liste des accessoire disponibles.
        """
        if accessoire in available_accessoires:
            selected_accessoires.append(accessoire)
            available_accessoires.remove(accessoire)
            # Redessine l'écran pour refléter les changements.
            renpy.restart_interaction()
        else:
            raise ValueError("L'accessoire n'est pas disponible.")

    def remove_from_selected_accessoires(accessoire):
        """
        Retire un accessoire du panier et le remet dans la liste des accessoire disponibles.

        Args:
            accessoire (Accessoire): L'accessoire à retirer du panier.

        Raises:
            ValueError: Si l'accessoire n'est pas dans le panier.
        """
        if accessoire in selected_accessoires:
            available_accessoires.append(accessoire)
            selected_accessoires.remove(accessoire)
            renpy.restart_interaction()
        else:
            raise ValueError(_("L'accessoire n'est pas dans le panier."))

screen accessoires():
    # $ renpy.block_rollback()
    add "Chambres/chambre_07.jpg"
    modal True
    text _("Choisissez vos accessoires"):
        style "acc_label_text_left"
    text _("Vos choix d'accessoires"):
        style "acc_label_text_right"
    viewport:
        xpos 20
        ypos 40
        xsize 850
        ysize 900
        draggable True
        mousewheel True
        scrollbars "vertical"

        ## La grille des emplacements des accessoires disponible.
        grid 5 6:
            style_prefix "slot"
            xalign 0.5
            yalign 0.5
            spacing 1
            $ qte_image_empty = 30 - len(available_accessoires)
            $ add = __("Ajout de: ")
            $ succes = __(" avec succès")
            for accessoire in available_accessoires: # 26 accessoires
                $ button = create_imagebutton(accessoire.image, accessoire.image_hover, accessoire.name, [Function(renpy.notify, add + accessoire.name + succes), Function(add_to_selected_accessoires, accessoire)])
            for i in range(qte_image_empty):
                $ button = create_imagebutton("accessoires/empty.png", "accessoires/empty.png", "", "")
    viewport:
        xpos 1030
        ypos 40
        xsize 850
        ysize 900
        draggable True
        mousewheel True
        scrollbars "vertical"

        ## La grille des emplacements des accessoires choisis.
        grid 5 6:
            style_prefix "slot"
            xalign 0.5
            yalign 0.5
            spacing 1
            $ qte_image_empty = 30 - len(selected_accessoires)
            $ remove = __("Suppression de: ")
            $ succes = __(" avec succès")
            for accessoire in selected_accessoires :
                $ button = create_imagebutton(accessoire.image, accessoire.image_hover, accessoire.name, [Function(renpy.notify, remove + accessoire.name + succes), Function(remove_from_selected_accessoires, accessoire)])
            for i in range(qte_image_empty):
                $ button = create_imagebutton("accessoires/empty.png", "accessoires/empty.png", "", "")
    # Bouton de validation centré en bas
    hbox:
        xalign 0.5
        yalign 0.96
        frame:
            style "frame_valider"
            textbutton _("Valider") style_prefix "my" action [Hide("accessoires"), Hide('notify'), Return(selected_accessoires)] xalign 0.5 yalign 0.5

style my_button_text is text:
    size 54
    outlines [ (1, "#cc0066", 1, 1) ]
    color "#efefef"
    hover_color "#FFFFFF"

style frame_valider:
    background "valider.png"
    xsize 253
    ysize 65

style button_valider:
    xsize 200
    ysize 50
    color "#efefef"
    font 80

style acc_button:
    xsize 160
    ysize 180
    xmargin 10
    ymargin 15
    hover_sound "audio/hover.wav"
    activate_sound "audio/click.wav"

style acc_label_text_left:
    xpos 240
    ypos 15
    color "#efefef"
    background "#006"

style acc_label_text_right:
    xpos 1250
    ypos 15
    color "#efefef"
    background "#006"