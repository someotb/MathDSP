import numpy as np
from matplotlib import pyplot as plt

f = 2
Ts = 0.4 
fs = 1 / Ts
t_analog = np.linspace(0,4,10000)
t_Ts = np.arange(0, 4 + Ts, Ts)

s_analog = np.cos(2 * np.pi * f * t_analog)
s_Ts = np.cos(2 * np.pi * f * t_Ts)

N_s = len(s_Ts)
S_t_sum = np.zeros_like(t_analog)
s = []

for n in range(N_s):
    S_t_sum += s_Ts[n] * np.sinc(fs * (t_analog - t_Ts[n]))


plt.plot(t_analog, s_analog)
plt.stem(t_Ts, s_Ts, linefmt = 'r')
plt.title("Непрерывный сигнал и его дискретные отчеты")
plt.show()
plt.plot(t_analog, S_t_sum)
plt.stem(t_Ts, s_Ts, linefmt = 'r')
plt.title("Восстановленные сигнал и его оцифрованная версия")
plt.show()

