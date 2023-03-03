from time import time
start = time()
a = list(map(int, input("Введите первый массив:").split()))
count = 0
for i in range(1, len(a)-1):
    print(a[i-1:i+2])
    if a[i] == max(a[i-1:i+2]):
        count += 1
print(count)
print(time()-start)