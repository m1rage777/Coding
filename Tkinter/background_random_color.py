from tkinter import *
import random
a= f"#{random.randrange(0x1000000):06x}"
def change_bg():
    a=f"#{random.randrange(0x1000000):06x}"
    w['bg']=a

w = Tk()
button1 = Button(text="hello",command=change_bg)
w.geometry("500x500+700+210")
button1.pack()

w.mainloop()