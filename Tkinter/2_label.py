#Виджеты. Label

import tkinter as tk

win = tk.Tk()
win.geometry(f"{500}x{600}+100+100")
win.title('Python Sort List')

label_1 = tk.Label(win,text='''Hello!!!
world!!!''',
                   bg="red",
                   fg="white",
                   font=('Arial',15,'bold'),
                   padx=20, # отступ по х
                   pady=40, # отступ по y
                   width=20,
                   height=10,
                   anchor='sw', # Прикрепляем текс по сторонам (n, ne, e, se, s,sw, w, nw, o, center)
                   #relief=tk.RAISED,
                   #bd=10,
                   #justify=tk.LEFT
                   )
label_1.pack()

win.mainloop()