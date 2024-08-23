from dataclasses import dataclass
from typing import List

@dataclass
class Racional():
    x:int
    y:int

def mdc(y1:int, y2:int)->int:
    if y1 % y2 == 0:
        if y2 < 0:
            return y2 * -1
        return y2
    return mdc(y2,y1%y2)


def soma(rac1: Racional, rac2: Racional) -> Racional:
    rac1.x *=  rac2.y
    rac2.x *= rac1.y
    return Racional(rac1.x + rac2.x, rac1.y * rac2.y)

def subt(rac1: Racional, rac2: Racional) -> Racional:
    rac1.x *=  rac2.y
    rac2.x *= rac1.y
    return Racional(rac1.x - rac2.x, rac1.y * rac2.y)

def mult(rac1: Racional, rac2: Racional) -> Racional:
    return Racional(rac1.x * rac2.x, rac1.y * rac2.y)

def divs(rac1: Racional, rac2: Racional) -> Racional:
    inverse_rac2: Racional = Racional(rac2.y, rac2.x)
    return mult(rac1, inverse_rac2)

N: int = int(input())

for i in range(N):
    statement: List[str] = input().split(" ") 
    rac1 = Racional(0,0)
    rac2 = Racional(0,0)
    op = statement[3]
    rac1.x = int(statement[0])
    rac1.y = int(statement[2])
    rac2.x = int(statement[4])
    rac2.y = int(statement[6])
    res = None
    if op == "+":
        res = soma(rac1, rac2)
    elif op == "-":
        res = subt(rac1, rac2)
    elif op == "/":
        res = divs(rac1, rac2)
    elif op == "*":
        res = mult(rac1, rac2)
        
    min_den = mdc(max(res.x, res.y), min(res.x, res.y))
    print(f"{res.x}/{res.y} = ", end="")
    res.x /= min_den
    res.y /= min_den
    print(f"{int(res.x)}/{int(res.y)}")
    