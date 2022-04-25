from tkinter import *
from tkinter import messagebox

#window settings
root = Tk()

root.resizable( width= False, height= False )
root.geometry('300x240')
root.title('Window name')
#root.wm_atributes( 'alpha', 0.9)
root['bg'] = '#ccc'

#Function
def check(event):
    L = login.get()
    P = password.get()

    if L and P:
        messagebox.showinfo('Success', 'Вы успешно вошли!')
    if not L and P:
        messagebox.showerror('Error 0x1', 'Введите логин!')
    elif not P and L:
        messagebox.showerror('Error 0x2', 'Введите пароль!')
    if not L and not P:
        messagebox.showerror('Error 1x1', 'Введите данные!')




#Event
text_login = Label( text= 'Login', font= 'Comfortaa 20',
                    fg='#3d3d42',
                    bg='#ccc',)

login = Entry(root, font = 'Consolas 15',
              fg='#eff5c9',
              bg='#48494f',
              justify='center')

text_password = Label(text='Password', font = 'Comfortaa 20',
                    fg='#3d3d42',
                    bg='#ccc',)

password = Entry(root, font = 'Consolas 15',
              fg = '#eff5c9',
              bg = '#48494f',
              justify = 'center',
                show= '*')

check_status = Checkbutton(text='Оставаться в системе!',
                           font='Comfortaa 13',
                           bg='#ccc',
                           fg='#3d3d42',
                           activebackground='#ccc',
                           activeforeground='#3d3d42')

enter = Button(text='Войти', font= 'Consolas 13',
                bg='#ccc',
                fg='#3d3d42',
                activebackground='#eff5c9',
                activeforeground='#6e6f73',
                width='22')
                #command= check)






#Packer
text_login.pack()
login.pack()

text_password.pack()
password.pack()

check_status.pack()
enter.pack()



#Bind
enter.bind( '<Button-1>', check)


root.mainloop()