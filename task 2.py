#imports
import numpy as np
import matplotlib.pyplot as plt
#set the range (-2pi, 2pi)
x = np.linspace(-2*np.pi, 2*pi)
#set the equation
f_x=np.exp((-x**2)/3)+3*np.sin(x +(np.pi/4))
#plot the equation as graph
plt.plot(f_x, label="f_x=e((-x^2)/3)+3sin(pi/4)")
#set legend(a table of all lines on a graph)
plt.legend()
#title
plt.title("Task 2A")
#enable grid
plt.grid()
#show graph
plt.show()
