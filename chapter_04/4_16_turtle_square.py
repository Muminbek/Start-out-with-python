import turtle

turtle.hideturtle()
angle = 90
side = 20
turtle.penup()
turtle.goto(250, -250)
turtle.pendown()
turtle.speed(0)
turtle.left(angle)

for square in range(100):
    
    for yin in range(4):
        turtle.forward(side)
        turtle.left(angle)
    
    side += 5

turtle.mainloop()
