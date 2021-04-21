import turtle
import random
from tkinter.simpledialog import *

##전역변수선언##
myturtle, tX, tY, tColor, tSize, tShape = [None]*6
shapelist = []
playerturtles = []
swidth, sheight = 500, 500

##메인코드##
if __name__ == "__main__":
    turtle.title('거북리스트활용')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)

    while True:
        inStr = askstring('문자열입력', '거북이 쓸 문자열을 입력')
        tSize = random.randrange(1, 3)

        for i in range(0, len(inStr)):
            turtle.penup()
            r = random.random();g = random.random();b = random.random()
            turtle.color(r,g,b)
            tX = random.randrange(-swidth / 2, swidth / 2)
            tY = random.randrange(-sheight / 2, sheight / 2)
            turtle.goto(tX, tY)
            size = random.randrange(10, 100, 5)
            turtle.write(inStr[i], font=('arial', size, 'normal'))

    turtle.done()