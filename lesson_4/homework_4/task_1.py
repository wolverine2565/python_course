'''1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств'''


'''def array_merge(n, m, ar1, ar2):
    arr1 = list(ar1.split())
    arr2 = list(ar2.split())
    arr3 = []
    if len(arr1) == int(n) and len(arr2) == int(m):
        for i in (str(arr1)+str(arr2)):
            if i in arr1 and i in arr2:
                arr3.append(i)
        return set(array_sort(arr3))

def array_sort(set_array):
    array = list(set_array)
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return array_sort(less) + [pivot] + array_sort(greater)

print(array_merge(input(), input(), input(), input()))
'''
n, m = input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))
