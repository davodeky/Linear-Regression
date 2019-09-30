import numpy as np
from itertools import combinations 

def comb(k, p):
    x = list(range(k))
    comb = combinations(x, p)
    C = list(comb)
    return C
    
m = 1
for i in range(4):
    C = comb(4,i+1)
    for j in range(len(C)):
        print("Sweep #"+str(m)+": ")
        print("[",end='')
        for l in range(len(C[j])-1):
            print("B"+str(C[j][l] + 1)+", ",  end='')
        print("B"+str(C[j][-1] + 1),  end='')
        print("]  ----> ")
        print()
        m = m + 1

    
