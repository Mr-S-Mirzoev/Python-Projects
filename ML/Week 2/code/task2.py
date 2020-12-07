import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
import matplotlib as mpl

def f(x: int):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

def f_by_w(w: np.array):
    def funct(x):
        value = 0
        for i in range(w.shape[0]):
            value += w[i] * (x ** i)
        
        return value
    
    return funct

x = np.array([1, 4, 10, 15])
b = np.array([f(val) for val in x])
A = np.zeros((len(x), len(x)))
for i in range(len(x)):
    for j in range(len(x)):
        A[i][j] = x[i] ** j
w = scipy.linalg.solve(A, b)
print(w)
print(A.dot(w), b)

ax_x = np.linspace(0,20,100)

# the function, which is y = x^2 here
ax_y = np.array([f_by_w(w)(val) for val in ax_x])
ax_y_f = np.array([f(val) for val in ax_x])

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('axes', 0))
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
# Colors: https://python-graph-gallery.com/196-select-one-color-with-matplotlib/
plt.plot(ax_x, ax_y, 'r', color='lawngreen')
plt.plot(ax_x, ax_y_f, 'r', color='magenta')

# show the plot
plt.show()