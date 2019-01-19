from math import *
import matplotlib.pyplot as plt

npoints = 1000

xcoord = [- pi / 2 + pi / (npoints - 1) * i for i in range(npoints)]
axisdistance = 18 * 5 / pi
d = sqrt(axisdistance**2 / 2)

def gd4(xf):
    if xf < - pi / 4:
        return - pi / 4
    if xf > pi / 4:
        return pi / 4

    x1 = cos(xf) * d
    ycoord = sin(xf) * d
    x2 = axisdistance - x1
    return atan(ycoord / x2)
    
x = []
y = []

for xpoint in xcoord:
    x.append(degrees(xpoint))
    y.append(degrees(gd4(xpoint)))

print(degrees(abs(gd4(- pi / 4) - gd4(- pi / 6))))
plt.plot(x, y, 'k', [- pi / 6], [gd4(- pi / 6)], 'bo')
plt.show()