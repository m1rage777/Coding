#Виджет Entry()

import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0, tk.END) #полная отчистка строки
    #name.delete(1, 'end') #0 удаляем с первого числа ('end' с первого по последнее)

def submite():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)

win = tk.Tk()
win.geometry(f"500x600+100+100")
win.title('Python Sort List')
tk.Label(win,text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win,text='Пароль').grid(row=1, column=0, stick='w')
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win,text='get',command=get_entry).grid(row=2, column=0,stick='we')
tk.Button(win,text='delete',command=delete_entry).grid(row=2, column=1,stick='we')
tk.Button(win,text='submite',command=delete_entry).grid(row=3, column=0,stick='we')
tk.Button(win,text='insert',command=lambda : name.insert(0,'hello'))\
    .grid(row=2, column=2,stick='we')

win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)


win.mainloop()