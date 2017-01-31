import math
import pylab
from pylab import genfromtxt
import matplotlib.pyplot as plt


X = genfromtxt("Fail.txt")

n = len(X)
xmin = X[0]
xmax = X[n-1]
height = .1
Y = []

for i in range(n):
    Y.append(0)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(xmin - .2, xmax + .2)
ax.set_ylim(-0.1, 0.1)


plt.hlines(0, xmin, xmax)
plt.vlines(xmin, - .05, .05)
plt.vlines(math.pi/2, - height / 2, height / 2)
plt.vlines(xmax, - height / 2, height / 2)

plt.plot(X[:], Y[:], 'b|', mew = 1)
plt.axis([1.46, 1.68, -1, 1])
plt.title('Initial Guess Values x_0 which failed to converge in less '
          'than 50 steps (using Newton\'s method with tolerance 1e-6)')
plt.xlabel('Initial Guess (x_0)')
#plt.ylabel('Number of Steps')
#plt.grid(True)

plt.text(xmin, -.1, '1.47', horizontalalignment='center')
plt.text(1.57, -.1, '1.57', horizontalalignment='center')
plt.text(xmax, -.1, '1.67', horizontalalignment='center')
plt.text(1.57, -.25, 'Initial Guess (x_0)', horizontalalignment='center')

plt.axis('off')
plt.show()
