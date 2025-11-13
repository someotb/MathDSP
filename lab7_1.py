import numpy as np
from matplotlib import pyplot as plt

fc = 200 # Частота среза (Hz)
t_0 = 0.02 # Время задержки фильтра (c)
fs = 10000
h_0 = 1
t = np.linspace(0, 2 * t_0, fs)
w = np.linspace(-20000, 20000, 1)
wc = np.pi * 2 * fc

h_t = h_0 * 2 * fc * ((np.sin(wc * (t - t_0)))/(wc * (t - t_0)))

H_jw = np.sum(h_t * np.exp(-1j * w * t) * 1/fs)

plt.plot(t, h_t)
plt.show()