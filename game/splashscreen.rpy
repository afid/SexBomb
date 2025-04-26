# Scene d'introduction avant le chargement du menu du jeu
label splashscreen:
    image splash = Movie(play="images/splashscreen.webm") # webm
    show splash with Dissolve(0.5)
    with Pause(0.5)
    show text _("Enfin un vrai jeu pour adultes") with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(0.5)
    show text _("Découvrez un jeu de gages amusants proposant plus de 1000 défis à relever en duo ou en groupe pour dynamiser votre vie sexuelle.") with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(0.5)
    show text _("La participation est requise par au moins deux personnes !") with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(0.5)
    show text _("Amusez-vous bien et profitez pleinement de cette aventure ludique !") with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(0.5)

    hide splash with Dissolve(0.5)
    return