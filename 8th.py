import numpy as np
import matplotlib.pyplot as plt
# set parameters for sine wave
freq = 3 # frequency in Hz
amp = 1 # amplitude
phase = 0 # phase angle in radians
# generate time array with sampling rate of 2 Hz
t = np.arange(0, 10.5, 0.5)
# generate samples of sine wave
y = amp * np.sin(2 * np.pi * freq * t + phase)
# plot the samples
plt.plot(t, y, 'r-', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave with f = 3 Hz, 2 Hz Sampling Rate')
plt.grid()
plt.show()