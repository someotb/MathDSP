from matplotlib import pyplot as plt
import numpy as np

tau = 1.0 # Длительность импульса
N = 1000
t = np.linspace(-2 * tau, 2 * tau, N)
dt = t[1] - t[0]

x = np.zeros_like(t)
x[np.abs(t) <= tau] = 1.0

plt.plot(t, x)
plt.grid(True)
plt.show()

freq = np.linspace(0, 3 / tau, N)
res = []
for f in freq:
    s = np.sum(x * np.exp(-2j * np.pi * f * t)) * dt
    res.append(s)
    
res = np.array(res)

ampl = np.abs(res)
phase = np.angle(res)

plt.subplot(2,1,1)
plt.plot(freq,ampl)
plt.xlabel("Частоты")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(freq,phase)
plt.xlabel("Частоты")
plt.ylabel("Фаза")
plt.grid(True)
plt.tight_layout()

plt.show()