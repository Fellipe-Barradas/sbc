from collections import deque

N = int(input())
for i in range(N):
    fila = deque()
    strs = input()
    res = 0
    for letter in strs:
        if letter == "<":
            fila.append(letter)
        elif letter == ">" and len(fila) > 0:
            fila.pop()
            res+=1
    print(res)
            