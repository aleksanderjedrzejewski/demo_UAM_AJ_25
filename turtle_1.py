import turtle

# Set up the turtle
window = turtle.Screen()
window.bgcolor("black")
window.title("Spiral Art")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw spiral
for i in range(360):
    pen.color(colors[i % len(colors)])
    pen.forward(i * 1.5)
    pen.left(59)

# Finish drawing
turtle.done()