try:
    a = float("abc")
except ValueError:
    print("Невозможно привести к числу!")

while True:
    a = input("Введите положительное число: ")
    try:
        a = float(a)
        if a <= 0:
            raise Exception("Число не положительное!")
    except ValueError:
        print("Невозможно привести к числу!")
    except Exception as exp:
        print(exp)
    else:
        print("Спасибо за корректный ввод!")
    finally:
        print("В любом случае, завершаем программу...")
        exit(0)