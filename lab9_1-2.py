# Любимов Кирилл, ИА-331, Вариант: 16
# Тип фильтра: ФВЧ - фильтр высоких частот

# Задание 1: Вычисление ИХ - импульсной хар-ки
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import freqz


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
plt.suptitle("Задание №1, расчет ИХ ФВЧ")
plt.stem(np.arange(N), h)
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid(True)
plt.tight_layout()
plt.show()

# Задание 2: Вычисление частотной характеристики ФНЧ
w, H = freqz(h, worN=1024, fs=fs)

plt.figure(figsize=(12, 4))
plt.suptitle("Задание 2: Вычисление частотной характеристики ФНЧ")
plt.subplot(1, 2, 1)
plt.plot(w, 20 * np.log10(np.abs(H)), label="АЧХ")
plt.axhline(-3, label="-3 дБ")
plt.axvline(fc, label=f"f_c = {fc} Гц")
plt.title("АЧХ (ФВЧ)")
plt.xlabel("Частота (Гц)")
plt.ylabel("Уровень (дБ)")
plt.grid(True)
plt.legend(["АЧХ", "-3 дБ", "f_c = 2000 Гц"])
plt.xlim(0, fs / 2)
plt.ylim(-80, 5)

plt.subplot(1, 2, 2)
phi = np.angle(H)
phi_unwrapped = np.unwrap(phi)
plt.plot(w, phi_unwrapped, label="ФЧХ")
plt.title("ФЧХ (ФВЧ)")
plt.xlabel("Частота (Гц)")
plt.ylabel("Фаза (рад)")
plt.grid(True)
plt.xlim(0, fs / 2)
plt.tight_layout()
plt.show()

f1 = 1500
f2 = 2500

t = np.linspace(0, 0.025, fs)
n1 = np.arange(-1000, 1000 + 1)
s_t = np.cos(2 * np.pi * f1 * t) + np.cos(2 * np.pi * f2 * t)

h = np.array([high_freq_filter(ni, omega) for ni in n1])

s_filterd = np.convolve(s_t, h, mode="same")

plt.figure(figsize=(12, 4))
plt.suptitle("Задание 3: Получить отсчеты сигнала s(t)")
plt.plot(t, s_t, label="Исходный сигнал s(t)")
plt.plot(t, s_filterd, label="Сигнал s(t) прошедший через фильтр")
plt.show()
