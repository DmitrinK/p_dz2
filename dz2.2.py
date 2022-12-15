"""
Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""
swap_list = list(input())
temporary_storage = None
step_count = 0
print(swap_list)
while step_count + 1 < len(swap_list):
    temporary_storage = swap_list[step_count]
    swap_list[step_count] = swap_list[step_count + 1]
    swap_list[step_count + 1] = temporary_storage
    step_count = step_count + 2
print(swap_list)
