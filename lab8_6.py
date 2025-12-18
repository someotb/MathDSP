import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import ifft

# Пример 1: ненулевой отсчёт в k=2
N = 16
X = np.zeros(N, dtype=complex)
X[2] = 1.0  # вещественное

x1 = np.real(ifft(X)) * N

# Пример 2: комплексное значение
X2 = np.zeros(N, dtype=complex)
X2[2] = 1j  # мнимое

x2 = np.real(ifft(X2)) * N

# Пример 3: меняем знак мнимой части
X3 = np.zeros(N, dtype=complex)
X3[2] = 2 - 1j

x3 = np.real(ifft(X3)) * N

# Пример 4: сопряжённое (меняем знак мнимой части)
X4 = np.zeros(N, dtype=complex)
X4[2] = 2 + 1j

x4 = np.real(ifft(X4)) * N

# Визуализация
n = np.arange(N)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n, x1, basefmt=" ")
plt.title("X[2] = 1 (вещественное)")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, x2, basefmt=" ")
plt.title("X[2] = 1j (чисто мнимое)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, x3, basefmt=" ")
plt.title("X[2] = 2 - 1j")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, x4, basefmt=" ")
plt.title("X[2] = 2 + 1j (сопряжённое)")
plt.grid(True)

plt.tight_layout()
plt.show()

# Вывод пояснений
print("Восстановленные сигналы — это комплексные синусоиды с разной фазой.")
print("Изменение мнимой части влияет на начальную фазу колебания.")
