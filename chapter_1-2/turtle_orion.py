# Эта программа наносит звезды созвездия Ориона,
# названия звезд и линии созвездия.
import turtle

 # Задать размер окна.
turtle.setup(500, 600)

 # Установить черепаху.
turtle.penup()
turtle.hideturtle()

 # Создать именованные константы для звездных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELLSTAR_X = -40
LEFT_BELLSTAR_Y = -20

MIDDLE_BELLSTAR_X = 0
MIDDLE_BELLSTAR_Y = 0

RIGHT_BELLSTAR_X = 40
RIGHT_BELLSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

 # Нанести звезды.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()

 # Вывести названия звезд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Бeтeльгeйзe')
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.write('Хатиса')
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.write('Aпьнитaк')
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.write('Aпьнилaм')
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Pигeль')

 # Нанесение линии между звёзд
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.penup()


turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.penup()


turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.penup()

turtle.goto(MIDDLE_BELLSTAR_X, MIDDLE_BELLSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELLSTAR_X, LEFT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

turtle.goto(RIGHT_BELLSTAR_X, RIGHT_BELLSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

turtle.done()
