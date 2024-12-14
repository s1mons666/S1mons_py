#Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы
неравенства A > 0 или B < —2»
try:
    # Запрашиваем у пользователя ввод двух целых чисел
    A = int(input("Введите целое число A: "))
    B = int(input("Введите целое число B: "))
    
    # Проверяем истинность неравенств
    if A > 0 or B < -2:
        print("Высказывание истинно: A > 0 или B < -2.")
    else:
        print("Высказывание ложно: ни одно из условий не выполнено.")

except ValueError:
    print("Введите корректные целые числа.")
