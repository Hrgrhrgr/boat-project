# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:56:01 2022

@author: Jirka Čech
"""

from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
import time

# fce pro kubickou interpolaci
def f(x):
    x_points = [ 0, 1, 2, 3, 4, 5]
    y_points = [12,14,22,39,58,77]

    # stačí následující dva řádky
    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)

print(f(1.25))

# Další příklad splinu
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0)
# Print hodnoty pro hovnotu
hovnota = 0.5
print(interpolate.splev(hovnota, tck, der=0))

plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Cubic-spline interpolation')
plt.show()

#stations = np.linspace(0, 4.4, num = 23)
stations = [0, 60, 120, 230, 350, 400, 450]

station00 = np.array([[0, 10],
                      [5, 14],
                      [10, 18],
                      [12, 35],
                      ])

