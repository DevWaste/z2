number = input("Введите пятизначное число: ")

# Разбиение числа на разряды
if len(number) == 5 and number.isdigit():
    units = int(number[-1])
    tens = int(number[-2])
    hundreds = int(number[-3])
    thousands = int(number[-4])
    tens_of_thousands = int(number[-5])

    # Выполнение вычислений
    result = (tens ** units) * hundreds / (tens_of_thousands - thousands)

    # Вывод результата
    print(f"Результат вычислений: {result}")
else:
    print("Пожалуйста, введите корректное пятизначное число.")
