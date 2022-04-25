from tkinter import *

#Window settings
root = Tk()

root.resizable(width=False, height=False)
root.geometry('333x222')
root.title('Window name')

root['bg']='#ccc'

def conn():
    UT = user_text.get()

    field.insert(0.0, f'{ UT } \n')


#Event
user_text = Entry(root, font='Consolas', bg='white', width=33, relief='solid')

btn = Button(text='Напечатать', bg='silver',relief='solid',command = conn)
global field
field = Text(root, width=33, height=10, wrap=WORD, font='Consolas',relief='solid', bg='silver')


user_text.pack( pady= 5)
btn.pack( pady= 5)
field.pack( pady= 5)

root.mainloop()
