from math import (sin, cos, pi)
def func (x):
	res = sin(x % (2*pi)) - x + 2.4
	return res
k = 0
a = float(input("Начало отрезка: "))
b = float(input("Конец отрезка: "))
x0 = a
x1 = b
x2 = a	

while abs(x1-x2)>=0.00005:
	k=k+1
	x2=x1
	x1=x1-(func(x1)*(x1-x0)/(func(x1)-func(x0)))
else:
	print ("Количество итераций для метода хорд:", k)
	
def diffunc (x):
	diffres = cos(x % (2*pi)) - 1
	return diffres
k = 0
x0 = float(input("Начальная точка: "))	
x1 = b
x2 = a	
while abs(x1-x2)>=0.00005:
	k=k+1
	x2=x1
	x1=x1-(func(x1)/diffunc(x0))
else:
	print ("Количество итераций для упрощённого метода Ньютона:", k)