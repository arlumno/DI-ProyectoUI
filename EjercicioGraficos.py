import matplotlib.pyplot as plt
import numpy as np
import time

print("01")

colores = ['pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
           'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper','PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
           'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic','flag', 'prism', 'ocean', 'gist_earth', 'terrain',
           'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
           'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
           'turbo', 'nipy_spectral', 'gist_ncar']
print(str(len(colores)) + " Colores")

plt.figure()
plt.title("Ejercicio Armando Castro")
print("Procesando " + str(len(colores)) + " gamas de colores.")

for color in colores:
    print(color)
    plt.pcolormesh(np.random.rand(30,30), cmap= color)
    plt.pause(0.1)
    time.sleep(0.2)
print("Programa finalizado.")