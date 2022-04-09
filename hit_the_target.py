from traceback import print_tb
import turtle

# Именованные константы
SCREEN_WIDH = 600
SCREEN_HEIGHT = 600
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WITH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
EAST = 0
WEST = 180
SOUTH = 270

#Настроить окно.
turtle.setup(SCREEN_WIDH, SCREEN_HEIGHT)

# Нарисовать цель
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WITH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WITH)
turtle.setheading(WEST)
turtle.forward(TARGET_WITH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WITH)
turtle.penup()

# Центрировать черепаху
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Получить угол и силу от пользователя
angle = float(input("Bвeдитe угол снаряда: "))
force = float(input("Bвeдитe пусковую силу (1-10): "))

# Рассчитать расстояние.
distance = force * FORCE_FACTOR

# Задать направление.
turtle.setheading(angle)

#Запустить снаряд.
turtle.pendown()
turtle.forward(distance)

# Снаряд поразил цель?
if (turtle.xcor() >=TARGET_LEFT_X and
    turtle.xcor() <= (TARGET_LEFT_X + TARGET_WITH) and
    turtle.ycor() >= TARGET_LEFT_Y and
    turtle.ycor() <= (TARGET_LEFT_Y + TARGET_WITH)):
        print('Цель поражена!')
else:
    print('Вы промахнулись.')
    
turtle.done()
