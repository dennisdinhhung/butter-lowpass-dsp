import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
from matplotlib import pyplot as plt

(freq, sample) = read('input.wav')

plt.subplot(221)
plt.plot(sample)
plt.title('input.wav')
plt.xlabel('Hz')
plt.ylabel('Amplitude')

fourier = sp.fft.fft(sample)
scale = np.linspace(0, freq, len(sample))

plt.subplot(222)
plt.stem(scale[0:5000], np.abs(fourier[0:5000]), 'r')
plt.title('Signal spectrum after FFT')
plt.xlabel('Hz')
plt.ylabel('Amplitude')

noise = np.random.rand(len(fourier))

noise_sample = noise + sample

write("input_with_noise.wav", freq, noise_sample)

b,a = signal.butter(5, 1250/(freq/2), btype='lowpass', analog=True)

filtered = signal.lfilter(b,a,noise_sample)
plt.subplot(223)
plt.plot(filtered)
plt.title('Lowpass Filtered')
plt.xlabel('Hz')
plt.ylabel('Amplitude')

write("output.wav", freq, filtered)

plt.show()