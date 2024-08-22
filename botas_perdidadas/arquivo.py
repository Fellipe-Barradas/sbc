import math

while True:
    try:
        num_botas = input()
    except EOFError:
        break
    
    set_d = [0] * 31
    set_e = [0] * 31
    
    for i in range(int(num_botas)):
        row = input().split()
        M, F = int(row[0]), row[1]
        if F == "D":
            set_d[M - 30] += 1
        else:
            set_e[M - 30] += 1
    res = 0
    for i in range(31):
        if set_d[i] == 0 or set_e[i] == 0:
            continue
        res += min(set_e[i], set_d[i])
    
    
    print(res)
    