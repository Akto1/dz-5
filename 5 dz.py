result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первое число меньше второго.")
    if b > 100:
        raise IndexError("Второе число больше 100.")
    return a / b

data = {
    10: 2,
    2: 5,
    "123": 4, 
    18: 0,  
    8: 4
}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль для ключа: {key}")
    except ValueError as e:
        print(f"Ошибка значения для ключа {key}: {e}")
    except IndexError as e:
        print(f"Ошибка индекса для ключа {key}: {e}")
    except TypeError as e:
        print(f"Ошибка типа данных для ключа {key}: {e}")

print(result)
