import math
import pylab
from pylab import genfromtxt
import matplotlib.pyplot as plt

X = genfromtxt("Xinitial.txt")
Y = genfromtxt("Numsteps.txt")

plt.axvline(math.pi/2, color='b', linestyle=':')
plt.plot(X[:], Y[:], 'r.', mew = 1)
plt.axis([1.47, 1.67, 0, 50])
plt.title('Initial Values x_0 vs. Number of Steps required for '
          'Convergence (using Newton\'s method with tolerance 1e-6)')
plt.xlabel('Initial Guess (x_0)')
plt.ylabel('Number of Steps')
plt.grid(True)
plt.show()
