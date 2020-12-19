import matplotlib.pyplot as plt

#Add the required packages to make the program work

Names1= ["Section_A", "Section_B", "Section_C"]
Values1= [2, 20, 200]

plt.figure(figsize=(9,3))
plt.subplot(131)

#Add code here for plotting a bar graph using Names1 and Values1
plt.bar(Names1,Values1)

plt.subplot(132)
#Add code here for plotting a scatterplot using Names1 and Values1
plt.scatter(Names1,Values1, c ="blue")

plt.subplot(133)
plt.plot(Names1, Values1)

plt.suptitle("Different Types of Plotting")

#Add the code here to save the figure with name display.png
plt.savefig('display.png')

plt.show()
