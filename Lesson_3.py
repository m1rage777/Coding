age = 25 # Инициализация переменной типа integer
print("Возраст: " + str(age)) # Вывод переменной age после преобразования в тип str
print("Возраст:", age)  # Вывод переменной age

temp = 5.9 # Инициализация переменной типа float
print("Температура:", temp, "градусов") # Вывод переменной temp

username = "M1rage" #Инициализация переменной string
print("Имя пользователя", username); print("Имя пользователя", username) #Вывод переменной usernam дважды

isexists = True  #Инициализация переменной типа boolean
print("Существует:", isexists) #Вывод переменной isexists
isexists = False # Изменение значения переменной isexists
print("Существует:", isexists) #Вывод переменной isexists

age = "18.5" #Изменение значения и типа переменной age
print("Возраст: " + age) #Вывод переменной age

print("Тип переменной age: ", type(age))
print("Тип переменной temp: ", type(temp))
print("Тип переменной isexists: ", type(isexists))
print("Тип переменной integer: ", type(10))

"""
Выводим типы переменных
с помощью функции print и type
"""
#Создание многострочного значения строковой переменной
text = '''Первая строка
Вторая строка
Третья строка'''

print(text) #Вывод переменной text (Не работает эта фигня на версии 3.10)