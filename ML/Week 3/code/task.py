import numpy as np
from math import sin, exp
import scipy.optimize
import matplotlib.pyplot as plt
import matplotlib as mpl

def f(x: float):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)

def h(x: float):
    return int(f(x))

def test_and_plot(function, accuracy = 50):
    ax_x = np.linspace(1,30,accuracy)

    # the function, which is y = x^2 here
    ax_y = np.array([function(val) for val in ax_x])

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

    # show the plot
    plt.show()

#test_and_plot(f)
test_and_plot(h, 1000)

print("Task 1 output:\n{} {}".format(scipy.optimize.minimize(f, 2, method='bfgs').fun,
                                     scipy.optimize.minimize(f, 30, method='bfgs').fun))

bounds = [(1, 30)]
print("Task 2 output:\n{}".format(scipy.optimize.differential_evolution(f, bounds).fun))

print("Task 3 output:\n{} {}".format(scipy.optimize.minimize(h, 30, method='bfgs').fun,
                                     scipy.optimize.differential_evolution(h, bounds).fun))

# Such results of BFGS occure due to the fact it's a value of hoizontal part at this point