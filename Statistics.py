import matplotlib.pyplot as plt
import numpy as np

f = 2

x = np.array([i for i in range(0,360 * f)])
s = np.array([np.sin(2 * np.pi* i / 360) for i in x])
c = np.array([np.cos(2 * np.pi* i / 360) for i in x])

plt.plot(x, s, color = "r")
plt.plot(x, c, color = "b")
plt.show()
