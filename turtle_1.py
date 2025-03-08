import turtle

# Setup the window
window = turtle.Screen()
window.bgcolor("white")
window.title("Turtle Drawing")

# Create turtle
pen = turtle.Turtle()
pen.color("green")
pen.width(3)
pen.speed(2)

# Draw the shell
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.fillcolor("green")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Draw head
pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.fillcolor("green")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Draw legs
for x, y in [(-30,-20), (30,-20), (-30, -20), (30, -20)]:
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

# Hide turtle and finish
pen.hideturtle()
turtle.done()
