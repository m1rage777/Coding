# b1 = True
# b2 = False
# print("b1=", b1)
# print("b2=", b2)
#
# b3 = b1 or b2
# print("b1 or b2 =", b3)
#
# print("b1 or b2", b1 or b2)
# print("b1 and b2", b1 and b2)
# print("not b1 =", not b1)
# print("b1 != b2 =", b1 != b2) #Исключающая или не равно
# print("b1 == b2 =", b1 == b2) #Проверка на равенство
#
# print("------------")
#
# x = 5
# y = 7
# print("x =", x)
# print("y =", y)
# print("x > y =", x > y)
# print("x < y =", x < y)
# print("x <= y =", x <= y) #Меньше или равно
# print("x >= y =", x >= y) #Больше или равно
# print("7 < 7 =", 7 < 7) #7 не может быть меньше или больше 7 (False)
# print("7 <= 7 =", 7 <= 7) #7 может быть равно 7 (True) меньше или равно, больше или равно
#
# print("x and b1 or (x > 10) =", x and b1 or (x > 10))
# print("x > 10 or y < 7 =", x > 10 or y < 7)
# print("x > 10 or y <= 7 =", x > 10 or y <= 7)


x = True
y = False
print(x and (x or (y and x or y) and x or x != y))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))