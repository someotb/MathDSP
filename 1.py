import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
A = 5   
f = 5    
ph = 0   

x = A * np.sin(2 * np.pi * f * t + ph)

plt.figure(figsize=(12, 8))
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title(f'A={A}V, F={f}Hz, φ={ph}°')
plt.grid(True)
plt.tight_layout()
plt.show()