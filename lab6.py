{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Untitled7.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "8GEEqh3HhWR8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "from matplotlib import mlab\n",
        "import pylab as plt\n",
        "import math "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iNXCovJm2dxb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def dif2y(x,y):\n",
        "  return y + 8.2 + 3.1*x*(1-x)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "manh-lrCWsSq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def Shooting(N):\n",
        "  y0 = 0\n",
        "  x0 = 0\n",
        "  h = 1/N\n",
        "  xlist = mlab.frange (0, 1, h)\n",
        "  \n",
        "  #описание метода\n",
        "  def RungeKutta(f, x, y):\n",
        "    def k1():\n",
        "      return h*f(x,y)\n",
        "    def k2():\n",
        "      return h*f(x+h/2, y+k1()/2)\n",
        "    def k3():\n",
        "      return h*f(x+h/2, y+k2()/2)\n",
        "    def k4():\n",
        "      return h*f(x+h, y+k3()) \n",
        "    return y + 1/6*k1() + 2/6*k2() + 2/6*k3() + 1/6*k4()\n",
        "  \n",
        "  #решение краевой задачи не зависит от параметра, поэтому вынес из цикла\n",
        "  u = 0\n",
        "  w = 1\n",
        "  def difw(x,y):\n",
        "    return u\n",
        "  def difu(x,y):\n",
        "    return w\n",
        "  for i in range (N):\n",
        "    w = RungeKutta(difw, x0+i*h, w)\n",
        "    u = RungeKutta(difu, x0+i*h, u)\n",
        "  #решение основной задачи\n",
        "  def dify(x,y):\n",
        "    return z\n",
        "  def difz(x,y):\n",
        "    return dif2y(x,y)\n",
        "  for i in range (N+1):\n",
        "    y=y0\n",
        "    z=-3.1\n",
        "    ylist = [y0]\n",
        "    for j in range (N):\n",
        "      z = RungeKutta(difz, x0+j*h, z)\n",
        "      y = RungeKutta(dify, x0+j*h, y)\n",
        "      ylist.append(y)\n",
        "    y0 = y0 - (y - math.e - 1/math.e + 2)/w\n",
        "  return plt.plot (xlist, ylist)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cBEE98rZXlfa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def q(x):\n",
        "  return 8.2 + 3.1*x*(1-x)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A9Rbv6vrBfpp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n",
        "\n",
        "def Tridiagonal(N):\n",
        "  y0 = 0\n",
        "  x0 = 0\n",
        "  h = 1/N\n",
        "  xlist = mlab.frange (0, 1, h)\n",
        "  a = [0 for i in range (N+1)]\n",
        "  m = [0 for i in range (N+1)]\n",
        "  y = [0 for i in range (N+1)]\n",
        "  #прямой ход\n",
        "  a[0]=0\n",
        "  m[0]=0\n",
        "  for i in range(N-1):\n",
        "    a[i+1] = -1/(1*a[i]-(2 + h*h))\n",
        "    m[i+1] = (h*h*q(x0+i*h) - m[i]*1)/(1*a[i]-(2 + h*h))\n",
        "  #обратный ход\n",
        "  y[N] = math.e + 1/math.e - 2\n",
        "  for i in reversed(range(1,N)):\n",
        "    y[i]=a[i]*y[i+1] + m[i]\n",
        "  y[0] = (2*y[1] + 6.2*h - h*h*q(x0))/(2 + h*h)\n",
        "  return plt.plot (xlist, y)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KzBJdr0bnum8",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O9yIDN-fNzJ4",
        "colab_type": "code",
        "outputId": "dd139f6a-460d-4ae2-efd5-e232f9657052",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "def realsolution(x):\n",
        "  return (math.exp(x) + 1/math.exp(x) + 3.1*x*x - 3.1*x - 2)\n",
        "xlist1 = mlab.frange (0, 1, 0.0001)\n",
        "realsolutionlist = [realsolution(x) for x in xlist1]"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:3: MatplotlibDeprecationWarning: numpy.arange\n",
            "  This is separate from the ipykernel package so we can avoid doing imports until\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1l6RpK2yWsVN",
        "colab_type": "code",
        "outputId": "f2cb3729-1293-4086-98d7-bf323c66bfc9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 324
        }
      },
      "source": [
        "Tridiagonal(100)\n",
        "Shooting(100)\n",
        "plt.plot(xlist1,realsolutionlist)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:5: MatplotlibDeprecationWarning: numpy.arange\n",
            "  \"\"\"\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7ff8fb3f6d68>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 126
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\nRK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    }
  ]
}