# Tiny-A5/1 
import random

def SinhSoNgauNhien(a):
    arr = []
    for i in range(0,a):
        # ramdom 0 or 1
        arr.append(random.randint(0,1))
    return arr
        
def maj(x, y, z):
    sum_xyz = int(x) + int(y) + int(z)
    if (sum_xyz <= 1):
        return 0
    return 1

def XOR(x, y):
    if (int(x) == int(y)):
        return 0
    return 1

def XOR_arr(x, y):
    s = []
    for i in range(0, len(x)):
        s.append(XOR(x[i], y[i]))
    return s

def Xoay_X(X):
    t = XOR(XOR(X[2], X[4]), X[5])
    X_xoay = [str(t)]
    for i in range(0, 5):
        X_xoay.append(str(X[i]))
    return X_xoay

def Xoay_Y(Y):
    t = XOR(Y[6], Y[7])
    Y_xoay = [str(t)]
    for i in range(0, 7):
        Y_xoay.append(str(Y[i]))
    return Y_xoay

def Xoay_Z(Z):
    t = XOR(XOR(Z[2], Z[7]), Z[8])
    Z_xoay = [t]
    for i in range(0, 8):
        Z_xoay.append(str(Z[i]))
    return Z_xoay

def sinh_Si(x, y, z):
    m = maj(x[1], y[3], z[3])
    if (m == int(x[1])):
        x = Xoay_X(x)
    if (m == int(y[3])):
        y = Xoay_Y(y)
    if (m == int(z[3])):  
        z = Xoay_Z(z)
    return x,y,z

def Key_S(num):
    # x = SinhSoNgauNhien(6)
    # y = SinhSoNgauNhien(8)
    # z = SinhSoNgauNhien(9)
    
    x = [1,0,0,1,0,1]
    y = [0,1,0,0,1,1,1,0]
    z = [1,0,0,1,1,0,0,0,0]

    s = []
    
    for i in range(0, num):
        x,y,z = sinh_Si(x, y, z)
        si = XOR(x[5], XOR(y[7], z[8]))
        s.append(si)    
    return s

p = [1,1,1]

print(XOR_arr(p, Key_S(len(p))))
