# 1.1 Вычисление интеграла свертки сигнала и импульсной характеристики

import numpy as np
from matplotlib import pyplot as plt

T = 0.01
f = 800

t = np.linspace(0, T*8, 1000)
RC = 0.01

h_t = 1/RC * np.exp(-t/RC)

plt.subplot(3, 1, 1)
plt.plot(t, h_t)
plt.title("Импульсная характеристика")
plt.xlabel("Время(t)")
plt.ylabel("Амплитуда(A)")

s1_t = np.cos(2*np.pi * f * t)

plt.subplot(3, 1, 2)
plt.plot(t, s1_t)
plt.title("Непрерывный сигнал")
plt.xlabel("Время(t)")
plt.ylabel("Амплитуда(A)")

result = np.convolve(s1_t, h_t, mode='same')

plt.subplot(3, 1, 3)
plt.plot(t, result)
plt.title("Свертка")
plt.xlabel("Время(t)")
plt.ylabel("Амплитуда(A)")
plt.tight_layout()
plt.show()