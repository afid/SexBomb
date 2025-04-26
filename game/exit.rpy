label mineur():
    h "{i}Vous êtes trop jeune, soyez patient un jour viendra ou vous aurez {b}18 ans{/b}. {w}\nMais pour me moment je dois metre fin a cette partie, et vous demande de ne pas retenter.{/i}"
    jump exit

label by():
    h "J’espère que vous avez appréciez ce jeu."
    jump exit

label exit():
    hide hitomi
    image splash = Movie(play="images/splashscreen.webm") # webm
    show splash with Dissolve(0.5)
    with Pause(0.5)
    show text "Fin" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(0.5)
    hide splash with Dissolve(0.5)
    return