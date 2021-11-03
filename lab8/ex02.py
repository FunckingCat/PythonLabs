import turtle
from math import *
from random import *

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

X_SIZE = 300
Y_SIZE = 300
AXIS_STEP = 100

pen = turtle.Turtle()
window = turtle.Screen()

try:
	xs = float(window.textinput("Value input", "Input x start"))
	xe = float(window.textinput("Value input", "Input x end"))
	st = float(window.textinput("Value input", "Input dx"))
	es = float(window.textinput("Value input", "Input eps"))
except:
	exit()

X_MAX = draw_axis(pen, X_SIZE, AXIS_STEP, "X")
pen.lt(180)
X_MIN = draw_axis(pen, -X_SIZE, AXIS_STEP, False)
pen.lt(90)
Y_MAX = draw_axis(pen, Y_SIZE, AXIS_STEP, "Y")
pen.lt(270)
Y_MIN = draw_axis(pen, -Y_SIZE, AXIS_STEP, False)
pen.write(" 0")

pen.up()
pen.hideturtle()

while xs <= xe:
	if xs > -1 and xs < 1:
		xs += st
		pen.up()
		continue
	y = 0
	n = 1
	m = 0
	while True:
		de = 1 / (n * xs ** n)
		y += de
		n += 2
		m += 1
		if abs(de) < es:
			break
	pen.goto(xs * AXIS_STEP, y * AXIS_STEP)
	pen.down()
	pen.dot(4, "#227800")
	xs += st

window.mainloop()