# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def input_int(msg=" "):
    while True:
        try: 
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else: 
            return result


def decimal_to_bin(number):
    buffer = number
    result = " "
    while buffer > 0:
        result = str(buffer % 2) + result
        buffer //= 2
    return result

print(decimal_to_bin(input_int("Введите целое число: "))) 