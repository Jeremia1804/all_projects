import numpy as np

def got_coefficient(y,x):
    add_1(x)
    # print(x)
    xT = np.transpose(x)
    xTx = xT.dot(x)
    # print(xTx)
    xTx_inverse = np.linalg.inv(xTx)
    xTy = xT.dot(y)
    # print(xT)
    A = xTx_inverse.dot(xTy)
    return A

def add_1(x):
    for  i in x:
        i.insert(0,1)

def get_note(A,x):
    sum = A[0]
    for i in range (len(x)):
        print("voici A: ",A[i+1])
        sum = sum + (A[i+1]*x[i])
    return sum

y = [10,8,2]

x = [
    [5,3,4,2],[4,2,4,7],[6,9,1,5]
]

A = got_coefficient(y,x)
j = get_note(A,[4,2,4,7])
print(A)
print(j)
