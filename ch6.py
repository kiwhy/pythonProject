import turtle
import random

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
    shapelist = turtle.getshapes()

    for i in range(0, 100):
        random.shuffle(shapelist)
        myturtle = turtle.Turtle(shapelist[0])
        tX = random.randrange(-swidth/2, swidth/2)
        tY = random.randrange(-sheight/2, sheight/2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 3)
        playerturtles.append([myturtle, tX, tY, tSize, r, g, b])

    for tList in playerturtles:
        myturtle = tList[0]
        myturtle.color((tList[4], tList[5], tList[6]))
        myturtle.pencolor((tList[4], tList[5], tList[6]))
        myturtle.turtlesize(tList[3])
        myturtle.goto(tList[1], tList[2])

    turtle.done()