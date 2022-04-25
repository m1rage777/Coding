n = int(input("Введите парное колличество элементов ключ : значение: "))
my_dict = {}


for i in range(n):
    key = input("Введите цвет: red, green, blue:")
    value = input("Введите значение типа строка :")
    # my_dict.update({key: value})

red_dict = {key: value for (key, value) in my_dict.items() if value == "red"}
green_dict = {key: value for (key, value) in my_dict.items() if value == "green"}
blue_dict = {key: value for (key, value) in my_dict.items() if value == "blue"}

# print(my_dict)
print(red_dict, green_dict, blue_dict)


