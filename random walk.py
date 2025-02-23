import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Random Walk")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the turtle
walker = turtle.Turtle()
walker.shape("turtle")
walker.speed("fast")
walker.pensize(2)

# List of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Random walk function
def random_walk(turtle, steps=1000):
    for _ in range(steps):
        turtle.color(random.choice(colors))  # Change to a random color
        turtle.forward(30)                  # Move forward by 30 units
        turtle.setheading(random.choice([0, 90, 180, 270]))  # Randomly set direction

# Execute the random walk
random_walk(walker)

# Keep the window open until clicked
screen.mainloop()

