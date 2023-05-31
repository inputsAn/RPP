import numpy as np
import numpy.random as rand


def matrix_input(): # ввод матрицы
    try:
        n = int(input("Введите кол-во строк в матрице: "))
        m = int(input("Введите кол-во столбцов в матрице: "))

        if n == m or n == 0 or m == 0: # квадратная матрица, либо матрица без строк или столбцов
            print("Квадратная или некорректная матрица.")
            matrix_input()
        return rand.randint(0, 10, (n, m)), n, m # генерация элементов матррицы
    except ValueError:
        print("Введено некорректное значение")
        matrix_input()


def zero_search(matrix, n, m): # поиск нулей
    try:
        l = int(input("Введите кол-во верхних строк в матрице, в которых будем искать нулевые элементы: "))
        k = int(input("Введите кол-во левых столбцов в матрице, в которых будем искать нулевые элементы: "))

        if (l > n or k > m) or (l == 0 or k == 0):
            print("Одно из введеных значений l или k превышают размер матрицы или равны 0")
            zero_search(matrix, n, m)
        zero_counter = 0 # счетчик нулей
        for i in range(l): # поиск по строкам
            for j in range(k): # поиск по столбцам
                if matrix[i][j] == 0:
                    zero_counter += 1
        return zero_counter
    except ValueError:
        print("Введено некорректное значение")
        zero_search(matrix, n, m)


if __name__ == '__main__':
    matrix, n, m = matrix_input() # матрица
    print(f"Матрица:\n {matrix}")
    ans = zero_search(matrix, n, m) # результат
    print(f"Кол-во нулевых элементов в матрице {ans}")
    f = open("output.txt", "w+")  # открывание (или создание) файла для записи
    try:
        f.write(f"Матрица:\n {matrix}\n")  # запись результатов
        f.write(f"Кол-во нулевых элементов в матрице: {ans}")
    finally:  # нужен для срабатывания f.close() при любом типе исключений
        f.close()
