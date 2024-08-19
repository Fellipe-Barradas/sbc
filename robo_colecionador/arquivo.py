import re

while True:
    N, M, S = list(map(int, input().split(" ")))
    if N == 0 and M == 0 and S == 0:
        break
    mapa = []
    rp = {"x": 0, "y":0, "ori":"S/N"}
    for i in range(N):
        linha = input()
        mapa.append(linha)

            
    
    def eAndavel(x, y):
        try:
            return not mapa[x][y] == "#"
        except:
            return False
    insts = input()
    resposta = 0
    direcao = rp["ori"]
    for i in range(len(insts)):
        instrucao = insts[i]
        if instrucao == "F":
            (x, y) = rp["x"], rp["y"]
            if rp['ori'] == "N" and x > 0 and eAndavel(x - 1, y):
                rp["x"] -= 1
            if rp['ori'] == "S" and x < (M - 1) and eAndavel(x + 1, y):
                rp["x"] += 1
            if rp['ori'] == "L" and y < (M - 1) and eAndavel(x, y + 1):
                rp["y"] += 1
            if rp['ori'] == "O" and y > 0 and eAndavel(x, y - 1):
                rp["y"] -= 1
        else:
            if instrucao == "D":
                if rp["ori"] == "N":
                    rp["ori"] = "L"
                elif rp["ori"] == "L":
                    rp["ori"] = "S"
                elif rp["ori"] == "O":
                    rp["ori"] = "N"
                elif rp["ori"] == "S":
                    rp["ori"] = "O"
            else:
                if rp["ori"] == "N":
                    rp["ori"] = "O"
                elif rp["ori"] == "O":
                    rp["ori"] = "S"
                elif rp["ori"] == "S":
                    rp["ori"] = "L"
                elif rp["ori"] == "L":
                    rp["ori"] = "N"
        if mapa[rp["x"]][rp["y"]] == "*":
            resposta+=1
            mapa[rp["x"]][rp["y"]] = "."
        
    print(resposta)