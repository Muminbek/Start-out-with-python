import turtle 
angle = 45


for octa in range(8):

    turtle.right(angle)
    turtle.forward(100)

turtle.penup()
turtle.left(-117)
turtle.forward(145)
turtle.write('STOP')
turtle.pendown()
turtle.hideturtle()
turtle.mainloop()
