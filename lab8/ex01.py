import turtle
from math import *
from random import *

def shot(r, x, y):
	if x >= 0 and y >= 0 and sqrt(x*x + y*y) <= r:
		return [x, y, 1]
	elif x <= 0 and y <= 0 and -x - r <= y:
		return [x, y, 1]
	else:
		return [x, y, 0]

X_SIZE = 300
Y_SIZE = 300
AXIS_STEP = 100

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
r = min(Y_MAX, X_MAX)
print(r)
for i in range(10000):
	print(i)
	x, y, res = shot(r, uniform(-r, r), uniform(-r, r))
	pen.goto(x * AXIS_STEP, y * AXIS_STEP)
	if res == 1:
		pen.dot(4, "#227800")
	else:
		pen.dot(4, "#ff6b6b")


pen.goto(0, 0)
pen.down()
X_MAX = draw_axis(pen, X_SIZE, AXIS_STEP, "X")
pen.lt(180)
X_MIN = draw_axis(pen, -X_SIZE, AXIS_STEP, False)
pen.lt(90)
Y_MAX = draw_axis(pen, Y_SIZE, AXIS_STEP, "Y")
pen.lt(270)
Y_MIN = draw_axis(pen, -Y_SIZE, AXIS_STEP, False)
pen.write(" 0")

window.mainloop()