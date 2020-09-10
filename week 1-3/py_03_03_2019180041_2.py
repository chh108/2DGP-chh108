import turtle

turtle.penup()
turtle.goto(-400, 300)

for i in range(6):
    turtle.pendown()
    turtle.forward(500)
    turtle.backward(500)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

turtle.penup()
turtle.goto(-400, 300)
turtle.right(90)

for i in range(6):
    turtle.pendown()
    turtle.forward(500)
    turtle.backward(500)
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
