
import numpy as np
import matplotlib.pyplot as plt
import helpers.plots

polynomial_coeffcient = np.polynomial.polynomial.polyfromroots([-3,-8,-2,-1,2,4])


polynomial = np.poly1d(np.flip(polynomial_coeffcient)) #ustvari polinom
polynomial_odvod = np.polyder(polynomial) #analitičen odvod polinoma
polynomial_odvod_2 = np.polyder(polynomial, 2)


approx = []

def laguerre(xr, eps):
    while abs(polynomial(xr)) > eps:

        s1 =  polynomial_odvod(xr)/polynomial(xr)
        s2 = (polynomial_odvod(xr)**2 - polynomial(xr) * polynomial_odvod_2(xr))/(polynomial(xr)**2)
        n = len(polynomial_coeffcient)

        xr = xr - (n) / (s1 - np.sqrt((n-1)*(n*s2-s1**2)))
        
        approx.append(xr)

    return xr


fig, axs = plt.subplots(1, 2)

x = np.linspace(-5,4, 1000) 
y = polynomial(x)

axs[0].plot(x, y)


approx.clear()
axs[0].set_title(r"Ničla za $a_0 = " + str(-5) + "$")
print(laguerre(-5, 0))
axs[0].plot( approx , polynomial(approx), linestyle="none", marker="+", markerfacecolor="red", markeredgecolor="red", label=("Približek"))


axs[1].set_title(r"Konvergenca v odvisnosti od $\Delta x_0")

axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$p(x)$')
axs[0].grid(True)
axs[0].legend()

fig.suptitle('Prikaz Laguerreove metode')
fig.set_tight_layout(True)
plt.savefig("../analyses/img/laguerre", dpi=200)

