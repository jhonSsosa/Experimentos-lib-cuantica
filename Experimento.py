def trans(b):
    complejo = " "
    matriz_trans = b
    for i in range(len(b)):
        for j in range(i,len(b)):
            complejo = matriz_trans[j][i]
            matriz_trans[j][i] = matriz_trans[i][j]
            matriz_trans[i][j] = complejo
    return matriz_trans

def prodrealesMv(v, w):
    if len(v) != len(w[0]):
        return 'No'

    prod = []
    i = 0
    while i < len(v[0]):
        prod.append([])
        j = 0
        while j < len(w):
            k = 0
            suma = 0

            while k < len(v):
                suma = suma + v[k][i] * w[j][k]
                k += 1
            prod[i].append(suma)
            j += 1
        i += 1
    return trans(prod)

def suma(a,b):
    cc = (a[0] + b[0])
    ci = (a[1] + b[1])
    return (cc,ci)

def producto(a,b):
    cc = ((a[0] * b[0]) - (a[1] * b[1]))
    ci = ((a[0] * b[1]) + (b[0] * a[1]))
    return (cc, ci)


def prodMv(v,w):
    if len(v)!=len(w[0]):
        return 'No'

    prod=[]
    i=0
    while i<len(v[0]):
        prod.append([])
        j=0
        while j<len(w):
            k=0
            suma=(0,0)

            while k<len(v):
                suma=suma(suma,producto(v[k][i],w[j][k]))
                k+=1
            prod[i].append(suma)
            j+=1
        i+=1


    return trans(prod)