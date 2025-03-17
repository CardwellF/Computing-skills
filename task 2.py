# imports
import numpy as np
import matplotlib.pyplot as plt

# create subplot
fig, ax = plt.subplot(nrow=1, ncol=2)

''' Task 2A '''
# set range
2A_x = np.linspace(-2*np.pi, 2*np.pi)
# define function f(x)
f_x = np.exp((-2A_x**2)/3) + 3*np.sin(2A_x+(np.pi/4))
#plot graph for task 2A
ax[0,0].plot(f_x)
# x axis label
ax[0,0].xlabel("f_x")
# y axis label
ax[0,0].ylabel("y")
# create title
ax[0,0].title("Task 2A")
# create grid
ax[0,0].grid()

''' Task 2B '''
# set range
t = np.linspace(0, 2*np.pi, 200)
# define function X
2B_x = 2*np.sin(t) * np.exp(np.cos(t))
# define function Y
2B_y = -(3/2)*np.cos(t)*np.exp(np.sin(2*t))
# plot graph for task 2B
ax[0,1].plot(2B_x, 2B_y)
# set graph title
ax[0,1].title("Task 2B")
# x axis label
ax[0,1].xlabel("x")
# y axis label
ax[0,1].ylabel("y")
# create grid
ax[0,1].grid()

#show graphs
plt.show()
