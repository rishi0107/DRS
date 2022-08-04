from tkinter import *
from tkinter.ttk import Label
import cv2 # pip install opencv-python
import PIL.Image, PIL.ImageTk # pip install pillow
from functools import partial
import threading
import time
import imutils # pip install imutils
from choose_file import *
from tkinter import filedialog

def slt_ftb_can():
    nx2.destroy()
    sel_ur_sprt()

def slt_ath_can():
    nx4.destroy()
    sel_ur_sprt()

def slt_crk_can():
    nx3.destroy()
    sel_ur_sprt()

def ftb_drs1():
    file=filedialog.askopenfilename()
    if file=="":
        slt_ftb_can()
    else:
        nx2.destroy()
        ftb_drs(file)



def crk_drs1():
    file=filedialog.askopenfilename()
    if file=="":
        slt_crk_can()
    else:
        nx3.destroy()
        crk_drs(file)


def ath_drs1():
    file=filedialog.askopenfilename()
    if file=="":
        slt_ath_can()
    else:
        nx4.destroy()
        ath_drs(file)

def slt_ftb():
    nx1.destroy()
    def back():
        nx2.destroy()
        sel_ur_sprt()
    
    global nx2
    nx2=Tk()
    
    nx2.geometry("1129x660+200+100")
    nx2.maxsize(1129,660)
    nx2.minsize(1129,660)

    canvas = Canvas(nx2, width=1129, height=660)
    photo = PIL.ImageTk.PhotoImage(file="5.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack()
     


    sbm=PhotoImage(file="Football_Upload.png") 
    btn = Button(nx2, image=sbm,bg="#5f3a6f",fg="white",command=ftb_drs1)
    btn.pack()
    btn.place(x=850,y=600)

    bck=PhotoImage(file="Football_Back-2.png") 
    btn = Button(nx2, image=bck,bg="#5f3a6f",fg="white",command=back)
    btn.pack()
    btn.place(x=150,y=600)

    

    nx2.mainloop()
    

def slt_crk():
    nx1.destroy()
    def back():
        nx3.destroy()
        sel_ur_sprt()
    global nx3
    
    nx3=Tk()
    
    nx3.geometry("1129x660+200+100")
    nx3.maxsize(1129,660)
    nx3.minsize(1129,660)
    

    canvas = Canvas(nx3, width=1129, height=660)
    photo = PIL.ImageTk.PhotoImage(file="10.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack()
    
    sbm=PhotoImage(file="Cricket_Upload.png")
    btn = Button(nx3, image=sbm,bg="#5f3a6f",fg="white",command=crk_drs1)
    btn.pack()
    btn.place(x=850,y=600)
    
    bck=PhotoImage(file="Cricket_Back-2.png") 
    btn = Button(nx3, image=bck,bg="#5f3a6f",fg="white",command=back)
    btn.pack()
    btn.place(x=150,y=600)

    nx3.mainloop()



def slt_Ath():
    nx1.destroy()
    def back():
        nx4.destroy()
        sel_ur_sprt()
    
    global nx4
    nx4=Tk()
    
    nx4.geometry("1129x660+200+100")
    nx4.maxsize(1129,660)
    nx4.minsize(1129,660)

    
    canvas = Canvas(nx4, width=1129, height=660)
    photo = PIL.ImageTk.PhotoImage(file="3.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack()
    
    global filename
    
    sbm=PhotoImage(file="Athletics_Upload.png")
    btn = Button(nx4, image=sbm,bg="#5f3a6f",fg="white",command=ath_drs1)
    btn.pack()
    btn.place(x=850,y=600)
    
    bck=PhotoImage(file="Athletics_Back-2.png") 
    btn = Button(nx4, image=bck,bg="#5f3a6f",fg="white",command=back)
    btn.pack()
    btn.place(x=150,y=600)

    nx4.mainloop()






def sel_ur_sprt():
    global nx1
    nx1=Tk()
    nx1.title("Select Your Sport")
    nx1.geometry("1129x660+200+100")
    nx1.maxsize(1129,660)
    nx1.minsize(1129,660)

    canvas = Canvas(nx1, width=1129, height=660)
    photo = PIL.ImageTk.PhotoImage(file="2.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack(fill="both",expand=True)



   
    
    ftb_img=PIL.ImageTk.PhotoImage(file="Football_Button.png")
    btn = Button(nx1, image=ftb_img,bg="#000000",command=slt_ftb,border=5)
    btn.pack()
    btn.place(x=165,y=550)

    crk_img=PIL.ImageTk.PhotoImage(file="Cricket_Button.png")
    btn = Button(nx1, image=crk_img,bg="#000000",command=slt_crk,border=5)
    btn.pack()
    btn.place(x=470,y=550)

    ath_img=PhotoImage(file='Athletics_Button.png')
    btn = Button(nx1, image=ath_img,command=slt_Ath,bg="#000000",border=5)
    btn.pack()
    btn.place(x=775,y=550)
    



    nx1.mainloop()