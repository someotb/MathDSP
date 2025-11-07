from matplotlib import pyplot as plt
import numpy as np

T = 15
f1 = 1 / T
f2 = 3 / T
N = 10000
t = np.linspace(0, T, N)
dt = t[1] - t[0]

s1_t = np.sin(2 * np.pi * f1 * t)

for n in range(1, 10):
    for k in range(1, 10):
        sk_t = np.sin(2 * np.pi * k * f2 * t)
        sn_t = np.sin(2 * np.pi * n * f1 * t)
        ort = np.sum(sk_t * sn_t) * dt
        if abs(ort) > 1e-6 and k != n:
            print(f"k={k},\tn={n},\tИнтеграл = {ort:.2e}\tНарушение ортогональности!")
        else:
            print(f"k={k},\tn={n},\tИнтеграл = {ort:.2e}")