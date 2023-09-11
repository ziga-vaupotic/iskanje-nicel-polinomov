


import numpy as np
import matplotlib.pyplot as plt
import helpers.plots
import random
import itertools

from collections import defaultdict

lt = [-5,-3,-2, 4,5,6]
polynomial_coeffcient = np.polynomial.polynomial.polyfromroots([-5,-3,-2, 4,5,6])

polynomial = np.poly1d(np.flip(polynomial_coeffcient)) #ustvari polinom


zeros_ap = defaultdict(lambda: [])
itearations_ap = defaultdict(lambda: None)

def makelist(dx ,lt):
    ret = []
    for x in range(0, len(lt)):
        ret.append(lt[x] + dx)
    return ret


approx = makelist( 0.7, lt)


def durand(eps):

    for n in range(0, 30):
        approx_cop = approx.copy()
        for i, x in enumerate(approx):
            if abs(polynomial(x)) < eps: 
                if(itearations_ap[i] == None):
                    itearations_ap[i] = n
                continue

            d = 1

            for k in approx_cop:
                if(k != x):
                    d = d * (x - k)

            approx[i] = x - (polynomial(x))/d
            zeros_ap[i].append( approx[i])
        #print(approx)

durand(0.02)

fig, axs = plt.subplots(1, 2)

x = np.linspace(-7,7, 1000) 
y = polynomial(x)

axs[1].plot(x, y)
for i, k in enumerate(zeros_ap):
    axs[1].plot(zeros_ap[k], [polynomial(x) for x in zeros_ap[k]], linestyle="none", marker="+", mfc="red", label="Ničla =" + str(i + 1))

axs[1].set_xlabel(r'$x$')
axs[1].set_xlim([-7, 7])
axs[1].set_ylim([-10000, 10000])
axs[1].set_ylabel(r'$p(x)$')
axs[1].grid(True)
axs[1].legend()

axs[0].set_ylabel("Število iteraciji")
axs[0].set_xlabel(r"$\Delta x$")

iterr = defaultdict(dict)

range_of_delta = np.arange(-5, 5, 0.1)

for i in range_of_delta:
    approx = makelist(i, lt)
    itearations_ap = defaultdict(lambda: None)
    durand(0.02)

    for x in itearations_ap:
        iterr[x][i] = (itearations_ap[x])
    #print(itearations_ap)

 
axs[0].set_ylabel("Število iteraciji")
axs[0].set_xlabel(r"$\Delta x$")

marker = itertools.cycle(('d', 'o', 'D', 's', '+')) 
for i, x in enumerate(list(iterr)):
    axs[0].plot(range_of_delta, [iterr[x].get(k) for k in range_of_delta], marker=next(marker), markersize=0.3, label="Ničla " + str(i + 1))
    print(iterr[x])

axs[0].legend()
axs[0].grid()
axs[0].set_title(r"Konvergenca v odvisnosti od $\Delta x$")

axs[1].set_title(r"Potek iteracije")

fig.set_tight_layout(True)

fig.suptitle('Prikaz Durand Kernerjeve metode')
plt.savefig("../analyses/img/durand", dpi=200)

