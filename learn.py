import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftshift, ifft

fc = 10  # Частота cos
fs = 32 * fc  # Частота дискретизации, избыточная
t = np.arange(0, 2, 1 / fs)
x = np.cos(2 * np.pi * fc * t)  # Формирование временного сигнала

plt.figure(1)
plt.plot(t, x)
plt.xlabel("$t = nT_s$")
plt.ylabel("$x[n]$")

N = fs  # Кол-во точек ДПФ
X = fft(x, N) / N

k = np.arange(0, N)

plt.figure(2)
plt.stem(k, abs(X))
plt.xlabel("k")
plt.ylabel("$x[k]$")

df = fs / N
kf = k * df
plt.figure(3)
plt.stem(kf, abs(X))  # Модуль ДПФ в частотах
plt.xlabel("Гц")
plt.ylabel("$x[k]$")

k2 = np.arange(-N / 2, N / 2)
kf2 = k2 * df
X2 = fftshift(X)  # Сдвиг ДПФ на центр
plt.figure(4)
plt.stem(kf2, abs(X2))  # Модуль ДПФ в частотах
plt.xlabel("Гц")
plt.ylabel("$x[k]$")

x_ifft = N * ifft(X, N)
t = np.arange(0, len(x_ifft)) / fs
plt.figure(5)
plt.plot(t, np.real(x_ifft))
# plt.stem(t, np.real(x_ifft))
plt.xlabel("c")
plt.ylabel("$x[n]$")
plt.show()
