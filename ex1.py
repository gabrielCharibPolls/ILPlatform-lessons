import random

def choisir_mot():
    liste_mots = ["chat", "chien", "oiseau", "python", "pendu"]
    return random.choice(liste_mots)

def afficher_mot(mot, lettres_trouvees):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre
        else:
            affichage += "_"
    return affichage

def jeu_du_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives = 6

    print("Bienvenue au jeu du pendu!")
    print(afficher_mot(mot_a_deviner, lettres_trouvees))

    while tentatives > 0:
        lettre_choisie = input("\nChoisissez une lettre: ").lower()

        if lettre_choisie in lettres_trouvees:
            print("Vous avez déjà choisi cette lettre.")
            continue

        if lettre_choisie in mot_a_deviner:
            lettres_trouvees.append(lettre_choisie)
            print("Bravo!")
        else:
            tentatives -= 1
            print(f"Dommage! Il vous reste {tentatives} tentatives.")

        print(afficher_mot(mot_a_deviner, lettres_trouvees))

        if "_" not in afficher_mot(mot_a_deviner, lettres_trouvees):
            print("\nFélicitations! Vous avez deviné le mot!")
            return

    print("\nFin du jeu. Le mot était:", mot_a_deviner)

jeu_du_pendu()
