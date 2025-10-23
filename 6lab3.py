# 1.3 Вычисление сигнала на выходе линейной цепи по частотной характеристикие цепи
# Взять частоту, сформировать сигнал, примешать к нему амплитуду, частоту

import numpy as np
from matplotlib import pyplot as plt

f = 150
RC = 0.01
t = np.linspace(0, 1, 1000)
w = np.linspace(1, 3/RC, 1000)

y = np.cos(2 * np.pi * f * t)
moduleACHX = 1 / np.sqrt(1 + (w * RC)**2)
argumentACHX = -np.arctan(w * RC)

y_ampl = np.convolve(y, moduleACHX, mode='same')
y_phase = np.convolve(y, argumentACHX, mode='same')

plt.subplot(3,1,1)
plt.plot(t, y)
plt.title("Исходный сигнал")
plt.xlabel("Время(t)")
plt.ylabel("H(jw)")

plt.subplot(3,1,2)
plt.plot(t, y_ampl)
plt.title("Модуль АЧХ")
plt.xlabel("Время(t)")
plt.ylabel("|H(jw)|")

plt.subplot(3,1,3)
plt.plot(t, y_phase)
plt.title("Аргумент ФЧХ")
plt.xlabel("Время(t)")
plt.ylabel("Фи(w)")
plt.tight_layout()
plt.show()
