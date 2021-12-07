import turtle
turtle.speed(20)



def draw_outline(x_pos,y_pos):
    turtle.penup()
    turtle.goto(x_pos,y_pos)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('yellow')
    turtle.circle(300)
    turtle.end_fill()

def draw_eye(x_pos,y_pos):
    turtle.penup()
    turtle.goto(x_pos,y_pos)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('white')
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x_pos,(y_pos+20))
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.circle(20)
    turtle.end_fill()

def draw_smile(x_pos,y_pos):
    turtle.penup()
    turtle.goto(x_pos,y_pos)
    turtle.setheading(270)
    turtle.pendown() 
    turtle.pensize(10)
    turtle.pencolor('red')
    turtle.circle(100,180)

turtle.pensize(3)

draw_outline(0,-200)

draw_eye(-100,180)
draw_eye(100,180)

draw_smile(-100,25)


turtle.exitonclick()
