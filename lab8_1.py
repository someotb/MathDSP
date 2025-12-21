import matplotlib.pyplot as plt
import numpy as np

fc1 = 5  # Гц
fs1 = fc1 * 100  # 500 Гц
t1 = np.arange(0, 0.1, 1 / fs1)  # 0.1 сек -> 50 отсчётов
s1 = np.cos(2 * np.pi * fc1 * t1)

fc2 = fc1 * 2  # 10 Гц
fs2 = fc2 * 100  # 1000 Гц
t2 = np.arange(0, 0.1, 1 / fs2)  # 0.1 сек -> 100 отсчётов
s2 = np.cos(2 * np.pi * fc2 * t2)

plt.figure(figsize=(10, 3))
plt.stem(t1, s1, linefmt="C0-", markerfmt="C0o", basefmt=" ", label="5 Гц, fs=500 Гц")
plt.stem(
    t2[::2],
    s2[::2],
    linefmt="C1--",
    markerfmt="C1s",
    basefmt=" ",
    label="10 Гц, fs=1000 Гц (каждый 2-й отсчёт)",
)
plt.xlabel("Время t (с)")
plt.ylabel("Амплитуда")
plt.title("Сравнение сигналов по времени")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

N = min(len(s1), len(s2))
n = np.arange(N)

x1 = s1[:N]
x2 = s2[:N]

max_diff = np.max(np.abs(x1 - x2))
print(f"Максимальная разница между x1[n] и x2[n]: {max_diff:.2e}")

plt.figure(figsize=(10, 3))
plt.stem(n, x1, linefmt="C0-", markerfmt="C0o", basefmt=" ", label="Сигнал 1 (5 Гц)")
plt.stem(n, x2, linefmt="C1--", markerfmt="C1s", basefmt=" ", label="Сигнал 2 (10 Гц)")
plt.xlabel("Номер отсчёта n")
plt.ylabel("x[n]")
plt.title("Сравнение по номеру отсчёта n (должны совпадать)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
