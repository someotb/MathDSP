import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# t = np.arange(-0.1, 0.1, Ts)
# s = 2 * np.cos(2 * np.pi * f * t)
# sc = np.cos(2 * np.pi * f * t)
# ss = np.sin(2 * np.pi * f * t)
# m1 = s * sc
# m2 = s * ss
# plt.plot(t, s, t, m1, t, m2)
# plt.ylim(-2,2)
# a1 = 1 / T * np.sum(m1) * Ts

# Начальные данные
f = 5
T = 1/f
w1 = (2 * np.pi) / T
Ts = 0.01
phase = np.pi/4
A = 5
t = np.linspace(0, T, 100, endpoint=False)

# Задайте гармоническое колебание x(t), выберите значение амплитуды, частоты, начальную фазу задайте равной 0
x = A * np.cos(2 * np.pi * f * t + phase)
plt.plot(t, x)
plt.show()

# Вычислите коэффициенты an и bn для n = 0,1,2,3,4. По полученным коэффициентам вычислите и постройте графики An, ϕ(n).
a = []
b = []
An = []
phi_n = []

for i in range(5):
    sc = np.cos(2 * np.pi * i * f * t)
    ss = np.sin(2 * np.pi * i * f * t)

    m1 = x * sc
    m2 = x * ss

    a_n = 2 / T * np.sum(m1) * Ts
    b_n = 2 / T * np.sum(m2) * Ts

    a.append(a_n)
    b.append(b_n)

An = np.sqrt(np.array(a)**2 + np.array(b)**2)
phi_n = np.arctan(-np.array(b) / np.array(a))

a[0] = a[0]/2

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.stem(range(5), An)
plt.title('Амплитуды An')
plt.xlabel('n')
plt.ylabel('An')

plt.subplot(1,2,2)
plt.stem(range(5), phi_n)
plt.title('Фазы phi_n')
plt.xlabel('n')
plt.ylabel('phi_n (рад)')

plt.tight_layout()
plt.show()