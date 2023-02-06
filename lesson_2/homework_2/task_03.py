'''3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
'''
def IntNumbers(n):
    for i in range(0, n + 1):
        result = 2**i
        if result < n:
            print(result)

IntNumbers(int(input()))