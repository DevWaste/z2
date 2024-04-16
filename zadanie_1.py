# Ввод длины и ширины прямоугольника
length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

# Расчёт площади и периметра
area = length * width
perimeter = 2 * (length + width)

# Вывод результатов
print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")
