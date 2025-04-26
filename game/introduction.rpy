label intro():
    play music "audio/play.opus"
    # 01 Affiche l'Accueil avec la présentation du jeux
    scene chambre_01 with Dissolve(1.0)

    default persistent.authorize = False

    show hitomi at place_left
    # Pour le dev
    # hide hitomi with Dissolve(0.6)

    # Si le joueur n'a jamais joué, on lui pose la question sur sa majorité sexuel
    if persistent.authorize == False:
        h "Ce jeu est destiné exclusivement à un public adulte (18 ans et plus). En participant à ce jeu, vous reconnaissez et acceptez les conditions suivantes :"
        "{size=23}{cps=25}1. Contenu Mature : Ce jeu peut contenir des thèmes, des images et des situations destinés à un public adulte. Il est déconseillé aux personnes sensibles ou mineures.
        \n2. Responsabilité : Les organisateurs du jeu ne peuvent être tenus responsables des conséquences physiques, émotionnelles ou psychologiques résultant de la participation au jeu. Chaque participant est responsable de ses propres actions et doit jouer de manière responsable.
        \n3. Consentement : En participant, vous acceptez de manière volontaire et éclairée de prendre part aux défis proposés. Vous avez le droit de refuser tout défi qui vous met mal à l'aise ou que vous jugez inapproprié.
        \n4. Confidentialité : Les informations personnelles des participants ne seront pas divulguées à des tiers sans consentement préalable. Veuillez respecter la vie privée des autres joueurs.
        \n5. Sécurité : Assurez-vous que les défis sont réalisés dans un environnement sûr et que les accessoires utilisés ne présentent aucun danger. La sécurité des participants est primordiale.{/cps}{/size}"
        menu:
            h "Pourriez-vous confirmer que vous avez atteint l'âge de la majorité légale ?"
            "Oui":
                $ persistent.authorize = True
                h "Excellent, nous allons pouvoir commencer la partie"
                jump new_player
            "Non":
                jump mineur
    # Si le joueur a déjà joué, on ne lui repose pas la question sur sa majorité sexuel
    else:
        h "De retour ? Alors c'est que vous avez apprécié.\nÊtes vous prêt pour une nouvelle partie ?"
        h "Pour rappel: Ce jeu est destiné exclusivement à un public adulte (18 ans et plus). En participant à ce jeu, vous reconnaissez et acceptez les conditions suivantes :"
        "{size=23}{cps=25}1. Contenu Mature : Ce jeu peut contenir des thèmes, des images et des situations destinés à un public adulte. Il est déconseillé aux personnes sensibles ou mineures.
        \n2. Responsabilité : Les organisateurs du jeu ne peuvent être tenus responsables des conséquences physiques, émotionnelles ou psychologiques résultant de la participation au jeu. Chaque participant est responsable de ses propres actions et doit jouer de manière responsable.
        \n3. Consentement : En participant, vous acceptez de manière volontaire et éclairée de prendre part aux défis proposés. Vous avez le droit de refuser tout défi qui vous met mal à l'aise ou que vous jugez inapproprié.
        \n4. Confidentialité : Les informations personnelles des participants ne seront pas divulguées à des tiers sans consentement préalable. Veuillez respecter la vie privée des autres joueurs.
        \n5. Sécurité : Assurez-vous que les défis sont réalisés dans un environnement sûr et que les accessoires utilisés ne présentent aucun danger. La sécurité des participants est primordiale.{/cps}{/size}"

        menu:
            "Aller on remet ça":
                jump old_player
            "J’arrête ici, je n'en peux plus je suis exténué":
                jump by
        jump exit


label new_player():
    h "Bienvenu, permettez moi de me présenter, je me nomme {b}Hitomi{/b} et je serais vôtre guide tout au long de cette partie."
    h "Découvrez un jeu de gages amusants proposant plus de 1000 défis à relever en duo ou en groupe pour dynamiser votre vie sexuelle."
    h "La participation est requise par au moins deux personnes !"
    h "Afin que je puisse créer un profil personnalisé pour chacun, vous serez invité(e) à répondre à quelques questions, cela ne vous prendra pas plus de deux minutes par joueur."
    h "Amusez-vous bien et profitez pleinement de cette aventure ludique !"
    hide hitomi with Dissolve(0.6)
    pause(0.2)
    jump accessoires

label old_player():
    h "Bienvenu, vous me connaissez déjà mais permettez moi de me présenter a nouveau, je me nomme {b}Hitomi{/b} et je serais vôtre guide tout au long de cette partie."
    h "Je vous rappel que la participation est requise par au moins deux personnes !"
    h "Afin que je puisse créer un nouveau profil personnalisé pour chacun, vous serez invité(e) à répondre à quelques questions."
    h "Amusez-vous bien et profitez pleinement de cette aventure ludique !"
    hide hitomi with Dissolve(0.6)
    pause(0.2)
    jump accessoires

label accessoires():
    show hitomi at place_left
    # Pour le dev
    # hide hitomi with Dissolve(0.6)

    h "Avant de commencer le jeu, je vous invite a sélectionner les accessoires que vous prêts à utiliser pour les gages et pimenter vos défis.\nCette étape est essentielle pour personnaliser les défis selon ce que vous avez sous la main."
    h "Cliquez sur les accessoires de la liste de gauche pour les ajouter a votre liste, cliquez sur les accessoires de la liste de droite pour les retirer"
    h "Une fois vos accessoires sélectionnés, notre système filtrera automatiquement les gages. Les défis nécessitant des accessoires que vous n'avez pas sélectionnés ne vous seront pas proposés.\nCela garantit que chaque gage est réalisable avec les objets que vous avez choisis."
    # 01 Affiche l’écran pour le choix des accessoires
    call screen accessoires


    # Début des Challenges : Après avoir sélectionné vos accessoires, vous êtes prêts à commencer les challenges ! Amusez-vous et relevez les défis en utilisant les accessoires que vous avez choisis.


    # 02 On filtre les gages selon les accessoires choisis
    $ filter_challenges()
    # On interdit les retours
    $ renpy.block_rollback()

    if len(selected_accessoires)>20:
        h "Le grand Jeux! Vous avez sélectionné: [', '.join([i.name for i in selected_accessoires])]"
    elif len(selected_accessoires)>10:
        h "Gourmands! Vous avez sélectionné: [', '.join([i.name for i in selected_accessoires])]"
    elif len(selected_accessoires)>0:
        h "Raisonnables! Vous avez sélectionné: [', '.join([i.name for i in selected_accessoires])]"
    else:
        h "C'est triste, vous n'avez sélectionné aucun accessoire"

    # 03 Affiche l'écran Questionnaire
    scene chambre_02 with Dissolve(1.0)

    show hitomi at place_left
    # Pour le dev
    # hide hitomi with Dissolve(0.6)

    jump questionnaire
    hide hitomi with Dissolve(1.0)
    h "test"
    # 04 Affiche l'écran avec les Gages
    jump gages


label gage_old():
    $ dice = [1,12] # pour les tests de génération de dés
    if len(dice)>0:
        $ view_dices = generate_number_dice(dice[0], dice[1]) # cette fonction affiche les dés aléatoires

    h "ici le text du gage avec le résultat du dé"
    # on supprime les dés

    $ hide_dices(view_dices)

    hide hitomi
    h "Fin de la partie"
