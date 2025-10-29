import numpy as np
import matplotlib.pyplot as plt

# Параметры
f = 1
T = 1/f  
t = np.linspace(0, 4*T, 1000) 

x1 = (4/np.pi) * np.cos(2*np.pi*f*t - np.pi/2)
x2 = (4/(3*np.pi)) * np.cos(2*np.pi*3*f*t - np.pi/2)
x_sum1 = x1 + x2

x_sum2 = np.zeros_like(t)
for n in range(1, 6):  # n от 1 до 5
    A_n = 4 / ((2*n - 1) * np.pi)
    freq_n = (2*n - 1) * f
    x_sum2 += A_n * np.cos(2*np.pi*freq_n*t - np.pi/2)

# Построение графиков
plt.figure(figsize=(12, 8))

# Первое 
plt.subplot(2, 1, 1)
plt.plot(t, x_sum1, 'b-', linewidth=2)
plt.title('x(t) = (4/π)cos(2πft - π/2) + (4/3π)cos(6πft - π/2)')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True)

# Второе 
plt.subplot(2, 1, 2)
plt.plot(t, x_sum2, 'r-', linewidth=2)
plt.title('x(t) = Σ [4/((2n-1)π)cos(2π(2n-1)ft - π/2)], n=1..5')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.tight_layout()
plt.show()