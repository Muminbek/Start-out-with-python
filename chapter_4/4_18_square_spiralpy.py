import turtle

turtle.speed(0)
side = 10

for square in range(50):
    
    turtle.forward(side) 
    turtle.left(90)
    side += 5
    
turtle.mainloop()