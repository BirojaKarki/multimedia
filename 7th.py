import numpy as np
import matplotlib.pyplot as plt
# set parameters for sine wave
freq = 3 # frequency in Hz
amp = 1 # amplitude
phase = 0 # phase angle in radians
# generate time array
t = np.arange(0, 3.1, 0.3)
# generate samples of sine wave
y = amp * np.sin(2 * np.pi * freq * t + phase)
# plot the samples against time
plt.plot(t, y, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('10 Samples of Sine Wave with f = 3 Hz')
plt.grid()
plt.show()