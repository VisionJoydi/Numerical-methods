import numpy as np

a = 1.0
b = 2.0

def func(x):
	return 1/(1+x**4)

def derfunc(x):
	return -4*x**3/(1+x**4)**2


def Euler (h):
	
	sum=-func(a)
	for i in range (int((b-a)/h)):
		sum = sum + func(a+i*h)
	return (h/2*(func(a) + func(b)) + h**2/12 * (derfunc(a) - derfunc(b)) + h*sum)
	
def Simpson (h):
	sum=-func(a)
	hsum = 0
	for i in range (int((b-a)/h)):
		sum = sum + func(a+i*h)
		hsum = hsum + func(a+(2*i+1)*h/2)
	return (h/6*(func(a) + func(b) + 4 * hsum + 2*sum))

def RungeForEuler(h):
	return ((Euler(h/2)-Euler(h))/(2**4 - 1))
	
def RungeForSimpson(h):
	return ((Simpson(h/2)-Simpson(h))/(2**4 - 1))
	
print (Euler (0.1),'\n',
Euler (0.05),'\n',
RungeForEuler(0.05),'\n',
Euler (0.025),'\n',
RungeForEuler(0.025),'\n',
Simpson (0.1),'\n',
Simpson (0.05),'\n',
RungeForSimpson(0.05),'\n',
Simpson (0.025),'\n',
RungeForSimpson(0.025))
