# Importation des modules nécessaires pour le jeu
import turtle
import random
import time

############################### Paramètres du jeu ###############################
# Taille de chaque carré de la grille du jeu
GRID_SIZE = 20  
# Combien de temps (en secondes) entre chaque mouvement du serpent
SNAKE_SPEED = 0.15  

############################### Initialisation de l'écran ###############################
# Crée une fenêtre où le jeu va se jouer
wn = turtle.Screen()
# Définit la couleur de fond de la fenêtre de jeu
wn.bgcolor("black")
# Définit la largeur et la hauteur de la fenêtre de jeu
wn.setup(width=600, height=600)
# Dit à la fenêtre de ne pas dessiner les animations automatiquement
wn.tracer(0)

############################### Création du serpent ###############################
# Crée un nouvel objet "turtle" qui sera notre serpent
snake = turtle.Turtle()
# Le serpent se déplace instantanément sans animation
snake.speed(0)
# Donne une forme carrée au serpent
snake.shape("square")
# Donne la couleur noir au serpent
snake.color("black")
# Lève le stylo pour que le serpent ne dessine pas quand il bouge
snake.penup()
# Place le serpent au centre de la fenêtre
snake.goto(0, 0)
# Définit la direction initiale du serpent comme étant 'stop' (arrêté)
snake.direction = "stop"

############################### Création des pommes ###############################
# Crée un nouvel objet "turtle" qui sera la nourriture du serpent
food = turtle.Turtle()
# La nourriture se déplace instantanément sans animation
food.speed(0)
# Donne une forme ronde à la nourriture
food.shape("circle")
# Donne la couleur rouge à la nourriture
food.color("red")
# Lève le stylo pour que la nourriture ne dessine pas quand elle bouge
food.penup()
# Place la nourriture à un endroit aléatoire sur la grille
food.goto(0, 100)

############################### Fonctions de déplacement ###############################
# Ces fonctions définissent comment le serpent se déplace
def move_up():
    # Si le serpent ne se déplace pas vers le bas, il peut aller vers le haut
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    # Si le serpent ne se déplace pas vers le haut, il peut aller vers le bas
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    # Si le serpent ne se déplace pas vers la droite, il peut aller vers la gauche
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    # Si le serpent ne se déplace pas vers la gauche, il peut aller vers la droite
    if snake.direction != "left":
        snake.direction = "right"

# Configure la fenêtre pour écouter les appuis de touches du clavier
wn.listen()
# Quand la flèche du haut est pressée, le serpent va vers le haut
wn.onkey(move_up, "Up")
# Quand la flèche du bas est pressée, le serpent va vers le bas
wn.onkey(move_down, "Down")
# Quand la flèche de gauche est pressée, le serpent va vers la gauche
wn.onkey(move_left, "Left")
# Quand la flèche de droite est pressée, le serpent va vers la droite
wn.onkey(move_right, "Right")

############################### Déplacement du serpent ###############################
# Cette fonction fait bouger le serpent dans la direction où il se dirige
def move():
    # Bouge le serpent dans la direction actuelle
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + GRID_SIZE)
       
        

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - GRID_SIZE)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - GRID_SIZE)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + GRID_SIZE)

############################### Gestion des collisions avec la nourriture ###############################
# Vérifie si le serpent a atteint la nourriture
def check_food_collision():
    # Si le serpent touche la nourriture, place la nourriture à un nouvel endroit
    if snake.distance(food) < GRID_SIZE:
        # Choisit un nouvel emplacement aléatoire pour la nourriture
        x = random.randint(-14, 14) * GRID_SIZE
        y = random.randint(-14, 14) * GRID_SIZE
        food.goto(x, y)
########################################################################################
#verifier si le serpent sort de la fenêtre de jeu -> returne un boolean 

def check_boundary_collision():
    x = snake.xcor
    y = snake.ycor

    if x > 290 or x < -290 or y > 290 or y < -290:
        game_over()  # Affiche le message Game Over
        return True
    return False
    

############################### Affiche le message Game Over ###############################
def game_over():
    # Efface le serpent et la nourriture
    snake.hideturtle()
    food.hideturtle()
    
    # Affiche le message Game Over
    wn.clear()
    wn.bgcolor("black")
    game_over_turtle = turtle.Turtle()
    game_over_turtle.color("white")
    game_over_turtle.penup()
    game_over_turtle.hideturtle()
    game_over_turtle.goto(0, 0)
    game_over_turtle.write("Game Over", align="center", font=("Courier", 24, "normal"))
############################### Fonction principale du jeu ###############################
# La fonction principale qui démarre le jeu
def main():
    while True:
        # Met à jour l'écran du jeu
        wn.update()
        # Fait bouger le serpent
        move()
        # Vérifie si le serpent a mangé la nourriture
        check_food_collision()
        check_boundary_collision()
        # Fait une pause dans le jeu pour contrôler la vitesse du serpent
        if check_boundary_collision():
            break
        time.sleep(SNAKE_SPEED)
###############################################################################################

# Vérifie si ce fichier est le fichier principal exécuté et lance le jeu
if __name__ == "__main__":
    main()
