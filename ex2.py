import random

def jeu_de_devinette():
    # Générer un nombre aléatoire entre 1 et 100
    nombre_mystere = random.randint(1, 100)
    
    tentatives = 0
    devine = False

    print("Devinez le nombre entre 1 et 100!")

    while not devine:
        # Demander à l'utilisateur de deviner le nombre
        try:
            supposition = int(input("Entrez votre supposition: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        tentatives += 1

        # Vérifier si la supposition est correcte
        if supposition == nombre_mystere:
            devine = True
            print(f"Bravo! Vous avez deviné le nombre en {tentatives} tentatives.")
        elif supposition < nombre_mystere:
            print("Le nombre est plus élevé!")
        else:
            print("Le nombre est plus bas!")

if __name__ == "__main__":
    jeu_de_devinette()
