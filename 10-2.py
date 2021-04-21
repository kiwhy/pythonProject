from tkinter import *
from tkinter import messagebox

##함수선언##
def clickleft(event):
    messagebox.showinfo("마우스", "마우스왼클릭")
def clickmid(event):
    messagebox.showinfo("마우스", "휠클릭")
def clickright(event):
    messagebox.showinfo("마우스", "오른클릭")

def clickleft2(event):
    messagebox.showinfo("마우스", "마우스왼클릭release")
def clickmid2(event):
    messagebox.showinfo("마우스", "휠클릭release")
def clickright2(event):
    messagebox.showinfo("마우스", "오른클릭release")

def clickleft3(event):
    messagebox.showinfo("마우스", "마우스 더블왼클릭")
def clickmid3(event):
    messagebox.showinfo("마우스", "휠 더블클릭")
def clickright3(event):
    messagebox.showinfo("마우스", "더블오른클릭")

def clickleft4(event):
    messagebox.showinfo("마우스", "왼클릭 드래그")
def clickmid4(event):
    messagebox.showinfo("마우스", "휠 드래그")
def clickright4(event):
    messagebox.showinfo("마우스", "오른클릭 드래그")

##메인코드##
window = Tk()
window.bind("<Button-1>", clickleft)
window.bind("<Button-2>", clickmid)
window.bind("<Button-3>", clickright)
window.bind("<ButtonRelease-1>", clickleft2)
window.bind("<ButtonRelease-2>", clickmid2)
window.bind("<ButtonRelease-3>", clickright2)
window.bind("<Double-Button-1>", clickleft3)
window.bind("<Double-Button-2>", clickmid3)
window.bind("<Double-Button-3>", clickright3)
window.bind("<B1-Motion>", clickleft4)
window.bind("<B2-Motion>", clickmid4)
window.bind("<B3-Motion>", clickright4)
window.mainloop()