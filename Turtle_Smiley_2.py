import turtle
turtle.speed(20)

def draw_outline(x_pos1,y_pos1):
    turtle.penup()
    turtle.goto(x_pos1,y_pos1)
    turtle.pensize(3)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('yellow')
    turtle.circle(300)
    turtle.end_fill()

def draw_eye(x_pos2,y_pos2):
    turtle.penup()
    turtle.goto(x_pos2,y_pos2)
    turtle.pensize(3)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('white')
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x_pos2,(y_pos2+20))
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('black')
    turtle.circle(20)
    turtle.end_fill()

def draw_smile(x_pos3,y_pos3):
    turtle.penup()
    turtle.goto(x_pos3,y_pos3)
    turtle.setheading(270)
    turtle.pendown() 
    turtle.pensize(10)
    turtle.pencolor('red')
    turtle.circle(100,180)

def draw_face(x_pos,y_pos):
    draw_outline(x_pos,y_pos)
    draw_eye((x_pos-100),(y_pos+380))
    draw_eye((x_pos+100),(y_pos+380))
    draw_smile((x_pos-100),(y_pos+225))

draw_face(-300,-300)
draw_face(-300,-300)

turtle.exitonclick()
