# Любимов Кирилл, ИА-331, Вариант: 16
# Тип фильтра: ФВЧ - фильтр высоких частот

# Задание 1: Вычисление ИХ - импульсной хар-ки
import numpy as np
from matplotlib import pyplot as plt


def high_freq_filter(n, omega):
    if n == 0:
        return (np.pi - omega) / np.pi
    else:
        return -np.sin(omega * n) / (np.pi * n)


fc = 2000  # Частота среза фильтра
perehod_polosa_f = 1500  # Ширина переходной полосы
fs = 9000  # Частота дискретизации
delta_f = perehod_polosa_f / fs

omega = 2 * np.pi * fc / fs  # Нормированная частота среза
N = int(np.ceil(3.3 / delta_f))
if N % 2 == 0:
    N += 1

M = (N - 1) // 2

n = np.arange(-M, M + 1)
h = np.array([high_freq_filter(ni, omega) for ni in n])

plt.figure(figsize=(8, 4))
plt.stem(np.arange(N), h)
plt.title("ИХ ФВЧ (вариант 16)")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)
plt.tight_layout()
plt.show()
