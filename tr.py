import turtle
import time

WIDTH, HEIGHT = 500, 500

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


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    return screen

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(25)
