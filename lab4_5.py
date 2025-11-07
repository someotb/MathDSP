from matplotlib import pyplot as plt
import numpy as np

tau = 0.5
N = 1000
t = np.linspace(-2 * tau, 2 * tau, N)
dt = t[1] - t[0]
x = np.zeros_like(t)
f = 200
x[np.abs(t) <= tau / 2] = 1.0
y = np.cos(2 * np.pi * f * t)

plt.plot(t, x)
plt.show()

freq = np.linspace(0, 3 / tau, N)
res = []
for f in freq:
    s = np.sum(x * np.exp(-2j * np.pi * f * t)) * dt
    res.append(s)

res = np.array(res)

y_res = res * y

ampl = np.abs(y_res)
phase = np.angle(y_res)

plt.subplot(2,1,1)
plt.plot(freq, ampl)
plt.xlabel("Частота")
plt.ylabel("Амлитуда")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(freq, phase)
plt.xlabel("Частота")
plt.ylabel("Фаза")
plt.grid(True)
plt.tight_layout()
plt.show()