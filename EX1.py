# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def input_int(msg=" "):
    while True:
        try: 
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else: 
            return result


def input_int_list():
    count = input_int("Введите количество элементов списка: ")
    result = []
    for i in range(count):
        result.append(input_int(f"Введите целое число №{i+1}: "))
    return result


def sum_of_odd(number_list):
    result = 0
    for i in range(len(number_list)):
        if i % 2 == 0:
            result += number_list[i]
    return result

print(sum_of_odd(input_int_list()))