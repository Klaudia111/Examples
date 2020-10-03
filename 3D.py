
# Import libraries
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Set the legend font size to 12
mpl.rcParams['legend.fontsize'] = 12

# Create figure object
fig = plt.figure()

# Get the current axes
ax = fig.gca(projection='3d')

# Create data point to plot
a = np.linspace(-6 * np.pi, 6 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(a)
y = r * np.cos(a)

# Plot line graph 
ax.plot(x, y, z, label='Parametric curve', color='purple')


# Set default legend
ax.legend()

plt.show()
