#DECISION REVIEW SYSTEM

from tkinter import *
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow


import imutils # pip install imutils
from sel_ur_sprt_main import *


#select ur sport
def sel_ur_sprt1():
    window.destroy()
    sel_ur_sprt()


# Width and height of our main screen
SET_WIDTH = 1129
SET_HEIGHT =660


# Tkinter gui starts here
window = Tk()
window.geometry("1129x660+200+100")
window.title("MINI PROJECT(GRP 1):DECISION REVIEW TOOL KIT")

canvas = Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PhotoImage(file="1.png")
image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
canvas.pack()


next_btn = PhotoImage(file="Next.png")

exit1 = PhotoImage(file="exit.png")


btn = Button(window, image=next_btn,fg="yellow",bg="#000000",command=sel_ur_sprt1)
btn.pack(padx=20)
btn.place(x=920,y=627)


btn = Button(window, image=exit1,bg="#000000",fg="yellow",command=exit)
btn.pack(padx=20)
btn.place(x=140,y=627)


window.mainloop()