import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'black', 'yellow', 'orange', 'purple', 'pink', 'brown', 'cyan', 'green']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input ("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!!.")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers must be between 2 and 10... Try again!!.")

def race(colors):
    turtles = create_turtles(colors)
    winner = None
    while not winner:
        for racer in turtles:
            distance = random.randint(1, 10)
            racer.forward(distance)
            if racer.ycor() >= HEIGHT // 2 - 20:
                winner = racer
                break
    print(f"The winner is the {winner.color()[0]} turtle!")
    time.sleep(3)
    turtle.bye()



def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    return screen

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

