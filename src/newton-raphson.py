
import numpy as np
import matplotlib.pyplot as plt
import helpers.plots

polynomial_coeffcient = np.polynomial.polynomial.polyfromroots([-3,-8,-2,-1,2,4])


polynomial = np.poly1d(np.flip(polynomial_coeffcient)) #ustvari polinom
polynomial_odvod = np.polyder(polynomial) #analitičen odvod polinoma


def tangenta(x, a, b, c):
    return (x - c)*b + a

linear_func = []

def newton(xr, eps):
    n = 0
    while abs(polynomial(xr)) > eps:
        linear_func.append([polynomial(xr),polynomial_odvod(xr), xr])
        xr = xr - polynomial(xr) / polynomial_odvod(xr)
        n = n + 1

    linear_func.append([polynomial(xr),polynomial_odvod(xr), xr])
    print(n)
    return xr


fig, axs = plt.subplots(1, 2)

x = np.linspace(-5,4, 1000) 
y = polynomial(x)

for i in axs:
 i.plot(x, y)


for i, g in enumerate([-3, 5]):
    linear_func.clear()
    axs[i].set_title(r"Ničla za $a_0 = " + str(g) + "$")
    print(newton(-g, 0.00001))
    done = False
    for par in linear_func:
        zeo = par[2]
        null = -par[0]/par[1] + par[2]
        sp = np.linspace(zeo - abs(zeo - null), zeo + abs(zeo - null), 3)
        axs[i].plot(sp, tangenta(sp, par[0], par[1], par[2]), linestyle="dotted", color="purple", label=("Iteracijske tangente" if done == False else ""))

        axs[i].plot( par[2] , polynomial( par[2]), linestyle="none", marker="+", markerfacecolor="red", markeredgecolor="red", label=("Približek" if done == False else ""))

        done = True

for i in axs:
 i.set_xlabel(r'$x$')
 i.set_ylabel(r'$p(x)$')
 i.grid(True)
 i.legend()

fig.suptitle('Prikaz Newtonove metode')
fig.set_tight_layout(True)
plt.savefig("../analyses/img/newton", dpi=200)

