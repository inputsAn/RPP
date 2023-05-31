import random
import sys

A = []
B = []

check_method = int(input("Введите 0 для реализации алгоритма с использованием стандартных функций или 1 без них: "))
check = int(input("Введите 0 для ручного или 1 для автоматического заполнения списка: "))


def manual_fillingA():  # функция ручной генерации списка с использованием стандартных функций (append)
    count_elem1 = int(input("Введите количество элементов списка А: "))

    for i in range(count_elem1):
        A.append(int(input()))
    print(A)
    A.append(999)


def manual_fillingB():
    count_elem2 = int(input("Введите количество элементов списка B: "))

    for i in range(count_elem2):
        B.append(int(input()))
    print(B)
    B.append(999)


def manual_filling_wo_func1(A):  # функция ручной генерации списка без использования стандартных функций
    count_elem = int(input("Введите количество элементов списка A: "))
    for i in range(0, count_elem):
        A += [int(input())]
    print(A)
    A += [int(999)]


def manual_filling_wo_func2(B):
    count_elem = int(input("Введите количество элементов списка B: "))
    for i in range(0, count_elem):
        B += [int(input())]
    print(B)
    B += [int(999)]


def random_a(): # функция автоматической генерации списка с использованием стандартных функций (append)
    A = [random.randint(0, 10) for i in range(random.randint(5, 20))]
    print(A)
    A.append(999)


def random_b():
    B = [random.randint(0, 10) for i in range(random.randint(5, 20))]
    print(B)
    B.append(999)

def random_a_wo_func(A): # функция автоматической генерации списка без стандартных функций
    A = [random.randint(0, 10) for i in range(random.randint(5, 20))]
    print(A)
    A += [int(999)]


def random_b_wo_func(B):
    B = [random.randint(0, 10) for i in range(random.randint(5, 20))]
    print(B)
    B += [int(999)]



min_row_id = 0


def main_func():  # главная функция в которой происходит обработка списка
    # Находим самую длинную цепочку в списке A
    longest_chain_A, index_A = [], 0
    for i in range(len(A)):
        chain = [A[i]]
        j = i + 1
        while j < len(A) and A[j] == chain[-1]:
            chain.append(A[j])
            j += 1
        if len(chain) > len(longest_chain_A):
            longest_chain_A = chain
            index_A = i

    # Находим самую длинную цепочку в списке B
    longest_chain_B, index_B = [], 0
    for i in range(len(B)):
        chain = [B[i]]
        j = i + 1
        while j < len(B) and B[j] == chain[-1]:
            chain.append(B[j])
            j += 1
        if len(chain) > len(longest_chain_B):
            longest_chain_B = chain
            index_B = i

    # Обмениваем цепочки между списками
    A[index_A:index_A + len(longest_chain_A)] = longest_chain_B
    B[index_B:index_B + len(longest_chain_B)] = longest_chain_A

    print("A после обмена:", A)
    print("B после обмена:", B)


def with_func(A, B):  # определение метода генерации списка
    if check == 0:
        if check_method == 0:
            manual_fillingA()
            manual_fillingB()
            main_func()
        elif check_method == 1:
            manual_filling_wo_func1(A)
            manual_filling_wo_func2(B)
            main_func()

    elif check == 1:
        if check_method == 0:
            random_a()
            random_b()
            # main_func()
        elif check_method == 1:
            random_a_wo_func(A)
            random_b_wo_func(B)
        main_func()
    else:
        print("Ошибка ввода")
        sys.exit()


# определение метода (с использованием стандартных функций или без)
if check_method == 0:
    with_func(A, B)
elif check_method == 1:
    with_func(A, B)
else:
    print("Введите только 0 или 1")
