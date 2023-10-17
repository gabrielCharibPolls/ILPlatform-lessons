import turtle
import random
import time

# Paramètres du jeu
GRID_SIZE = 20  # Taille de la grille
SNAKE_SPEED = 0.15  # Vitesse du serpent en secondes

# Initialisation de l'écran
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Création du serpent
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("blacks")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Création des pomes 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Fonction pour déplacer le serpent vers le haut
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

# Fonction pour déplacer le serpent vers le bas
def move_down():
    if snake.direction != "up":
        snake.direction = "down"

# Fonction pour déplacer le serpent vers la gauche
def move_left():
    if snake.direction != "right":
        snake.direction = "left"

# Fonction pour déplacer le serpent vers la droite
def move_right():
    if snake.direction != "left":
        snake.direction = "right"

# Écouter les événements clavier
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Déplacement du serpent
def move():
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

# Gestion des collisions avec la nourriture
def check_food_collision():
    if snake.distance(food) < GRID_SIZE:
        x = random.randint(-14, 14) * GRID_SIZE
        y = random.randint(-14, 14) * GRID_SIZE
        food.goto(x, y)

# Fonction principale du jeu
def main():
    while True:
        wn.update()
        move()
        check_food_collision()
        time.sleep(SNAKE_SPEED)

# Lancement du jeu
if __name__ == "__main__":
    main()
