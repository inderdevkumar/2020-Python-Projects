import numpy as np
import matplotlib.pyplot as plt

t= np.arange(0, 5, 0.2)
t2= t**2
t3= t**3
t4= t**4

# Plot  blue dot
plt.scatter(t,t3, c ="blue")
 
# Plot a line graph with dotted and teal color
plt.plot(t2, t4, c='red', ls=('dotted'), lw=4)
 

#Add the code here to save the figure with name display.png
plt.savefig('display.png')

plt.show()
