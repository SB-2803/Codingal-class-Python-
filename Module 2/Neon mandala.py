import turtle
import random
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

colours = ["red", "orange", "yellow", "lime", "cyan", "violet", "blue", "pink", "white", "lightblue", "deeppink"]
spiral = random.randint(40,100)
for i in range(spiral):
    board.color(random.choice(colours))
    board.width(2)
    board.forward(i * 4)
    board.right(91)

#Part 2: Star
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color(random.choice(colours), random.choice(colours))
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

#Part 3: Solid square spiral
board.penup()
board.goto(0,0)
board.pendown()
for i in range(36):
    board.color(random.choice(colours), random.choice(colours))
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

#done() keeps the window open even when the pattern has been created or else it will close
turtle.done()