from tkinter import *
from tkinter.ttk import Label
from PIL import ImageTk, Image
from itertools import count, cycle


class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None
    
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


def ftbdes1():
    n1.destroy()
    global d1
    d1 = Tk()
    d1.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d1)
    lbl1.pack()
    lbl1.load("Football-Vid.gif")
    img1 = PhotoImage(file='Football_GD.png')
    btn = Button(d1, image=img1, command=lambda: ftb_goal())
    btn.pack()
    btn.place(x=440, y=520)
    d1.mainloop()


def ftbdes2():
    n1.destroy()
    global d1
    d1 = Tk()
    d1.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d1)
    lbl1.pack()
    lbl1.load("Football-Vid.gif")
    img1 = PhotoImage(file='Football_GD.png')
    btn = Button(d1, image=img1, command=lambda: ftb_foul())
    btn.pack()
    btn.place(x=440, y=520)
    d1.mainloop()


def ftbdes3():
    n1.destroy()
    global d1
    d1 = Tk()
    d1.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d1)
    lbl1.pack()
    lbl1.load("Football-Vid.gif")
    img1 = PhotoImage(file='Football_GD.png')
    btn = Button(d1, image=img1, command=lambda: ftb_notagoal())
    btn.pack()
    btn.place(x=440, y=520)
    d1.mainloop()


def crkdes1():
    n2.destroy()
    global d2
    d2 = Tk()
    d2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d2)
    lbl1.pack()
    lbl1.load("Cricket-Vid.gif")
    img1 = PhotoImage(file='Cricket_GD.png')
    btn = Button(d2, image=img1, command=lambda: crk_out())
    btn.pack()
    btn.place(x=440, y=540)
    d2.mainloop()


def crkdes2():
    n2.destroy()
    global d2
    d2 = Tk()
    d2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d2)
    lbl1.pack()
    lbl1.load("Cricket-Vid.gif")
    img1 = PhotoImage(file='Cricket_GD.png')
    btn = Button(d2, image=img1, command=lambda: crk_notout())
    btn.pack()
    btn.place(x=440, y=540)
    d2.mainloop()


def crkdes3():
    n2.destroy()
    global d2
    d2 = Tk()
    d2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d2)
    lbl1.pack()
    lbl1.load("Cricket-Vid.gif")
    img1 = PhotoImage(file='Cricket_GD.png')
    btn = Button(d2, image=img1, command=lambda: crk_noball())
    btn.pack()
    btn.place(x=440, y=540)
    d2.mainloop()


def crkdes4():
    n2.destroy()
    global d2
    d2 = Tk()
    d2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(d2)
    lbl1.pack()
    lbl1.load("Cricket-Vid.gif")
    img1 = PhotoImage(file='Cricket_GD.png')
    btn = Button(d2, image=img1, command=lambda: crk_fair())
    btn.pack()
    btn.place(x=440, y=540)
    d2.mainloop()


def ftb_goal():
    d1.destroy()

    w1 = Tk()
    w1.geometry("1129x660+200+100")

    lbl1 = ImageLabel(w1)
    lbl1.pack()
    lbl1.load("Goal-Football1.gif")

    w1.mainloop()


def ftb_foul():
    d1.destroy()
    w1 = Tk()
    w1.geometry("1129x660+200+100")

    lbl1 = ImageLabel(w1)
    lbl1.pack()
    lbl1.load("FF.gif")

    w1.mainloop()


def ftb_notagoal():
    d1.destroy()
    w1 = Tk()
    w1.geometry("1129x660+200+100")
    lbl1 = ImageLabel(w1)
    lbl1.pack()
    lbl1.load("Not-a-Goal-Football.gif")

    w1.mainloop()


def crk_noball():
    d2.destroy()
    w2 = Tk()
    w2.geometry("1129x660+200+100")

    lbl1 = ImageLabel(w2)
    lbl1.pack()
    lbl1.load("No-Ball-Cricket.gif")

    w2.mainloop()


def crk_out():
    d2.destroy()
    w2 = Tk()
    w2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(w2)
    lbl1.pack()
    lbl1.load("Out-Cricket.gif")

    w2.mainloop()


def crk_notout():
    d2.destroy()
    w2 = Tk()
    w2.geometry("1129x660+200+100")
    lbl1 = ImageLabel(w2)
    lbl1.pack()
    lbl1.load("Not-Out-Cricket.gif")

    w2.mainloop()


def crk_fair():
    d2.destroy()
    w2 = Tk()
    w2.geometry("1129x660+200+100")

    lbl1 = ImageLabel(w2)
    lbl1.pack()
    lbl1.load("Fair-Delivery-Cricket.gif")
    w2.mainloop()


def deci(a):
    if a == 1:
        des_ftb()
    if a == 2:
        des_crk()
    if a == 3:
        des_ath()


def des_ftb():
    global n1
    n1 = Tk()
    n1.geometry("1129x660+200+100")
    canvas = Canvas(n1, width=1129, height=660)
    photo = PhotoImage(file="Give Decision.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack()
    goal = PhotoImage(file="GOAL.png")
    btn1 = Button(n1, image=goal, command=lambda: ftbdes1())
    btn1.pack()
    btn1.place(x=300, y=600)
    foul = PhotoImage(file="FOUL.png")
    btn2 = Button(n1, image=foul, command=lambda: ftbdes2())
    btn2.pack()
    btn2.place(x=500, y=600)
    not_a_goal = PhotoImage(file="NOT A GOAL.png")
    btn3 = Button(n1, image=not_a_goal, command=lambda: ftbdes3())
    btn3.pack()
    btn3.place(x=700, y=600)

    n1.mainloop()


def des_crk():
    global n2
    n2 = Tk()
    n2.geometry("1129x660+200+100")
    canvas = Canvas(n2, width=1129, height=660)
    photo = PhotoImage(file="Give Decision.png")
    image_on_canvas = canvas.create_image(0, 0, ancho=NW, image=photo)
    canvas.pack()
    out = PhotoImage(file="OUT.png")
    btn1 = Button(n2, image=out, command=lambda: crkdes1())
    btn1.pack()
    btn1.place(x=200, y=600)
    not_out = PhotoImage(file="NOT OUT.png")
    btn2 = Button(n2, image=not_out, command=lambda: crkdes2())
    btn2.pack()
    btn2.place(x=400, y=600)
    no_ball = PhotoImage(file="NO BALL.png")
    btn3 = Button(n2, image=no_ball, command=lambda: crkdes3())
    btn3.pack()
    btn3.place(x=600, y=600)
    fair = PhotoImage(file="FAIR DELIVERY.png")
    btn4 = Button(n2, image=fair, command=lambda: crkdes4())
    btn4.pack()
    btn4.place(x=800, y=600)

    n2.mainloop()


def des_ath():
    global n3
    n3 = Tk()
    n3.geometry("1129x660+200+100")
    lbl1 = ImageLabel(n3)
    lbl1.pack()
    lbl1.load("Athletics-Vid.gif")

    n3.mainloop()
