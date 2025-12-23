# Задание 3: Получить отсчеты сигнала s(t)
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz

fs = 9000
T = 0.025
t = np.arange(0, T, 1 / fs)

f1 = 2500  # пропускается
f2 = 1500  # подавляется

s = np.cos(2 * np.pi * f1 * t) + np.cos(2 * np.pi * f2 * t)

# Спектр (ДПФ)
S = np.fft.fft(s)
freq = np.fft.fftfreq(len(S), 1 / fs)

plt.figure(figsize=(10, 4))
plt.plot(freq[: len(freq) // 2], np.abs(S[: len(S) // 2]))
plt.title("Спектр входного сигнала s(n)")
plt.xlabel("Частота, Гц")
plt.ylabel("|S(f)|")
plt.grid()
plt.show()


# Задание 4: Фильтрация сигнала (свёртка) и спектр на выходе
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

y = np.convolve(s, h, mode="same")

Y = np.fft.fft(y)

plt.figure(figsize=(10, 4))
plt.plot(freq[: len(freq) // 2], np.abs(Y[: len(Y) // 2]))
plt.title("Спектр сигнала после ФВЧ")
plt.xlabel("Частота, Гц")
plt.ylabel("|Y(f)|")
plt.grid()
plt.show()


# Задание 5: Оконная функция (Хэмминга)
M = (len(h) - 1) // 2
n = np.arange(-M, M + 1)

w = 0.54 + 0.46 * np.cos(np.pi * n / M)
h_w = h * w

plt.figure(figsize=(10, 4))
plt.stem(n, h, linefmt="b-", markerfmt="bo", basefmt=" ")
plt.stem(n, w, linefmt="g-", markerfmt="go", basefmt=" ")
plt.stem(n, h_w, linefmt="r-", markerfmt="ro", basefmt=" ")
plt.legend(["ИХ", "Окно Хэмминга", "ИХ с окном"])
plt.title("Применение оконной функции")
plt.grid()
plt.show()

# Задание 6: Частотная характеристика до и после окна
w1, H1 = freqz(h, worN=2048, fs=fs)
w2, H2 = freqz(h_w, worN=2048, fs=fs)

plt.figure(figsize=(10, 4))
plt.plot(w1, 20 * np.log10(np.abs(H1)), label="Без окна")
plt.plot(w2, 20 * np.log10(np.abs(H2)), label="С окном Хэмминга")
plt.axvline(2000, color="k", linestyle="--", label="fc = 2000 Гц")
plt.ylim(-100, 5)
plt.xlabel("Частота, Гц")
plt.ylabel("Амплитуда, дБ")
plt.title("ЧХ фильтра до и после оконной обработки")
plt.legend()
plt.grid()
plt.show()

# Задание 7: Фильтрация с оконной ИХ и спектр
y_w = np.convolve(s, h_w, mode="same")
Y_w = np.fft.fft(y_w)

plt.figure(figsize=(10, 4))
plt.plot(freq[: len(freq) // 2], np.abs(Y_w[: len(Y_w) // 2]))
plt.title("Спектр сигнала после ФВЧ с окном")
plt.xlabel("Частота, Гц")
plt.ylabel("|Y(f)|")
plt.grid()
plt.show()
