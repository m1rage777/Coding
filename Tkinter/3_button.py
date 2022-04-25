
def say_hello():
    print("Hello litle bastard")

def add_label():
    label = tk.Label (win, text= 'new')
    label.pack()

count = 0 # счётчик равен нулю изначально

def counter():
    global count
    count+=1
    btn4['text'] = f'Счётчик: {count}'

def fstat():
    bstat = btn4['state']
    if bstat == 'normal':
        bstat = 'disabled'
    elif bstat == 'disabled':
        bstat = 'normal'
    btn1['state'] = btn2['state'] = btn3['state'] = btn4['state'] = bstat
    btn5['text'] = f'button stat {bstat}'

import tkinter as tk

win = tk.Tk()
win.geometry(f"{500}x{600}+100+100")
win.title('Python Sort List')

btn1 = tk.Button(win, text='Hello',
                 command=say_hello
                 )

btn2 = tk.Button(win, text='Add new label',
                 command=add_label
                 )

btn3 = tk.Button(win, text='Add new label lambda',
                 command=lambda: tk.Label(win, text='new lambda').pack()
                 )

btn4 = tk.Button(win, text=f'Cчётчик: {count}',
                 command=counter,
                 bg='red',
                 activebackground='blue',
                 #state=tk.DISABLED #NORMAL
                 )
btn5 = tk.Button(win, text=f'buttons is normal',
                 command=fstat
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()


win.mainloop()