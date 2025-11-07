from matplotlib import pyplot as plt
import numpy as np

res = []
t = np.arange(0,4.1,0.25)

for n in t:
    res_t = ((4 * np.sin(np.pi * n)) / np.pi)
    res.append(res_t)
    print(f"t = {n:4.2f} → res = {res_t:8.5f}")

plt.plot(t, res)
plt.show()
# Код просто для того чтобы быстро посчитать все значения