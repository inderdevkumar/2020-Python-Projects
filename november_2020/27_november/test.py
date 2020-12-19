import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 1000)
print(x)

plt.hist(x, bins = 50)

plt.show()
