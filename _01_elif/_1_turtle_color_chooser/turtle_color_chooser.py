import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    Bob = turtle.Turtle();
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    while True:
        for C in range(4):
            Bob.forward(100)
            Bob.right(90)
        #      3) Set the pen width to 10
        Bob.width(10)
        #      4) Ask the user what color pen they would like to draw with
        Input = simpledialog.askstring("Prompt", "What color?").lower()
        #      5) Use an if/else statement to set the pen color that the user
        #         requested
        if Input == "red":
            Bob.color("red")
        elif Input == "green":
            Bob.color("green")
        elif Input == "blue":
            Bob.color("blue")
        else:
            Bob.color(get_random_color())
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
