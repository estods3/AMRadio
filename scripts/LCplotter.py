import matplotlib.pyplot as plt
import numpy as np

## Design
samples = 100
min_L_in_uH = 150
max_L_in_uH = 400
min_C_in_pF = 50
max_C_in_pF = 250

## Model
L = np.linspace(min_L_in_uH*(10**(-6)),  max_L_in_uH*(10**(-6)),  samples)
C = np.linspace(min_C_in_pF*(10**(-12)), max_C_in_pF*(10**(-12)), samples)
L.shape = (samples, 1)
C.shape = (1, samples)
freq_in_Hz = 1.0 / (2.0 * 3.1415926535 * np.sqrt(L*C))

freq_in_kHz = freq_in_Hz / 1000.0
freq_in_kHz = np.flipud(freq_in_kHz)
## Display

axis_labels = [min_C_in_pF, max_C_in_pF, min_L_in_uH, max_L_in_uH]
print(axis_labels)
plt.imshow(freq_in_kHz, cmap='jet', extent=axis_labels)
plt.xlabel('Capacitance (pF)')
plt.ylabel('Inductance (uH)')
plt.title('Resonance Frequency (kHz) for Inductance and Capacitance') 
plt.colorbar()
plt.show()
