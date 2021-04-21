from turtlemodule import *
import turtle

##전역변수##
str1 = ''
swidth, sheight = 500, 500
tx, ty, tangle, tsize = [0, 0, 0, 0]

##메인코드##
turtle.title('거북이')
turtle.setup(width = swidth+50, height = sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(20)
str1 = getstring()

for i in str1:
    tx, ty, tangle, tsize = getxyas(swidth, sheight)
    r, g, b = getrgb()
    turtle.goto(tx, ty)
    turtle.left(tangle)
    turtle.pencolor(r, g, b)
    turtle.write(i, font=('arial', tsize, 'normal'))

turtle.done()