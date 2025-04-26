init python:
    import random
    import pprint

    player_challenges = {}
    filtered_challenges_by_user = {}
    filtered_challenges_by_pratique = {}
    filtered_challenges_by_accessoires={}
    assigned_challenges = {}
    current_player_index = 0
    current_gage = 0
    current_level_primary = 1
    current_level_secondary = 1
    participants = []
    partenaires_restant = []
    partenaires_compatibles=[]
    available_accessoire_names=[]


    # Mapping des compatibilités d’orientation
    COMPATIBILITY_MAP = {
        "h_hetero": ["f_hetero", "f_bi"],
        "gay": ["gay", "h_bi"],
        "h_bi": ["f_hetero", "gay", "h_bi", "f_bi"],
        "f_hetero": ["h_hetero", "h_bi"],
        "lesbienne": ["lesbienne", "f_bi"],
        "f_bi": ["h_hetero", "lesbienne", "h_bi", "f_bi"]
    }

    # Règles complémentaires pour les pratiques
    COMPLEMENTARY_PRACTICES = {
        "domination_soft": "soumission_soft",
        "domination_hard": "soumission_hard",
        "anus_penetration_actif": "anus_penetration_passif",
        "sexe_oral_actif": "sexe_oral_passif",
        "anus_oral_actif": "anus_oral_passif",
        "anus_caresse_actif": "anus_caresse_passif",
    }

    class Player:
        def __init__(self, id, name, gender, orientation, sexe_oral_actif, sexe_oral_passif, anus_oral_actif, anus_oral_passif, sexe_penetration_actif, anus_caresse_actif, anus_penetration_actif, anus_caresse_passif, anus_penetration_passif, fun, soumission_soft, soumission_hard, domination_soft, domination_hard, sperme_soft, sperme_hard, sperme_perso_soft, sperme_perso_hard, partner_orientation):
            self.id = id
            self.name = name
            self.gender = gender
            self.orientation = orientation
            self.sexe_oral_actif = sexe_oral_actif
            self.sexe_oral_passif = sexe_oral_passif
            self.anus_oral_actif = anus_oral_actif
            self.anus_oral_passif = anus_oral_passif
            self.sexe_penetration_actif = sexe_penetration_actif
            self.anus_caresse_actif = anus_caresse_actif
            self.anus_penetration_actif = anus_penetration_actif
            self.anus_caresse_passif = anus_caresse_passif
            self.anus_penetration_passif = anus_penetration_passif
            self.fun = fun
            self.soumission_soft = soumission_soft
            self.soumission_hard = soumission_hard
            self.domination_soft = domination_soft
            self.domination_hard = domination_hard
            self.sperme_soft = sperme_soft
            self.sperme_hard = sperme_hard
            self.sperme_perso_soft = sperme_perso_soft
            self.sperme_perso_hard = sperme_perso_hard
            self.partner_orientation = partner_orientation

    class Partner:
        def __init__(self, player_orientation):
            self.player_orientation = player_orientation

        def get_partner_orientation(self):
            return str(COMPATIBILITY_MAP.get(self.player_orientation, []))


    # Fonction pour filtrer les challenges en fonction des accessoires disponibles
    def filter_challenges():
        available_accessoire_names = {accessoire.name for accessoire in available_accessoires} # Utilisation d'un ensemble pour les noms d'accessoires disponibles
        filtered_challenges_by_accessoires = []

        # print(f'Nombre de challenges au départ: {len(all_challenges)}')
        for challenge in all_challenges:
            if not any(accessory in available_accessoire_names for accessory in challenge["accessoires"]):
                filtered_challenges_by_accessoires.append(challenge)
        # print(f'Nombre de challenges restant après le choix des accessoires: {len(filtered_challenges_by_accessoires)}')
        return filtered_challenges_by_accessoires

    # Fonction pour mélanger tous les gages
    def randomize_all_challenges(all_challenges):
        return random.shuffle(all_challenges)

    # Fonction pour trier tous les gages par niveau et sous niveau
    def sort_all_challenges_by_levels(level_primary, level_secondary):
        return all_challenges.sort(key=lambda x: (x[level_primary], x[level_secondary]))

    # Fonction pour assigner les gages a chaque joueur selon leur genre
    def assign_challenges_to_players_by_gender(name, gender):
        # Création de la liste de challenges pour name si elle n'existe pas
        if name not in player_challenges:
            player_challenges[name] = []
        for challenge in all_challenges:
            if (gender in challenge["player_gender"]):
                player_challenges[name].append(challenge)
        # print(f'Nombre de challenges restant pour {name} après choix gender: {gender}, {len(player_challenges[name])}')
        return player_challenges

    # Fonction pour filtrer les gages de chaque joueur selon son orientation
    def filter_challenges_by_orientation(name, orientation):
        filtered_challenges_by_user[name] = [
            challenge for challenge in player_challenges[name] if orientation in challenge["player_orientation_sexuelle"]
        ]
        # print(f'Nombre de challenges restant pour {name} après choix orientation: {orientation}, {len(filtered_challenges_by_user[name])}')
        return filtered_challenges_by_user

    # Fonction pour retirer les gages de chaque joueur si non pratiqué
    def filter_challenges_by_pratique(name, pratique):
        filtered_challenges_by_user[name] = [challenge for challenge in filtered_challenges_by_user[name] if pratique not in challenge["player_pratiques"]]
        # print(f'Nombre de challenges restant pour {name} après choix pratique: {pratique}, {len(filtered_challenges_by_user[name])}')
        return filtered_challenges_by_user

    # Fonction pour mélanger les gages pour chaque joueur
    def randomize_challenges(name):
        return random.shuffle(filtered_challenges_by_user[name])

    # Fonction pour trier les gages par niveau et sous niveau pour chaque joueur
    def sort_challenges_by_levels(name, level_primary, level_secondary):
        return filtered_challenges_by_user[name].sort(key=lambda x: (x[level_primary], x[level_secondary]))

    # Fonction pour supprimer un gage de la liste de chaque joueur si celui si a été joué
    def remove_challenge(name, id):
        # print(f'Nombre de challenges avant suppression pour {name}: {len(filtered_challenges_by_user[name])}')
        filtered_challenges_by_user[name] = [
            challenge for challenge in filtered_challenges_by_user[name] if id not in challenge["id"]
        ]
        # print(f'Nombre de challenges après suppression pour {name}: {len(filtered_challenges_by_user[name])}')
        return filtered_challenges_by_user

    # Fonction pour créer la liste partenaires_restant contenant les partenaires compatibles
    def filter_partenaire_by_orientation(joueur, orientation, participants):
        partenaires_restant = participants.copy()
        partenaires_restant.pop(current_player_index)

        partenaires_orientation_compatible = COMPATIBILITY_MAP.get(orientation) # retourne la liste des orientations des partenaires compatibles avec le joueur
        # print(f'Orientations compatibles: {partenaires_orientation_compatible}')

        filtered_partenaire_by_orientation = {joueur.name:[]}
        # Parcourir la liste des partenaires restants
        # print(f'Nombre de partenaires potentiel restant: {len(partenaires_restant)}') # Retourne le nombre de partenaires compatibles avec le joueur
        j=0
        for i in range(len(partenaires_restant)): # i=0 puis i= 1
            if len(partenaires_restant) > 0: # Si il reste des partenaires dans la liste
                if partenaires_restant[0].orientation in partenaires_orientation_compatible:
                    # print(f'Un partenaire compatible a été trouvé: "id": {j}, "name": {partenaires_restant[0].name}')
                    # Ajout du partenaire a la liste du joueur
                    valeurs={"name": partenaires_restant[0].name, "orientation": partenaires_restant[0].orientation, "gender": partenaires_restant[0].gender}
                    filtered_partenaire_by_orientation[joueur.name].append(valeurs)
                    # Supprime le partenaire a la liste partenaires_restant
                    partenaires_restant.pop(0)
                    j = j+1
                else:
                    # Le partenaire actuel est incompatible avec le joueur, on le supprime de la liste partenaires_restant sans l'ajouter a la liste du joueur
                    partenaires_restant.pop(0)

        if len(filtered_partenaire_by_orientation[joueur.name]) > 0:
            # Mélanger la liste des partenaires pour une affectation aléatoire
            random.shuffle(filtered_partenaire_by_orientation[joueur.name])

            # Créer des variables dynamiquement et les affecter aux partenaires
            # print(f'Enum ala ligne 168: {enumerate(filtered_partenaire_by_orientation[joueur.name], start=1)}')
            for i, p in enumerate(filtered_partenaire_by_orientation[joueur.name], start=1):
                globals()[f'partenaire_{i}'] = p["name"]
                # print(f'partenaire_{i} = {globals()[f"partenaire_{i}"]}')

        return [filtered_partenaire_by_orientation[joueur.name]]

###########################################################################################
# Ici commence le questionnaire
###########################################################################################
label questionnaire():
    h "Pour vous offrir un accompagnement personnalisé, je vais procéder à l'enregistrement de vos préférences via un bref questionnaire." # To offer you personalized support, I will record your preferences via a brief questionnaire.
    $ msg = _("Avant de commencer, pourriez-vous m'indiquer le nombre de participants à cette session (entre 2 et 6 personnes)?")
    $ nbrJoueur = renpy.input(msg, allow="23456", length=1) # Before starting, could you tell me the number of participants in this session (between 2 and 6 people)?
    $ nbrJoueur = int(nbrJoueur.strip())

    if nbrJoueur < 2:
        $ msg = _("Merci de m'indiquer le nombre de participants à cette session ? (2 au minimum)")
        $ nbrJoueur = renpy.input(msg, allow="23456")
        $ nbrJoueur = int(nbrJoueur.strip())

    if nbrJoueur < 2:
        h "Vous n'êtes pas coopératif, je mets fin au jeu." # You are not cooperative, I end the game.
        jump by

    if nbrJoueur > 9:
        h "Ouah vous êtes trop nombreux, je mets fin au jeu." # Wow there are too many player, I'm ending the game.
        jump by

    if nbrJoueur > 1:
        $ i = 0
        while i <= nbrJoueur-1:
            # récupération des noms
            $ msg = _("Nom du joueur {} :")
            $ name = renpy.input(msg.format(i+1)).strip()
            if not name:
                $ msg = _("Nom du joueur {} (obligatoire) :")
                $ name = renpy.input(msg.format(i+1)).strip()
                if not name:
                    h "Vous n'êtes pas coopératif, je mets fin au jeu." # You are not cooperative, I end the game.
                    jump by
            menu:
                h "Pourriez-vous m'indiquer votre identité de genre ?" # Could you tell me your gender identity?
                "Je suis un homme": # I am a man
                    $ gender = "h"
                "Je suis une femme": # I am a woman
                    $ gender = "f"
            $ assigned_challenges[name] = assign_challenges_to_players_by_gender(name, gender)

            h "A partir de maintenant, vous pouvez masquer vos réponses a votre partenaire pour ajouter une touche de suspense et d'excitation." # From now on, you can hide your answers from your partner to add a touch of suspense and excitement.

            # Homme
            if gender == "h":
                menu:
                    h "Précisez votre orientation sexuelle" # Specify your sexual orientation
                    "Je suis hétérosexuel": # I am heterosexual
                        $ orientation ="h_hetero"
                        $ renpy.notify(_("Orientation hétérosexuel a été ajouté à vos préférences")) # Heterosexual orientation has been added to your preferences
                    "Je suis homosexuel": # I am homosexual
                        $ orientation ="gay"
                        $ renpy.notify(_("Orientation homosexuel a été ajouté à vos préférences")) # Homosexual orientation has been added to your preferences
                    "Je suis bisexuel": # I am bisexual
                        $ orientation ="h_bi"
                        $ renpy.notify(_("Orientation bisexuel a été ajouté à vos préférences")) # Bisexual orientation has been added to your preferences
                $ assigned_challenges[name] = filter_challenges_by_orientation(name, orientation)
                h "A présent , veuillez m'indiquez les pratiques sexuelles que vous appréciez." # Now, please tell me the sexual practices that you enjoy.
                "FUN"
                menu:
                    "J'aime les jeux de rôle, les défis": # I like role-playing games, challenges
                        $ fun = True
                        $ renpy.notify(_("Les jeux de rôle ont été ajouté à vos préférences")) # Role playing games have been added to your preferences
                    "Je n'aime pas les jeux de rôle, les défis":
                        $ fun = False
                        $ renpy.notify(_("Les jeux de rôle ont été retiré de vos préférences")) # Role playing games have been removed from your preferences
                        # On retire les gages avec fun
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "fun")
                "L'ORAL"
                if orientation =="h_hetero":
                    menu:
                        "J'aime goûter au sexe de ma partenaire": # I like to taste my partner's sex
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été ajouté à vos préférences")) # Tasting your partner's sex has been added to your preferences
                        "Je n'aime pas goûter au sexe de ma partenaire": # I don't like tasting my partner's sex
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été retiré de vos préférences")) # Tasting your partner's sex has been removed from your preferences
                            # On retire les gages avec sexe_oral_actif
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                elif orientation =="gay":
                    menu:
                        "J'aime goûter au sexe de mon partenaire": # I like to taste my partner's penis
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été ajouté à vos préférences")) # Tasting your partner's penis has been added to your preferences
                        "Je n'aime pas goûter au sexe de mon partenaire":
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été retiré de vos préférences")) # Tasting your partner's penis has been removed from your preferences
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                else:
                    menu:
                        "J'aime goûter au sexe de mon ou ma partenaire": # I like to taste my partner's sex
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de vos partenaires a été ajouté à vos préférences")) # Tasting your partner's sex has been added to your preferences
                        "Je n'aime pas goûter au sexe de mon ou ma partenaire":
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de vos partenaires a été retiré de vos préférences")) # Tasting your partner's sex has been removed from your preferences
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                menu:
                    "J'aime que l'on goûte à mon sexe": # I like people to taste my penis
                        $ sexe_oral_passif = True
                        $ renpy.notify(_("Goûter a votre sexe a été ajouté à vos préférences")) # Taste Your penis has been added to your Preferences
                    "Je n'aime pas que l'on à goûte mon sexe":
                        $ sexe_oral_passif = False
                        $ renpy.notify(_("Goûter a votre sexe a été retiré de vos préférences")) # Taste Your penis has been removed from your Preferences
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_passif")
                menu:
                    "J'aime goûter l'anus de mon ou ma partenaire": # I like to taste my partner's anus
                        $ anus_oral_actif = True
                        $ renpy.notify(_("Goûter a l'anus de votre partenaire a été ajouté à vos préférences")) # Tasting your partner's anus has been added to your preferences
                    "Je n'aime pas goûter l'anus de mon ou ma partenaire":
                        $ anus_oral_actif = False
                        $ renpy.notify(_("Goûter a l'anus de votre partenaire a été retiré de vos préférences")) # Tasting your partner's anus has been removed from your preferences
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_passif")
                menu:
                    "J'aime que l'on goûte à mon anus": # I like people to taste my anus
                        $ anus_oral_passif = True
                        $ renpy.notify(_("Goûter a votre anus a été ajouté à vos préférences")) # Taste Your Anus has been added to your Preferences
                    "Je n'aime pas que l'on goûte à mon anus":
                        $ anus_oral_passif = False
                        $ renpy.notify(_("Goûter a votre anus a été retiré de vos préférences")) # Taste Your Anus has been removed from your Preferences
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_passif")
                "LA PÉNÉTRATION"
                if orientation !="gay":
                    menu:
                        "J'aime pénétrer le sexe de ma partenaire":
                            $ sexe_penetration_actif = True
                            $ renpy.notify(_("Pénétrer le sexe de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas pénétrer le sexe de ma partenaire":
                            $ sexe_penetration_actif = False
                            $ renpy.notify(_("Pénétrer le sexe de votre partenaire a retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_penetration_actif")
                else:
                    $ sexe_penetration_actif = False
                    $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_penetration_actif")

                menu:
                    "J'aime caresser et doigter l'anus de mon ou ma partenaire":
                        $ anus_caresse_actif = True
                        $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été ajouté à vos préférences"))
                    "Je n'aime pas caresser et doigter l'anus de mon ou ma partenaire":
                        $ anus_caresse_actif = False
                        $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_actif")

                if orientation =="h_hetero":
                    menu:
                        "J'aime sodomiser ma partenaire":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser ma partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                elif orientation =="gay":
                    menu:
                        "J'aime sodomiser mon partenaire":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser mon partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                else:
                    menu:
                        "J'aime sodomiser ma ou mon partenaire":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser vos partenaires a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser ma ou mon partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser vos partenaires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                menu:
                    "J'aime que l'on me caresse et que l'on me doigte l'anus":
                        $ anus_caresse_passif = True
                        $ renpy.notify(_("Caresser et doigter votre anus a été ajouté à vos préférences"))
                    "Je n'aime pas que l'on me caresse et que l'on me doigte l'anus":
                        $ anus_caresse_passif = False
                        $ renpy.notify(_("Caresser et doigter votre anus a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_passif")
                if orientation =="h_hetero":
                    menu:
                        "J'aime que ma partenaire me sodomise":
                            $ anus_penetration_passif = True
                            $ renpy.notify(_("Sodomisé par votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas que ma partenaire me sodomise":
                            $ anus_penetration_passif = False
                            $ renpy.notify(_("Sodomisé par votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_passif")
                elif orientation =="gay":
                    menu:
                        "J'aime que mon partenaire me sodomise":
                            $ anus_penetration_passif = True
                            $ renpy.notify(_("Sodomisé par votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas que mon partenaire me sodomise":
                            $ anus_penetration_passif = False
                            $ renpy.notify(_("Sodomisé par votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_passif")
                else:
                    menu:
                        "J'aime que l'on me sodomise":
                            $ anus_penetration_passif = True
                            $ renpy.notify(_("Vous faire sodomisé a été ajouté à vos préférences"))
                        "Je n'aime pas que l'on me sodomise":
                            $ anus_penetration_passif = False
                            $ renpy.notify(_("Vous faire sodomisé a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_passif")
                "BDSM"
                menu:
                    "J'aime les petits jeux de soumission":
                        $ soumission_soft = True
                        $ renpy.notify(_("Les petits jeux de soumission ont été ajouté à vos préférences"))
                    "Je n'aime pas les petits jeux de soumission":
                        $ soumission_soft = False
                        $ renpy.notify(_("Les petits jeux de soumission ont été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "soumission_soft")
                menu:
                    "J'aime me sentir dominé par un maître ou une maîtresse même si cela comprend douleurs et humiliations":
                        $ soumission_hard = True
                        $ renpy.notify(_("Être dominé été ajouté à vos préférences"))
                    "Je n'aime pas me sentir dominé":
                        $ soumission_hard = False
                        $ renpy.notify(_("Être dominé été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "soumission_hard")
                menu:
                    "J'aime les petits jeux de domination":
                        $ domination_soft = True
                        $ renpy.notify(_("Les petits jeux de domination ont été ajouté à vos préférences"))
                    "Je n'aime pas les petits jeux de domination":
                        $ domination_soft = False
                        $ renpy.notify(_("Les petits jeux de domination ont été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "domination_soft")
                menu:
                    "J'aime dominer mon ou ma partenaire et je sais punir sans blesser et humilier ni moquer":
                        $ domination_hard = True
                        $ renpy.notify(_("Dominer vos partenaires été ajouté à vos préférences"))
                    "Je n'aime pas dominer mon ou ma partenaire":
                        $ domination_hard = False
                        $ renpy.notify(_("Dominer vos partenaires été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "domination_hard")

                "SPERME"
                menu:
                    "J'aime goûter le sperme":
                        $ sperme_soft = True
                        $ renpy.notify(_("Goûter le sperme été ajouté à vos préférences"))
                    "Je n'aime pas goûter le sperme":
                        $ sperme_soft = False
                        $ renpy.notify(_("Goûter le sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_soft")
                menu:
                    "J'aime avaler le sperme":
                        $ sperme_hard = True
                        $ renpy.notify(_("Avaler le sperme été ajouté à vos préférences"))
                    "Je n'aime pas avaler le sperme":
                        $ sperme_hard = False
                        $ renpy.notify(_("Avaler le sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_hard")
                menu:
                    "J'aime goûter mon sperme":
                        $ sperme_perso_soft = True
                        $ renpy.notify(_("Goûter votre sperme été ajouté à vos préférences"))
                    "Je n'aime pas goûter mon sperme":
                        $ sperme_perso_soft = False
                        $ renpy.notify(_("Goûter votre sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_perso_soft")
                menu:
                    "J'aime avaler mon sperme":
                        $ sperme_perso_hard = True
                        $ renpy.notify(_("Avaler votre sperme été ajouté à vos préférences"))
                    "Je n'aime pas avaler mon sperme":
                        $ sperme_perso_hard = False
                        $ renpy.notify(_("Avaler votre sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_perso_hard")
            # Femme
            else:
                menu:
                    h "Précisez votre orientation sexuelle"
                    "Je suis hétérosexuelle":
                        $ orientation ="f_hetero"
                        $ renpy.notify(_("Orientation hétérosexuel a été ajouté à vos préférences"))
                    "Je suis lesbienne":
                        $ orientation ="lesbienne"
                        $ renpy.notify(_("Orientation lesbienne a été ajouté à vos préférences"))
                    "Je suis bisexuelle":
                        $ orientation ="f_bi"
                        $ renpy.notify(_("Orientation bisexuelle a été ajouté à vos préférences"))
                $ assigned_challenges[name] = filter_challenges_by_orientation(name, orientation)
                h "A présent , veuillez m'indiquez les pratiques sexuelles que vous appréciez."
                $ sperme_perso_soft = False
                $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_perso_soft")

                $ sperme_perso_hard = False
                $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_perso_hard")
                "FUN"
                menu:
                    "J'aime les jeux de rôle, les défis":
                        $ fun = True
                        $ renpy.notify(_("Les jeux de rôle ont été ajouté à vos préférences"))
                    "Je n'aime pas les jeux de rôle, les défis":
                        $ fun = False
                        $ renpy.notify(_("Les jeux de rôle ont été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "fun")
                "L'ORAL"
                if orientation =="f_hetero":
                    menu:
                        "J'aime goûter au sexe de mon partenaire":
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas goûter au sexe de mon partenaire":
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                elif orientation =="lesbienne":
                    menu:
                        "J'aime goûter au sexe de ma partenaire":
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas goûter au sexe de ma partenaire":
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                else:
                    menu:
                        "J'aime goûter au sexe de mon ou ma partenaire":
                            $ sexe_oral_actif = True
                            $ renpy.notify(_("Goûter au sexe de vos partenaires a été ajouté à vos préférences"))
                        "Je n'aime pas goûter au sexe de mon ou ma partenaire":
                            $ sexe_oral_actif = False
                            $ renpy.notify(_("Goûter au sexe de vos partenaires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_actif")
                menu:
                    "J'aime que l'on goûte à mon sexe":
                        $ sexe_oral_passif = True
                        $ renpy.notify(_("Goûter a votre sexe a été ajouté à vos préférences"))
                    "Je n'aime pas que l'on à goûte mon sexe":
                        $ sexe_oral_passif = False
                        $ renpy.notify(_("Goûter a votre sexe a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_oral_passif")

                if orientation == "f_hetero":
                    menu:
                        "J'aime goûter l'anus de mon partenaire":
                            $ anus_oral_actif = True
                            $ renpy.notify(_("Goûter a l'anus de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas goûter l'anus de mon partenaire":
                            $ anus_oral_actif = False
                            $ renpy.notify(_("Goûter a l'anus de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_oral_actif")
                elif orientation =="lesbienne":
                    menu:
                        "J'aime goûter l'anus de ma partenaire":
                            $ anus_oral_actif = True
                            $ renpy.notify(_("Goûter a l'anus de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas goûter l'anus de ma partenaire":
                            $ anus_oral_actif = False
                            $ renpy.notify(_("Goûter a l'anus de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_oral_actif")
                else:
                    menu:
                        "J'aime goûter l'anus de mon ou ma partenaire":
                            $ anus_oral_actif = True
                            $ renpy.notify(_("Goûter a l'anus de vos partenaires a été ajouté à vos préférences"))
                        "Je n'aime pas goûter l'anus de mon ou ma partenaire":
                            $ anus_oral_actif = False
                            $ renpy.notify(_("Goûter a l'anus de vos partenaires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_oral_actif")
                menu:
                    "J'aime que l'on goûte à mon anus":
                        $ anus_oral_passif = True
                        $ renpy.notify(_("Goûter a votre anus a été ajouté à vos préférences"))
                    "Je n'aime pas que l'on goûte à mon anus":
                        $ anus_oral_passif = False
                        $ renpy.notify(_("Goûter a votre anus a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_oral_passif")

                "LA PÉNÉTRATION"
                if orientation != "lesbienne":
                    menu:
                        "J'aime être pénétrée par un homme ou un accessoire":
                            $ sexe_penetration_passif = True
                            $ renpy.notify(_("Être pénétrée par un homme ou un accessoire a été ajouté à vos préférences"))
                        "Je n'aime pas être pénétrer":
                            $ sexe_penetration_passif = False
                            $ renpy.notify(_("Être pénétrée par un homme ou un accessoire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_penetration_passif")
                else:
                    menu:
                        "J'aime être pénétrée par un accessoire":
                            $ sexe_penetration_passif = True
                            $ renpy.notify(_("Être pénétrée par un accessoire a été ajouté à vos préférences"))
                        "Je n'aime pas être pénétrer":
                            $ sexe_penetration_passif = False
                            $ renpy.notify(_("Être pénétrée par un accessoire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_penetration_passif")
                if orientation != "f_hetero":
                    menu:
                        "J'aime pénétrée ma partenaire à l'aide d'accessoires":
                            $ sexe_penetration_actif = True
                            $ renpy.notify(_("Pénétrée votre partenaire à l'aide d'accessoires a été ajouté à vos préférences"))
                        "Je n'aime pas pénétrée ma partenaire":
                            $ sexe_penetration_actif = False
                            $ renpy.notify(_("Pénétrée votre partenaire à l'aide d'accessoires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sexe_penetration_actif")

                if orientation == "f_hetero":
                    menu:
                        "J'aime caresser et doigter l'anus de mon partenaire":
                            $ anus_caresse_actif = True
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas caresser et doigter l'anus de mon partenaire":
                            $ anus_caresse_actif = False
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_actif")
                elif orientation == "lesbienne":
                    menu:
                        "J'aime caresser et doigter l'anus de ma partenaire":
                            $ anus_caresse_actif = True
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas caresser et doigter l'anus de ma partenaire":
                            $ anus_caresse_actif = False
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_actif")
                else:
                    menu:
                        "J'aime caresser et doigter l'anus de mon ou ma partenaire":
                            $ anus_caresse_actif = True
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été ajouté à vos préférences"))
                        "Je n'aime pas caresser et doigter l'anus de mon ou ma partenaire":
                            $ anus_caresse_actif = False
                            $ renpy.notify(_("Caresser et doigter l'anus de votre partenaire a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_actif")

                if orientation == "f_hetero":
                    menu:
                        "J'aime sodomiser mon partenaire à l'aide d'accessoires":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser votre partenaire à l'aide d'accessoires a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser mon partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser votre partenaire à l'aide d'accessoires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                elif orientation == "lesbienne":
                    menu:
                        "J'aime sodomiser ma partenaire à l'aide d'accessoires":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser votre partenaire à l'aide d'accessoires a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser ma partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser votre partenaire à l'aide d'accessoires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                else:
                    menu:
                        "J'aime sodomiser mon ou ma partenaire à l'aide d'accessoires":
                            $ anus_penetration_actif = True
                            $ renpy.notify(_("Sodomiser vos partenaires a été ajouté à vos préférences"))
                        "Je n'aime pas sodomiser mon ou ma partenaire":
                            $ anus_penetration_actif = False
                            $ renpy.notify(_("Sodomiser vos partenaires a été retiré de vos préférences"))
                            $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_actif")
                menu:
                    "J'aime que l'on me caresse et que l'on me doigte l'anus":
                        $ anus_caresse_passif = True
                        $ renpy.notify(_("Caresser et doigter votre anus a été ajouté à vos préférences"))
                    "Je n'aime pas que l'on me caresse et que l'on me doigte l'anus":
                        $ anus_caresse_passif = False
                        $ renpy.notify(_("Caresser et doigter votre anus a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_caresse_passif")
                menu:
                    "J'aime que l'on me sodomise":
                        $ anus_penetration_passif = True
                        $ renpy.notify(_("Se faire sodomisé a été ajouté à vos préférences"))
                    "Je n'aime pas que l'on me sodomise":
                        $ anus_penetration_passif = False
                        $ renpy.notify(_("Se faire sodomisé a été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "anus_penetration_passif")
                "BDSM"
                menu:
                    "J'aime les petits jeux de soumission":
                        $ soumission_soft = True
                        $ renpy.notify(_("Les petits jeux de soumission ont été ajouté à vos préférences"))
                    "Je n'aime pas les petits jeux de soumission":
                        $ soumission_soft = False
                        $ renpy.notify(_("Les petits jeux de soumission ont été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "soumission_soft")
                menu:
                    "J'aime me sentir dominé par un maître ou une maîtresse même si cela comprend douleurs et humiliations":
                        $ soumission_hard = True
                        $ renpy.notify(_("Être dominé été ajouté à vos préférences"))
                    "Je n'aime pas me sentir dominé":
                        $ soumission_hard = False
                        $ renpy.notify(_("Être dominé été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "soumission_hard")
                menu:
                    "J'aime les petits jeux de domination":
                        $ domination_soft = True
                        $ renpy.notify(_("Les petits jeux de domination ont été ajouté à vos préférences"))
                    "Je n'aime pas les petits jeux de domination":
                        $ domination_soft = False
                        $ renpy.notify(_("Les petits jeux de domination ont été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "domination_soft")
                menu:
                    "J'aime dominer mon ou ma partenaire et je sais punir sans blesser et humilier ni moquer":
                        $ domination_hard = True
                        $ renpy.notify(_("Dominer vos partenaires été ajouté à vos préférences"))
                    "Je n'aime pas dominer mon ou ma partenaire":
                        $ domination_hard = False
                        $ renpy.notify(_("Dominer vos partenaires été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "domination_hard")
                "SPERME"
                menu:
                    "J'aime goûter le sperme":
                        $ sperme_soft = True
                        $ renpy.notify(_("Goûter le sperme été ajouté à vos préférences"))
                    "Je n'aime pas goûter le sperme":
                        $ sperme_soft = False
                        $ renpy.notify(_("Goûter le sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_soft")
                menu:
                    "J'aime avaler le sperme":
                        $ sperme_hard = True
                        $ renpy.notify(_("Avaler le sperme été ajouté à vos préférences"))
                    "Je n'aime pas avaler le sperme":
                        $ sperme_hard = False
                        $ renpy.notify(_("Avaler le sperme été retiré de vos préférences"))
                        $ assigned_challenges[name] = filter_challenges_by_pratique(name, "sperme_hard")

            # Affectation du genre de partenaire compatible au joueur actuel
            $ partner_orientation = COMPATIBILITY_MAP.get(orientation, [])

            # Création du joueur
            $ player = Player(i, name, gender, orientation, sexe_oral_actif, sexe_oral_passif, anus_oral_actif, anus_oral_passif, sexe_penetration_actif, anus_caresse_actif, anus_penetration_actif, anus_caresse_passif, anus_penetration_passif, fun, soumission_soft, soumission_hard, domination_soft, domination_hard, sperme_soft, sperme_hard, sperme_perso_soft, sperme_perso_hard, partner_orientation)
            # Ajout du joueur a la liste des participants
            $ participants.append(player)
            # TODO revoir l'affectation, ce n'est pas le bon moment pour affecter des challenges, on doit le faire a chaque tour de jeux
            # Affectation de challenges au joueur actuel
            $ assigned_challenges[name] = randomize_challenges(name)

            $ i += 1
    h "À tour de rôle vous aurez des défis à relever certain avec des accessoires que vous aurez choisis."
    h "Au fur et à mesure de la partie le niveau deviendra de plus en plus chaud."
    h "Arrivé au dernier niveau vous serez prêt pour la finale."
    # Mélanger les énigmes
    $ randomize_all_challenges(all_challenges)
    # Trier les challenges par niveau de difficulté et sous niveau
    $ sort_all_challenges_by_levels("level_primary", "level_secondary")
    jump control

label control:
    # Ici on contrôle que le jeux peut être lancé car les joueurs sont compatible
    # interdire les retours en arrière
    $ renpy.block_rollback()
    # Index du joueur principal
    $ joueur_principale = participants[current_player_index]
    $ joueur_principale_name = joueur_principale.name
    # $ print(f'joueur_principale.name: {joueur_principale_name}')
    # $ partenaires_compatibles=[]
    # récupération des noms des partenaires avec des orientations compatibles
    $ partenaires_compatibles = filter_partenaire_by_orientation(joueur_principale, joueur_principale.orientation, participants)

    # Si aucun partenaire compatible on mets fin au jeu
    if len(partenaires_compatibles[0]) == 0:
        h "[joueur_principale.name], selon les choix que vous m'avez fournis, vous ne pouvez pas jouer avec un partenaire car vous n'avais pas d'affinités sexuelle à partager ensemble."
        h "Je n'ais d'autre choix que de mettre fin au jeu."
        jump exit
    else:
        $ i = 1
        while i <= len(partenaires_compatibles):
            # $ print(f' nombre de partenaires compatible: {len(partenaires_compatibles)}')
            # $ print(f'partenaire_{i} = {globals()[f"partenaire_{i}"]}')
            $ i += 1
        jump gages
