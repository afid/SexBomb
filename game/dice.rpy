init python:
    import random

    def generate_number_dice(start, end):
        """
        Génère et affiche un ou plusieurs dés avec un effet d'animation dans Ren'Py.

        Cette fonction détermine aléatoirement les valeurs des dés en fonction des paramètres `start` et `end`.
        Elle affiche ensuite les images des dés sur l'écran en appliquant un effet d'apparition fluide.

        Paramètres:
        -----------
        start : int
            Valeur minimale du lancer de dé (doit être ≥ 1).
        end : int
            Valeur maximale du lancer de dé (limité à 12 max).

        Fonctionnement:
        ---------------
        - Si `end` ≤ 6, un seul dé est affiché.
        - Si `end` > 6, deux dés sont affichés (limité à un maximum de 12).
        - Les dés sont affichés côte à côte avec des effets de transition et de zoom.

        Retourne:
        ---------
        list[str]
            Liste contenant les noms des images des dés affichés (ex: `['3_first', '5_second']`).

        Exemple:
        --------
        >>> generate_number_dice(1, 6)
        ['4_first']

        >>> generate_number_dice(1, 10)
        ['2_first', '5_second']
        """
        results_dices_value = 0
        results_dices_images = []
        max_dice_value = 6  # Valeur max pour un seul dé

        # Calcul du nombre de dés nécessaires
        num_dices = min((end // max_dice_value), 2)  # Limité à 2 dés pour l'affichage

        # Positions spécifiques pour éviter la superposition
        dice_positions = [dice_transform_1, dice_transform_2]
        dice_names = ["first", "second"]

        for i in range(num_dices):
            dice_value = random.randint(1, max_dice_value)
            results_dices_value = results_dices_value + dice_value
            image_dice = f"{dice_value}_{dice_names[i]}"
            results_dices_images.append(image_dice)
            # Affichage avec transformation pour éviter la superposition
            renpy.show(image_dice, at_list=[dice_positions[i]])
            renpy.pause(0.3)  # Effet de délai entre l'apparition des dés
            renpy.notify(f"Le nombre est généré par les dés est: {results_dices_value}")

        return results_dices_images

    def hide_dices(dice_images):
        """
        Masque les dés affichés à l'écran dans Ren'Py.

        Cette fonction prend une liste de noms d'images représentant les dés et
        les masque un par un à l'aide de `renpy.hide()`.

        Paramètres:
        -----------
        dice_images : list[str]
            Liste contenant les noms des images des dés à masquer.

        Fonctionnement:
        ---------------
        - Vérifie si la liste `dice_images` est vide pour éviter des traitements inutiles.
        - Parcourt chaque image de la liste et la masque avec `renpy.hide()`.

        Retourne:
        ---------
        None
            Cette fonction ne retourne rien, elle effectue seulement l'action de masquage.

        Exemple:
        --------
        >>> hide_dices(['3_first', '5_second'])
        # Les images '3_first' et '5_second' sont masquées.
        """
        if dice_images:  # Vérifie que la liste n'est pas vide
            for image in dice_images:
                renpy.hide(image)

# Transformations pour positionner les dés côte à côte
transform dice_transform_1:
    alpha 0.0 pos (0.92, 0.1)
    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0

transform dice_transform_2:
    alpha 0.0 pos (0.84, 0.1)
    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:
        linear .25 zoom 1.25 alpha 0.0
