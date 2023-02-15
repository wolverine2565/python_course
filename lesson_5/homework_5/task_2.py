def num_summ(a,b):
    if b == 0: return a
    return num_summ(a + 1, b - 1)

print(num_summ(int(input()), int(input())))