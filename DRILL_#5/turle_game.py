import turtle
      
def turtle_move_up():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
def turtle_move_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
def turtle_move_down():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)     
def turtle_move_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

turtle.shape("turtle")

turtle.onkey(turtle.reset,'Escape')
turtle.onkey(turtle_move_up,'w')
turtle.onkey(turtle_move_left,'a')
turtle.onkey(turtle_move_down,'s')
turtle.onkey(turtle_move_right,'d')
turtle.listen()
