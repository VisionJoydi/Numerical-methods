import numpy as np
n = int(input("Размер матрицы А:"))
A0 = np.zeros((n, n))
b0 = np.zeros((1, n))
print("Введите матрицу А")
for i in range(n):
	for j in range(n):
		A0[i,j] = float(input())
print("Введите матрицу b")
for i in range(n):
	b0[0,i] = float(input())

	
A=np.concatenate((A0,b0.T),axis=1)
#Gauss
lu = np.array(np.zeros((n, n+1)))
			
for k in range(n):
    for i in range(k, n):
        lu[i,k] = A[i, k] - np.dot(lu[i, :k],lu[:k, k]) #b[i,j]
    for j in range(k + 1, n+1):
        lu[k, j] = (A[k, j] - np.dot(lu[k, :k],lu[:k, j])) / lu[k, k] #c[i,j]

#get L
lm = np.zeros((n, n))
for k in range(n):
	lm[k, k] = 1
	for j in range(k+1, n):
           lm[k, j] = lu[k,j]

b = np.zeros((n,1))
for k in range (n):
	b[k,0]=lu[k,n]
			

xg = np.zeros((n, 1))
for k in range (1,n+1):
	xg[-k,0] = b[-k,0] - np.dot(lm[-k,-k:],xg[-k:,0])
	
print(xg)

#Jakobу
D= np.zeros((n,n))
for k in range (n):
	D[k,k]=A0[k,k]

Dinv = np.linalg.inv(D) 

x0 = np.zeros((n, 1))
x1 = np.dot(np.dot(Dinv,D-A0),x0) + np.dot(Dinv,b0.T)
k = 0
while (np.linalg.norm(x1-x0))>=0.00005: 
	k = k+1
	x0 = x1
	x1 = np.dot(np.dot(Dinv,D-A0),x1) + np.dot(Dinv,b0.T)
else: 
	print ("Количество итераций для метода Якоби:", k)
	
#Gauss-Seidel
L = np.tril(A0-D)
R = np.triu(A0-D)
F = -1*np.linalg.inv(np.identity(n) + np.dot(Dinv,L))

x0 = np.zeros((n, 1))
x1 = np.dot(np.dot(F,np.dot(Dinv,R)),x0) + np.dot(F,np.dot(Dinv, b0.T))
k=0
while (np.linalg.norm(x1-x0))>=0.00005: 
	k = k+1
	x0 = x1
	x1 = np.dot(np.dot(F,np.dot(Dinv,R)),x1) + np.dot(F,np.dot(Dinv, b0.T))
else: 
	print ("Количество итераций для метода Гаусса-Зейделя:", k)











