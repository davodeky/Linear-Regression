import numpy as np
from itertools import combinations 

def comb(k, p):
    x = list(range(k))
    comb = combinations(x, p)
    C = list(comb)
    return C
    

for i in range(5):
    C = []
    C = comb(5, i+1)
    print(C)
