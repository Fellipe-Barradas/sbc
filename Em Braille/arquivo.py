tradutor = {1: {1}, 2: {1, 3}, 3: {1,2}, 4: {1,2,4}, 5:{1, 4}, 6: {1, 2, 3}, 7:{1, 2, 3, 4}, 8: {1, 3, 4},9:{2, 3}, 0: {2, 3, 4}}
while True:
    D = int(input())
    if D == 0:
        break
    t = input()
    if t == "S":
        number = input()
        row1 = ""
        row2 = ""
        row3 = ""
        for i in range(D):
            digit = int(number[i])
            brl = tradutor[digit]
            for i in range(1,7):
                value = "*" if i in brl else "."
                if i <= 2:
                    row1 += value
                elif i <= 4:
                    row2 += value
                elif i <= 6:
                    row3 += value
            row1+= " "
            row2+= " "
            row3+= " "
        print(row1.strip())
        print(row2.strip())
        print(row3.strip())
    else:
        row1 = input().split(" ")
        row2 = input().split(" ")
        row3 = input().split(" ")
        text = ""
        for i in range(D):
            r1 = row1[i]
            r2 = row2[i]
            r3 = row3[i]
            brl = r1 + r2 + r3
            c: set = set()
            
            for i in range(1,7):
                if brl[i-1] == "*":
                    c.add(i)
            for k, value in tradutor.items():
                if c == value:
                    text += str(k)
                    break
        print(text)