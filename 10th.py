import wave
# open wave file for reading
wav_file = wave.open("example.wav", "r")
# get parameters of wave file
num_channels = wav_file.getnchannels()
sample_width = wav_file.getsampwidth()
sample_rate = wav_file.getframerate()
num_samples = wav_file.getnframes()
# close wave file
wav_file.close()
# print parameters
print("Number of channels: ", num_channels)
print("Sampling width (bit depth): ", sample_width)
print("Sampling rate: ", sample_rate)
print("Number of samples: ", num_samples)