PI = 3.1415926535
def dot(x,y):
    return sum(x_i*y_i for x_i, y_i in zip(x, y))

def cross(u,v):  
    dim = len(u)
    s = []
    for i in range(dim):
        if i == 0:
            j,k = 1,2
            s.append(u[j]*v[k] - u[k]*v[j])
        elif i == 1:
            j,k = 2,0
            s.append(u[j]*v[k] - u[k]*v[j])
        else:
            j,k = 0,1
            s.append(u[j]*v[k] - u[k]*v[j])
    return s
def subtract(a,b):
    size = len(a)
    s = []
    for i in range(size):
        s.append(a[i]-b[i])
    return s

def norm(a):
    magnitude = 0
    for i in a:
        magnitude += i ** 2
    magnitude = magnitude ** 0.5
    return magnitude

def divide(a,b):
    size = len(a)
    s = []
    for i in range(size):
        s.append(a[i]/b)
    return s

def deg2rad(x):
    return x * (PI/180)

def det(a):
    size = len(a)
    if size == 1:
        return a[0][0]
    elif size == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    elif size == 3:
        return a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] \
               - a[0][0] * a[1][2] * a[2][1] - a[0][1] * a[1][0] * a[2][2] - a[0][2] * a[1][1] * a[2][0]
    else:
        mow = [pow(-1, x) * a[0][x] for x in range(len(a))]
        for y in range(size):
            grant = []
            for z in range(len(a)):
                if z != 0:
                    filarr = []
                    for w in range(len(a)):
                        if w != y:
                            filarr.append(a[z][w])
                    grant.append(filarr)
            mow[y] *= det(grant)
        return sum(mow)

def mtxmul(a,b):
    
    if type(a) != list:
        return [a * b[i] for i in range(len(b))]

    matrix = [[0 for x in range(4)] for j in range(len(a))]
    
    for each in a:
        if len(each) != len(b):
            raise Exception
    for x in range(len(a)):
        for y in range(len(b[0])):
            for z in range(len(b)):
                matrix[x][y] += a[x][z] * b[z][y]
    return matrix

