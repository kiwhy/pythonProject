from tkinter import *

## 변수 선언 부분 ##
btnList = [""] * 9
fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList=[None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("300x300")

for i in range(0, 9):
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos,y=yPos)
        num += 1
        xPos += 100
    xPos = 0
    yPos += 100

window.mainloop()