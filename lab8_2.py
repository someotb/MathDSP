import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

fc = 10  # Частота cos
fs = 32 * fc  # Частота дискретизации, избыточная
t = np.arange(0, 2, 1 / fs)
x = np.cos(2 * np.pi * fc * t)  # Формирование временного сигнала

plt.figure(1)
plt.plot(t, x)
plt.xlabel("$t = nT_s$")
plt.ylabel("$x[n]$")

N = 256  # Кол-во точек ДПФ
df = fs / N
k = np.arange(0, N)
X = fft(x, N) / N

print("Шаг частот между точками ДПФ: ", df)
print("Сигнал fc =", fc, "Гц находится в точке k =", fc / df)

plt.figure(2)
plt.stem(k, np.abs(X))
plt.xlabel("k")
plt.ylabel("$x[k]$")
plt.show()
