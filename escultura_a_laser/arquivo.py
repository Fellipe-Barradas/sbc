while True:
    A, C = list(map(int,input().split(" ")))
    if A == 0:
        break
    blocks = list(map(int,input().split(" ")))
    res = 0
    for i in range(C):
        if i == 0:
            res += A - blocks[0]
        else:
            if blocks[i-1] > blocks[i]:
                res+=blocks[i-1] - blocks[i]
    print(res)
    
    