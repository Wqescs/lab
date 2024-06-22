opened = '{'
closed = '}'
meter1 = 0
meter2 = 0
slash = '/'

with open('Lav1.txt', 'r') as file:
    while True:
        char = file.read(1)
        # Открытая фигурная скобка, переключаем флаг
        if char == opened:
            meter1 += 1
        # Закрытая фигурная скобка, сбрасываем флаг
        elif char == closed:
            meter1 -= 1
        elif char == slash:
            meter2 += 1
        elif char == '\n' and meter2 != 0:
            meter2 -= 1

        # Не внутри фигурных скобок, выводим символ
        elif meter1 == 0 and meter2 == 0:
            print(char, end='')
        # Если конец файла, выходим из цикла
        if not char:
            break
