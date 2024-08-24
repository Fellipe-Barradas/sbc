from collections import deque
while True:
    try:
        rnaa = input()
    except EOFError:
        break
    combination = {"B":"S","C":"F","S":"B","F":"C"}
    d = deque()
    res = 0
    for letter in rnaa.strip():
        if len(d) == 0:
            d.append(letter)
        elif d[-1] ==  combination[letter]:
            d.pop()
            res+=1
        else:
            d.append(letter)
    print(res)
            