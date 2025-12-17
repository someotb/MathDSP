from cProfile import label

import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import fft, fftshift, ifft

# Для заданных значений частоты синала и частоты дискретизации получите дискретное колебания
fc1 = 5  # Частота cos
fs1 = fc1 * 100
t1 = np.arange(0, 2, 1 / fs1)
s1 = np.cos(2 * np.pi * fc1 * t1)

# Далее увеличьте частоту сигнала в несколько раз

fc2 = fc1 * 5
fs2 = fc2 * 100
t2 = np.arange(0, 2, 1 / fs2)
s2 = np.cos(2 * np.pi * fc2 * t2)

plt.figure(1)
plt.plot(t1, s1, label="Частота 5 Гц")
plt.plot(t2, s2, label="Частота 25 Гц")
plt.legend()
plt.show()
