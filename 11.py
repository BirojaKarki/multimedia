import wave
import math
import numpy as np

# Define the parameters
frequency = 4400 # Hz
amplitude = 400 # m
phase = 0 # radians
duration = 1 # seconds
sample_rate = 44100 # Hz
sample_width=2
# Calculate the number of samples
num_samples = int(sample_rate * duration)
# Create a new wave file
with wave.open('sine_wave.wav', 'w') as file:
# Set the wave file parameters
 file.setnchannels(1) # mono
file.setsampwidth(2) # 2 bytes per sample
file.setframerate(sample_rate)
# Generate and write the samples
for i in range(num_samples):
# Calculate the sample value at the current time
 time = i / sample_rate
sample = amplitude * math.sin(2 * math.pi * frequency * time + phase)
# Convert the sample to a 2-byte integer
sample = int(sample * 32767)
sample_bytes = sample.to_bytes(2, byteorder='little', signed=True)
# Write the sample to the wave file
file.writeframes(sample_bytes)