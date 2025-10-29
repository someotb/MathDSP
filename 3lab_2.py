import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
T = 1.0
tau = 0.2
Ts = 0.001
t = np.arange(0, T, Ts)

x = np.where(t < tau, 1.0, 0.0)

a = []
b = []

plt.plot(t, x)
plt.show()

r = range(7)
for i in r:
    xc = np.cos(2 * np.pi * i * t/T)
    xs = np.sin(2 * np.pi * i * t/T)

    m1 = x * xc
    m2 = x * xs

    a_n = 2 / T * np.sum(m1) * Ts
    b_n = 2 / T * np.sum(m2) * Ts

    a.append(a_n)
    b.append(b_n)

a[0] = a[0]/2

An = np.sqrt(np.array(a)**2 + np.array(b)**2)
phi = -np.arctan(np.array(b)/np.array(a))

plt.subplot(1,2,1)
plt.stem(range(7), An)
plt.title('Амплитуды An')
plt.xlabel('n')
plt.ylabel('An')

plt.subplot(1,2,2)
plt.stem(range(7), phi)
plt.title('Фазы phi')
plt.xlabel('n')
plt.ylabel('phi')

plt.tight_layout()
plt.show()