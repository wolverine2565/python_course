
def NumberPow(Num, Pow):
    if Pow == 0: return 1
    else:
        return NumberPow(Num, Pow - 1)*Num

print(NumberPow(int(input()), int(input())))