from collections import deque
while True:
    N = int(input())
    if N == 0:
        break
    f = deque([i for i in range(N, 0,-1)])
    descartadas = []
    while len(f) >= 2:
        descartadas.append(str(f.pop()))
        f.appendleft(f.pop())
        
    joined = ", ".join(descartadas)
    print("Discarded cards:", joined)
    print("Remaining card:", f.pop())
    
    