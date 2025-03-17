#parrametric function
import numpy as np
import matplotlib.pyplot as plt

# set range (t)
t = np.linspace(0, 2*np.pi)
# x equation
x_t = 2*np.sin(t)*(np.exp(np.cos(t)))
# y equation
y_t = -(3/2)*np.cos(t)*(np.exp(np.sin(2*t)))
# plot graph with 200 points
plt.plot(x_t, y_t, bins=200, label="parametric functions")
# show grid
plt.grid()
# create legend
plt.legend()
# show graph
plt.show()
