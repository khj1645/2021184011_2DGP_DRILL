import turtle

count = 0
x = 0
y = 0
while count < 6:
    turtle.forward(500)
    turtle.penup()
    x = 0
    y += 100
    turtle.goto(x,y)
    turtle.pendown()
    count += 1
    
turtle.penup()
count = 0
x = 0
y = 0
turtle.goto(x,y)
turtle.left(90)
turtle.pendown()
while count < 6:
    turtle.forward(500)
    turtle.penup()
    x += 100
    y = 0
    turtle.goto(x,y)
    turtle.pendown()
    count += 1
turtle.exitonclick()
