import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


x_s, y_s, x_j, y_j, x_t, y_t, t = np.genfromtxt('data.txt', unpack=True, usecols=(0, 1, 2, 3, 4, 5, 6))

plt.style.use('seaborn-v0_8')

fig, axes = plt.subplots(figsize=(6, 6))




#axes.plot(x_s, y_s, '.', color='yellow', label=r'$(x,y)_{S}$')
#axes.plot(x_j, y_j, '.', color='black', label=r'$(x,y)_{J}$')




#t = np.linspace(0,len(x_s) , len(x_s))
# axes[0].plot(t, x_s, '.', color='yellow', label=r'$(x)_{S}$')
# axes[1].plot(t, y_s, '.', color='yellow', label=r'$(y)_{S}$')
# axes[2].plot(t, x_j, '.', color='black', label=r'$(x)_{J}$')
# axes[3].plot(t, y_j, '.', color='black', label=r'$(y)_{J}$')
# axes[4].plot(t, x_t, '.', color='blue', label=r'$(x)_{T}$')
# axes[5].plot(t, y_t, '.', color='blue', label=r'$(y)_{T}$')


#axes.plot(t, x_t, '.', color='blue', label=r'$(x)_{T}$')

peaks, _ = find_peaks(x_t)

tpeaksD = np.roll(t[peaks], 1)
tpeak = t[peaks]

resta = tpeak - tpeaksD
print(np.mean(resta[1:]))

##Maximo global
max1 = t[np.argmax(x_t[:60000])]
max2 = t[60000+np.argmax(x_t[60000:])]
print(max1)
print(max2)
print(max2-max1)








#axes.legend()




# Se ajustan demás detalles del gráfico.

# axes.set_xlabel('x', fontsize=12)
# axes.set_ylabel('y', fontsize=12)
# axes.legend(loc='upper left')
# axes.grid(True, linestyle='--')
# axes.set_title("x vs y", fontsize=14)
plt.tight_layout()
#fig.savefig('plot.pdf')
