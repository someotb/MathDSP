import numpy as np
from matplotlib import pyplot as plt

fc = 1000 # Частота среза (Hz)
t_0 = 0.03 # Время задержки фильтра (c)
fs = 10000
h_0 = 1
t = np.linspace(0, 2 * t_0, fs)
w_massive = np.linspace(-20000, 20000, 500)
wc = np.pi * 2 * fc
H_jw_massive = []
ampl = []
phase = []

h_t = h_0 * 2 * fc * ((np.sin(wc * (t - t_0)))/(wc * (t - t_0)))

for w in w_massive:
    H_jw = np.sum(h_t * np.exp(-1j * w * t) * 1/fs)
    H_jw_massive.append(H_jw)
    ampl.append(abs(H_jw))
    phase.append(np.angle(H_jw))

plt.subplot(2,1,1)
plt.plot(w_massive, ampl)
plt.title("АЧХ")

plt.subplot(2,1,2)
plt.plot(w_massive, phase)
plt.title("ФЧХ")

plt.tight_layout()
plt.show()