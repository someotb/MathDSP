import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

fc = 10
fs = 32 * fc
N = 256

K = 3
fc_new = K * fc
t = np.arange(0, 2, 1 / fs)
x = np.cos(2 * np.pi * fc_new * t)

X = fft(x, N) / N
df = fs / N
k_signal = fc_new / df

print(f"Новая частота: {fc_new} Гц")
print(f"Шаг по частоте Δf: {df:.2f} Гц")
print(f"Сигнал находится в точке k = {k_signal}")

k = np.arange(N)
plt.figure(figsize=(8, 3))
plt.stem(k, np.abs(X), basefmt=" ")
plt.xlabel("k")
plt.ylabel("|X[k]|")
plt.title(f"Спектр сигнала {fc_new} Гц (k = {int(k_signal)})")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
