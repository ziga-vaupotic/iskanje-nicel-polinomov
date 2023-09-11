import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import helpers.plots

res = []
intervals = []

polynomial_coeffcient = np.polynomial.polynomial.polyfromroots([-2, -3, -8, 2, 4, 7, 9])

polynomial = np.poly1d(np.flip(polynomial_coeffcient)) #ustvari polinom
def bisection(interval, eps):
    #intervals.append(interval.copy())
    a = (interval[0] + interval[1]) / 2
    while abs(polynomial(a)) > eps:
        a = (interval[0] + interval[1]) / 2
        res.append(a)
        
        if(polynomial(a) * polynomial(interval[0]) < 0):
            interval[1] = a
        else:
            interval[0] = a
        
        intervals.append(interval.copy())
    return a

interval = [0, 3]

x = [np.linspace(-3, 4, 1000), np.linspace(0, 3, 1000)]
y = [polynomial(k) for k in x]

solve = (bisection(interval.copy(), 0.001))

fig, axs = plt.subplots(1, 2)

for i, a in enumerate(axs):
    a.plot(x[i], y[i], linestyle="dashed")
    a.set_xlabel('x')
    a.set_ylabel('p(x)')
    a.plot( interval, [polynomial(x) for x in interval], linestyle="none", marker="d", markerfacecolor="green", markeredgecolor="green", label=r"Začetni interval $a_{1}, a_{2}$")
    a.set_box_aspect(1)

#plt.grid(True)
axs[1].plot( res, [polynomial(x) for x in res], linestyle="none", marker="|", markerfacecolor="red", markeredgecolor="red", label = r"Prilagojen interval $a$")
axs[0].plot( res, [polynomial(x) for x in res], linestyle="none", marker="+", markerfacecolor="red", markeredgecolor="red", label = r"Prilagojen interval $a$")

axs[0].set_title(r"Prikaz približkov ničel $a_n$")
axs[1].set_title("Prikaz intervalov")

axs[1].hlines(y=0, xmin=0, xmax=3, linestyle="dotted", colors="purple")


size = len(intervals)
for i,x in enumerate(intervals):
    plt.gca().add_patch(Rectangle((x[0], -10000), abs(x[1]-x[0]), 35000, facecolor="red", alpha=i/size * 0.8 + 0.1)) #(np.arange(x[0], x[1], 0.01), 100000, facecolor='green', alpha=.5)

axs[0].legend(loc='lower left')
axs[0].grid()

fig.suptitle('Prikaz Biskecije')
fig.set_tight_layout(True)
plt.savefig("../analyses/img/bisection", dpi=200)

