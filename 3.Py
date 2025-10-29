import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
A1, A2, A3 = 1.5, 1, 2   
f = 2  
phi1, phi2, phi3 = np.radians(90), np.radians(45), np.radians(60)

x1 = A1 * np.sin(2 * np.pi * f * t + phi1)
x2 = A2 * np.sin(2 * np.pi * f * t + phi2)
x3 = A3 * np.sin(2 * np.pi * f * t + phi3)
x_sum = x1 + x2 + x3

A_total = np.max(x_sum)  
first_max_index = np.argmax(x_sum)
t_max = t[first_max_index]
phi_total = -2 * np.pi * f * t_max  
print("Параметры суммарного колебания:")
print(f"Амплитуда: A = {A_total:.3f}")
print(f"Начальная фаза: φ = {np.degrees(phi_total):.1f}°")

plt.plot(t, x_sum, 'r-', linewidth=2)
plt.title('Суммарное колебание')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()