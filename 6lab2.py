# 1.2 Вычисление частотной характеристики RC цепи

import numpy as np
from matplotlib import pyplot as plt

RC = 0.01
w = np.linspace(1, 3/RC, 1000)

H_jw = 1 / (1 + 1j * w * RC)
moduleACHX = 1 / np.sqrt(1 + (w * RC)**2)
argumentACHX = -np.arctan(w * RC)

plt.subplot(3,1,1)
plt.plot(w, H_jw)
plt.title("Частотная характеристика RC цепи")
plt.xlabel("Частота(Гц)")
plt.ylabel("H(jw)")

plt.subplot(3,1,2)
plt.plot(w, moduleACHX)
plt.title("Модуль АЧХ")
plt.xlabel("Частота(Гц)")
plt.ylabel("|H(jw)|")

plt.subplot(3,1,3)
plt.plot(w, argumentACHX)
plt.title("Аргумент ФЧХ")
plt.xlabel("Частота(Гц)")
plt.ylabel("Фи(w)")
plt.tight_layout()
plt.show()
