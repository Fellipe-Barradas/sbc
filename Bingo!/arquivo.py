'''
Cartas de 0 à N em colunas e linhas
É retirado um subconjunto de bolas do globo que é possivelmente vazio, de forma que ao menos 2 bolas fiquem no globo
Primeira bola é sorteada e coloca de volta no globo
Segunda bola é sorteada e coloca de volta no globo
Após isso, é dito a diferença absoluta da subtração dessas bolas
Caller opera o globo com N + 1 bolas de 0 até N

ENTRADA
1 <= N <= 90
B NUMERO DE BOLAS QUE PERMANEÇERAM NO GLOBO

COMO PROSEGUIR
WHILE TRUE
    PEGAR N E B
    SE N E B == 0
        BREAK
    SE B > N
        PRINT(Y)
    SENAO
        PEGAR NUMEROS QUE FORAM TIRADOS
        USAR O TWO SUM PARA ENCONTRAR O VALOR BUSCADO POREM ADAPTADO PARA SUBTRAÇÃO O(N)
        PARA CADA VALOR NA LISTA B, SOMAR COM O ALVO E INSERIR EM UM DICIONARIO
        EX:
            5 0 1 3
            0 + 2 = 2
            5 + 2 = 7
            1 + 2 = 3
            3 + 2 = 5
            
        SE FOR ENCONTRADO
            PRINT(Y)
        SENAO
            PRINT(N)
'''

def two_sub(target: int, arr: set):
    sumtarget = set(map(lambda x: x + target, arr))
    return len(sumtarget.intersection(arr)) > 0 and target != 0
    

while True:
    arr = list(map(int, input().split(" ")))
    N, B = arr[0], arr[1]
    if N == 0 and B == 0:
        break
    total_bolas = set(i for i in range(N+1))
    bolas_globo = set(map(int, input().split(" ")))
    diferentes = total_bolas.difference(bolas_globo)
    if len(diferentes) == 0:
        print("Y")
    else:
        finded = "Y"
        for diference_num in diferentes:
            if not two_sub(diference_num, bolas_globo):
                finded = "N"
                break  
        print(finded)
        