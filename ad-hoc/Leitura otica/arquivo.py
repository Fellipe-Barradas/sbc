while True:
    n = int(input())
    if n == 0:
        break
    
    letters = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
    for i in range(n):
        res = list(map(int, input().split(" ")))
        marked = list(filter(lambda x: x <= 127, res))
        if len(marked) == 1:
            index = res.index(marked[0])
            print(letters[index])
        else:
            print("*")
            

        
            