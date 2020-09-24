import turtle

turtle.hideturtle()
turtle.begin_fill()
turtle.color('red', 'pink')

x = 0
for x in range(2):
    turtle.setheading(90)
    turtle.circle(25, 180)
    x += 1

turtle.setheading(300)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.end_fill()
input()