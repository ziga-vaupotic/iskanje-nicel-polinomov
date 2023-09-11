
import numpy as np
import random
import matplotlib.pyplot as plt
import helpers.plots
import numpy.polynomial.polynomial as P



def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

ls = []

for i in range(0, 24): #taylorjev razvoj funkcije po sinusu
    ls.append(0)
    ls.append((-1 if i % 2 == 1 else 1)*1/(factorial(1 + 2*i)))

companion_matrix = np.polynomial.polynomial.polycompanion(ls) #ustavri matriko (potrebuje ravno obraten red koeficientov)
ls.reverse()

polynomial = np.poly1d(ls) #ustvari polinom


eval, evec = np.linalg.eig(companion_matrix) #poišči ničle, prvi seznam lastne vrednosti drugi lastni vekotrji

eval_r = [x for x in eval if np.imag(x) == 0]
eval_c = [x for x in eval if np.imag(x) != 0]


fig, axs = plt.subplots(1, 2)

x = np.linspace(-19.6, 19.6, 1000)
y = polynomial(x)
axs[1].plot(x, y, label="Funkcija", c="green", linestyle="dashed")
axs[1].plot(np.real(eval_r), [polynomial(x) for x in np.real(eval_r)], 'r+',  label="Ničle")
axs[1].set_title('Polinom')
axs[1].set_xlabel('x')
axs[1].set_ylabel(r'$p(x)$')
axs[1].set_box_aspect(1)
#plt.ylim(-1,1)
axs[1].grid(True)

axs[1].legend()


axs[0].set_title('Spekter lastnih vrednosti')
axs[0].set_xlabel(r'$Re(\lambda)$')
axs[0].set_ylabel(r'$Im(\lambda)$')
axs[0].plot(np.real(eval_r), np.imag(eval_r), 'r+', label="Realne ničle", markerfacecolor="none")
axs[0].plot(np.real(eval_c), np.imag(eval_c), 'bd', label="Kompleksne ničle", markerfacecolor="none")
axs[0].legend()
axs[0].set_box_aspect(1)
axs[0].grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

#plt.matshow(companion_matrix)

fig.suptitle("Iskanje ničel s pridruženo matriko")
fig.set_tight_layout(True)
plt.savefig("../analyses/img/eigenvalue", dpi=200)
