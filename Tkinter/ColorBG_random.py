from random import *
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def change_color():
    wnd.config(bg=_from_rgb((randint(0,255),randint(0,255),randint(0,255))))


from tkinter import *

wnd=Tk()
wnd.title('Че смотришь?')
wnd.geometry("700x700")
wnd.config(bg='orange')
btn=Button(wnd,text='Поменять цвет на случайный!!!',command=change_color)
btn.pack()

wnd.mainloop()