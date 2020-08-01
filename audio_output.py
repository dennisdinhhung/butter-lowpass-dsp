import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
from matplotlib import pyplot as plt

(freq, sample) = read('input.wav')
len(sample)

fourier = sp.fft.fft(sample)
scale = np.linspace(0, freq, len(sample))

noise = np.random.rand(len(fourier))

noise_sample = noise + sample

b,a = signal.butter(5, 1500/(freq/2), btype='lowpass')

filter2 = signal.lfilter(b,a,noise_sample)

write("output1500.wav", freq, filter2)

