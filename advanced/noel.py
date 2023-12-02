import random

def print_tree(height):
    for i in range(height):
        row = ''
        for j in range(height - i - 1):
            row += ' '
        for j in range(2 * i + 1):
            ####################################################
            # Choix aléatoire  une décoration ou une branche
            ####################################################
            if random.choice([True, False]):
                row += '*'
            else:
                row += 'O'
        print(row)
    #############################
    #tronc à l'arbre
    #################################
    for i in range(3):
        print(' ' * (height - 2) + '###')

def main():
    while True:
        try:
            height = int(input("Entrez la hauteur de l'arbre de Noël (entre 3 et 20) : "))
            if 3 <= height <= 20:
                break
            else:
                print("S'il vous plaît, entrez un nombre entre 3 et 20.")
        except ValueError:
            print("S'il vous plaît, entrez un nombre valide.")

    print_tree(height)

main()
