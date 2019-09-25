aux = []
mtx = []
I = []
B = []
D = []

n = int(input("Digite n: ")) #ENTRA COM O TAMANHO DA MATRIZ

#ENTRA COM OS VALORES DA MATRIZ

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = float(input("MTX[{}][{}] = ".format(i, j)))    
        aux.append(a)
    mtx.append(aux)
    aux = []

#ZERA TODOS OS VALORES DA MATRIZ D
for i in range(1, n + 1):
    for j in range(1, (2 * n) + 1):  # n + 1):
        a = 0
        aux.append(a)
    D.append(aux)
    aux = []
    
#ZERA TODOS OS VALORES DA MATRIZ I
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = 0
        aux.append(a)
    I.append(aux)
    aux = []

#ZERA TODOS OS VALORES DA MATRIZ B
for i in range(1, n + 1):
    for j in range(1, (2 * n) + 1):  # n + 1):
        a = 0
        aux.append(a)
    B.append(aux)
    aux = []
    
print("MATRIZ INSERIDA ")  #PRINTA A MATRIZ INSERIDA

for i in range(len(mtx)):
    print(mtx[i]) 

#CRIA A MATRIZ IDENTIDADE
for i in range(len(mtx)):
    for j in range(len(mtx)):
        if(i == j):
            I[i][j] = 1
        else:
            I[i][j] = 0

#PRINTA A MATRIZ IDENTIDADE
print("MATRIZ IDENTIDADE")  
for i in range(len(I)):
    print(I[i])

#JUNTA A MATRIZ INSERIDA E A MATRIZ IDENTIDADE
for i in range(len(mtx)):
    for j in range(2 * len(mtx)):
      if(j <= (n - 1)):
        B[i][j] = mtx[i][j]
      else:
        B[i][j] = I[i][j - n]



print("MATRIZ INSERIDA E MATRIZ IDENTIDADE")  #PRINTA A MATRIZ INSERIDA E MATRIZ IDENTIDADE 
for i in range(len(B)):
    print(B[i])

#COMEÇA A SE INVERTER MATRIZ
#ZERAR AS LINHAS ONDE mtx[I][J] SÃO DIFERENTES DE mtx[I][I]

#PRIMEIRA PARTE DO ESCALONAMENTO
for j in range(len(mtx)):
    for i in range(len(mtx)):
        if(i > j):
            c = -(B[i][j] / B[j][j])
            for k in range(2 * len(mtx)):
                B[i][k] = c * B[j][k] + B[i][k]

print("PRIMEIRA PARTE DO ESCALONAMENTO")  #PRINTA PRIMEIRA PARTE DO ESCALONAMENTO 
for i in range(len(B)):
    print(B[i])

#SEGUNDA PARTE DO ESCALONAMENTO
for i in range(len(mtx)):
    for j in range(len(mtx)):
        if(j>i):
            v = -(B[i][j] / B[j][j])
            for k in range(2 * len(B)):
                B[i][k] = v * B[j][k] + B[i][k]

print("SEGUNDA PARTE DO ESCALONAENTO")  #PRINTA SEGUNDA PARTE DO ESCALONAMENTO
for i in range(len(B)):
    print(B[i])
                  
#DIVIDI OS PIVOS POR ELES MESMOS, ATÉ FICARE UNITARIOS
for i in range(len(mtx)):
    for j in range(2 * len(mtx)):
      if(j <= (n - 1)):
        D[i][j] = (B[i][j] / B[i][i])
      else:
        D[i][j] = (B[i][j] / B[i][i])


print("MATRIZ POS ESCALONAENTO")
for i in range(len(D)):
    print(D[i])


q = []
p = []
#PRINTA A MATRIZ INVERSA
print("MATRIZ INVERSA")
for i in range(len(mtx)):
    for j in range(2 * len(mtx)):
      if(j >= (n)): 
        q.append(D[i][j])
    p.append(q)
    q = []

for i in range(len(p)):
    print(p[i])