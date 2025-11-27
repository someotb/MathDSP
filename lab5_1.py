from matplotlib import pyplot as plt
import numpy as np

def s1(t):
    return np.where((t >= 0) & (t <= 1), 1, 0)

def s2(tau):
    return s1(tau)
    
tau = np.linspace(-5, 5, 1000)

# График функции s1(-tau)
plt.figure()
plt.plot(tau, s1(-tau), label='s1(-tau)')
plt.plot(tau, s1(tau), label='s1(tau)')
plt.legend()
plt.title("Сигнал s1(+/-tau)")
plt.grid(True)
plt.tight_layout()

# График s1(t - tau)
plt.figure()
t_values = [-1, 0, 2]
for t in t_values:
    plt.plot(tau, s1(t - tau), label=f's1({t} - tau)')
plt.legend()
plt.title("Сигнал s1(t - tau)")
plt.grid(True)
plt.tight_layout()

# Произведение функций s2(tau)s1(t - tau)
plt.figure()
for t in t_values:
    result = s2(tau) * s1(t - tau)
    plt.plot(tau, result, label=f's2(tau)s1({t} - tau)')
plt.legend()
plt.title(f"Произведение функций s2(tau)s1({t_values} - tau)")
plt.grid(True)
plt.tight_layout()

# Вычислим интеграл для значения t = 0.2
dt = tau[1] - tau[0]
t_val = 0.2
integral1 = np.sum(s2(tau) * s1(t_val - tau)) * dt
print(f"Значение интеграла при t = {t_val}: {integral1}")

# Вычислим интеграл для диапазона значений t
t_values2 = np.linspace(-1, 2, 200)
integral2 = []

for t in t_values2:
    conv = np.sum(s2(tau) * s1(t - tau)) * dt
    integral2.append(conv)

plt.figure()
plt.plot(t_values2, integral2, label='Интеграл свертки s2(tau)s1(t - tau)')
plt.title("Свёртка s1 * s2")
plt.grid(True)
plt.tight_layout()
plt.show()