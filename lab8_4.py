import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

fc = 10
fs = 32 * fc
N = 512

t = np.arange(0, 2, 1 / fs)
x = np.cos(2 * np.pi * fc * t)

X = fft(x, N) / N
df = fs / N
k_signal = fc / df

print(f"Частота сигнала: {fc} Гц")
print(f"Количество точек ДПФ: N = {N}")
print(f"Шаг по частоте Δf: {df:.3f} Гц")
print(f"Сигнал находится в точке k = {k_signal}")

k = np.arange(N)
plt.figure(figsize=(10, 3))
plt.stem(k, np.abs(X), basefmt=" ", markerfmt="C1o", linefmt="C1-")
plt.xlabel("k")
plt.ylabel("|X[k]|")
plt.title(f"ДПФ с N={N}: пик на k = {int(k_signal)}")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
