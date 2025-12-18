import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

fc1 = 10
fc2 = 25
fs = 32 * max(fc1, fc2)
N = 512

t = np.arange(0, 2, 1 / fs)
x = np.cos(2 * np.pi * fc1 * t) + np.cos(2 * np.pi * fc2 * t)

X = fft(x, N) / N
df = fs / N

print(f"Сигнал: cos({fc1} Гц) + cos({fc2} Гц)")
print(f"Пики ожидаются в k1 = {fc1 / df:.0f}, k2 = {fc2 / df:.0f}")

k = np.arange(N)
plt.figure(figsize=(10, 3))
plt.stem(k, np.abs(X), basefmt=" ")
plt.xlabel("k")
plt.ylabel("|X[k]|")
plt.title("Спектр суммы двух косинусов")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
