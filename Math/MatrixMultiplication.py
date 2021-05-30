def matmult(x,y):
    z=[[0,0],[0,0]]
    for iz in range(len(x)):
        for jz in range(len(y[0])):
            for kz in range(len(y)):
                z[iz][jz] += x[iz][kz] * y[kz][jz]
    return z

x = [[1,2],[3,4]]
y = [[5,6],[7,8]]
print(matmult(x,y))