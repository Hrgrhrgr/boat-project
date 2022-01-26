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
# Integrál splinu
print(interpolate.splint(3, 6, tck))


plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Cubic-spline interpolation')
plt.show()# -*- coding: utf-8 -*-
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
# Integrál splinu
print(interpolate.splint(3, 6, tck))


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
                      [8, 18],
                      [12, 35],
                      ])
splajna = interpolate.splrep(station00[:,0], station00[:,1],s=0.8)
xnew = np.arange(0, 12, 0.1)
ynew = interpolate.splev(xnew, splajna)

plt.figure()
plt.plot(station00[:,0], station00[:,1], 'x', xnew, ynew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()

keelPoints = np.array([[0, 15],
                      [220, 0],
                      [221, 0],
                      [450, 8],
                      ])
splajna = interpolate.splrep(keelPoints[:,0], keelPoints[:,1], k=2,s=0.0)
xnew = np.arange(0, 451, 1)
ynew = interpolate.splev(xnew, splajna)

plt.figure()
plt.plot(keelPoints[:,0], keelPoints[:,1], 'x', xnew, ynew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()

midPoints = np.array([[-25, 45],
                      [0, 0],
                      [25, 45],
                      ])
splajna = interpolate.splrep(midPoints[:,0], midPoints[:,1], k=2,s=0)
xnew = np.arange(-25, 26, 1)
ynew = interpolate.splev(xnew, splajna)

plt.figure()
plt.plot(midPoints[:,0], midPoints[:,1], 'x', xnew, ynew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()



#stations = np.linspace(0, 4.4, num = 23)
stations = [0, 60, 120, 230, 350, 400, 450]

station00 = np.array([[0, 10],
                      [0.1, 10],
                      [5, 14],
                      [8, 18],
                      [12, 35],
                      ])
splajna = interpolate.splrep(station00[:,0], station00[:,1])
xnew = np.arange(0, 12, 0.1)
ynew = interpolate.splev(xnew, splajna)

plt.figure()
plt.plot(station00[:,0], station00[:,1], 'x', xnew, ynew)
plt.legend(['Linear', 'Cubic Spline'])
plt.title('Cubic-spline interpolation')
plt.show()

