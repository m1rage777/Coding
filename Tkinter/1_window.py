#Главное окно Tkinter

import tkinter as tk

win = tk.Tk()
h = 500
w = 600
photo = tk.PhotoImage(file="snake2.png")
win.iconphoto(False, photo)
win.config(bg='LightSlateGray')# Цвет Back Ground
win.title('Python Sort List')
win.geometry(f"{500}x{600}+100+100")
win.minsize(500, 600)
win.maxsize(600, 800)
win.resizable(True, True)
win.mainloop()


