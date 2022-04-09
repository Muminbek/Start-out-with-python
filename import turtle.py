import turtle
turtle.setup(600, 600)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.goto(200, 100)
turtle.goto(200, 200)
turtle.goto(100, 200)
turtle.goto(100, 100)

turtle.goto (150, 150)
if  turtle.xcor() >= 100 and turtle.xcor() <= 200 and\
    turtle.ycor() >= 100 and turtle.ycor() <= 200:
        turtle.pencolor('red')
        turtle.bgcolor("blue")
        
        

turtle.done()