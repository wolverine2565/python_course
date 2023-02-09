'''1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X'''

def list_nums(n, nums, x):
    count = 0
    nums_array = [char for char in str(nums)]
    
    if len(nums_array) == n:
       for i in nums_array:
            if str(i) == str(x):
                
                count += 1
    
    return(count)

    

        

    

print(list_nums(5, 12345, 3))
