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
        busca = re.search("[A-Z]", linha);
        if busca:
            rp["x"] = i
            rp["y"] = busca.start()
            rp['ori'] = busca.group()

            
    
    def eAndavel(x, y):
        if (x < 0 or x >= N) or (y < 0 or y >= M):
            return False
        return not mapa[x][y] == "#"
        
    insts = input()
    resposta = 0
    direcao = rp["ori"]
    
    rotacao_direita = {"N": "L", "L":"S", "S":"O", "O":"N"}
    rotacao_esquerda = {"N": "O", "L":"N", "S":"L", "O":"S"}
    finded_flags = set()
    
    for i in range(len(insts)):
        (x, y) = rp["x"], rp["y"]
        instrucao = insts[i]
        if instrucao == "F":
            
            if direcao == "N" and x > 0 and eAndavel(x - 1, y):
                rp["x"] -= 1
            if direcao == "S" and x < (M - 1) and eAndavel(x + 1, y):
                rp["x"] += 1
            if direcao == "L" and y < (M - 1) and eAndavel(x, y + 1):
                rp["y"] += 1
            if direcao == "O" and y > 0 and eAndavel(x, y - 1):
                rp["y"] -= 1
        else:
            if instrucao == "D":
                direcao = rotacao_direita[direcao]
            else:
                direcao = rotacao_esquerda[direcao]
        if mapa[rp["x"]][rp["y"]] == "*":
            tupla = (rp["x"], rp["y"])
            if tupla not in finded_flags:
                finded_flags.add((rp["x"], rp["y"]))
                resposta+=1
        
    print(resposta)