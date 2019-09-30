import numpy as np
import pandas as pd
from itertools import combinations 

stop = True

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
            
            
def comb(k, p):
    x = list(range(k))
    comb = combinations(x, p)
    C = list(comb)
    return C
    

def Adjust(A):
    rows = len(A)
    cols = np.shape(A)[1]
    pivot = 0;
    for k in range(rows):
        D = A[pivot][pivot]
        print("Sweep is :", k)
        print("D is :", D)
        for i in range(rows):
            B = A[i][pivot]
            for j in range(cols):
                if(i == pivot):
                    A[i][j] = A[i][j]/D
                    print(A[i][j])
                else:
                    if(j == pivot):
                        A[i][j] = -B/D
                    else:
                        A[i][j] = A[i][j] - B*A[pivot][j]
        A[pivot][pivot] = 1/D;
        pivot = pivot + 1     
        print("Sweep #", k)
        print()
        print(A)


XM = []

while(stop):

    N = int(input("Enter the number of variables:"))

    if(yes_or_no("Did you mean " + str(N) + " variables?")):
       stop = False
    else:
        stop = True


stop = True

while(stop):

    P = int(input("Enter the number of observations:"))

    if(yes_or_no("Did you mean " + str(P) + " Observations?")):
        stop = False
    else:
        stop = True
        

  
for i in range(N):
    globals()['X' + str(i + 1)] = []
    print("Independent Variable #" + str(i + 1))
    for j in range(P):
        print("Observation " + str(j + 1) +" for Independent Variable #" + str(i + 1) +" :")
        globals()['X' + str(i + 1)].append(float(input()))
    XM.append(globals()['X' + str(i + 1)])

print("Enter output from the observations: ")
Y = []
for i in range(P):
    print("Output for Observation " + str(i + 1) +" :")
    Y.append(float(input()))

XM.append(Y)
    
print(XM)  
XM = np.transpose(XM)
print(XM.shape)
X0 = np.ones((P,), dtype=int)
XM = np.c_[X0, XM]


print()
for j in range(N + 1):
    print('X' + str(j), end = "| ")
print('Y', end = " | ")
print()
print("----------------------------")
for i in range(P): 
    for j in range(N + 2): 
        print(XM[i][j], end = " | ") 
    print()



XMT = np.transpose(XM);

A = np.matmul(XMT, XM);


Adjust(A)
