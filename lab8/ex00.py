import turtle
from math import *

def func(x):
	if x <= -2:
		y = -x - 2
	if x > -2 and x < -1:
		y = sqrt(1 - pow(x + 1, 2))
	if x >= -1 and x <= 1:
		y = 1
	if x > 1 and x < 2:
		y = -2 * (x - 2) - 1
	if x >= 2:
		y = -1
	return y

X_SIZE = 300
Y_SIZE = 300
AXIS_STEP = 30

pen = turtle.Turtle()
window = turtle.Screen()

def draw_axis(pen: turtle.Turtle, size, step, arrow) -> None:
	pen.speed(0)
	m = 0
	for i in range(0, size, step * int((size / abs(size)))):
		m += 1
		pen.fd(step)
		pen.lt(90)
		pen.write(" " + str(m * int((size / abs(size)))))
		pen.fd(5)
		pen.bk(10)
		pen.fd(5)
		pen.rt(90)
	pen.fd(step)
	if (arrow):
		pen.stamp()
		pen.write(arrow)
	pen.home()
	return m * int((size / abs(size)))

X_MAX = draw_axis(pen, X_SIZE, AXIS_STEP, "X")
pen.lt(180)
X_MIN = draw_axis(pen, -X_SIZE, AXIS_STEP, False)
pen.lt(90)
Y_MAX = draw_axis(pen, Y_SIZE, AXIS_STEP, "Y")
pen.lt(270)
Y_MIN = draw_axis(pen, -Y_SIZE, AXIS_STEP, False)
pen.write(" 0")

pen.penup()
pen.goto(AXIS_STEP * X_MIN, AXIS_STEP * func(X_MIN))
pen.pendown()
pen.pencolor('red')
pen.pensize(2)
x = X_MIN
while x <= X_MAX:
	y = func(x)
	pen.goto(int(x * AXIS_STEP), int(y * AXIS_STEP))
	x += 0.1

window.mainloop()