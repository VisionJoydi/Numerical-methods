
import numpy as np
from matplotlib import mlab
import pylab as plt
import math

def dif2y(x,y):
  return y + 8.2 + 3.1*x*(1-x)

def Shooting(N):
  y0 = 0
  x0 = 0
  h = 1/N
  xlist = mlab.frange (0, 1, h)
  
  #описание метода
  def RungeKutta(f, x, y):
    def k1():
      return h*f(x,y)
    def k2():
      return h*f(x+h/2, y+k1()/2)
    def k3():
      return h*f(x+h/2, y+k2()/2)
    def k4():
      return h*f(x+h, y+k3()) 
    return y + 1/6*k1() + 2/6*k2() + 2/6*k3() + 1/6*k4()
  
  #решение краевой задачи не зависит от параметра, поэтому вынес из цикла
  u = 0
  w = 1
  def difw(x,y):
    return u
  def difu(x,y):
    return w
  for i in range (N):
    w = RungeKutta(difw, x0+i*h, w)
    u = RungeKutta(difu, x0+i*h, u)
  #решение основной задачи
  def dify(x,y):
    return z
  def difz(x,y):
    return dif2y(x,y)
  for i in range (N+1):
    y=y0
    z=-3.1
    ylist = [y0]
    for j in range (N):
      z = RungeKutta(difz, x0+j*h, z)
      y = RungeKutta(dify, x0+j*h, y)
      ylist.append(y)
    y0 = y0 - (y - math.e - 1/math.e + 2)/w
  return plt.plot (xlist, ylist)

def q(x):
  return 8.2 + 3.1*x*(1-x)

def Tridiagonal(N):
  y0 = 0
  x0 = 0
  h = 1/N
  xlist = mlab.frange (0, 1, h)
  a = [0 for i in range (N+1)]
  m = [0 for i in range (N+1)]
  y = [0 for i in range (N+1)]
  #прямой ход
  a[0]=0
  m[0]=0
  for i in range(N-1):
    a[i+1] = -1/(1*a[i]-(2 + h*h))
    m[i+1] = (h*h*q(x0+i*h) - m[i]*1)/(1*a[i]-(2 + h*h))
  #обратный ход
  y[N] = math.e + 1/math.e - 2
  for i in reversed(range(1,N)):
    y[i]=a[i]*y[i+1] + m[i]
  y[0] = (2*y[1] + 6.2*h - h*h*q(x0))/(2 + h*h)
  return plt.plot (xlist, y)



def realsolution(x):
  return (math.exp(x) + 1/math.exp(x) + 3.1*x*x - 3.1*x - 2)
xlist1 = mlab.frange (0, 1, 0.0001)
realsolutionlist = [realsolution(x) for x in xlist1]

Tridiagonal(100)
Shooting(100)
plt.plot(xlist1,realsolutionlist)