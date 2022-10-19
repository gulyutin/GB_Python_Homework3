# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def input_int(msg=" "):
    while True:
        try: 
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else: 
            return result


def possitive_fibonacci(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    result = list()
    result.append(0)
    result.append(1)
    for i in range (2, n+1):
        result.append(result[i-1] + result[i-2])
    return result

def reverse_list(input_list):
    result = list()
    length = len(input_list)
    for i in range(length):
        result.append(input_list[length - i - 1])
    return result

def negative_fibonacci(n):
    if n <= 0:
        return []
    if n == 1: 
        return [1]
    if n == 2:
        return [-1,1]
    result = list()
    result.append(0)
    result.append(1)
    result.append(-1)
    for i in range(3, n+1):
        result.append(result[i-2] - result[i-1])
    result.pop(0)
    return reverse_list(result)

def full_fibonacci(n):
    return negative_fibonacci(n) + possitive_fibonacci(n)

print(full_fibonacci(input_int("Введите целое чилсло: ")))