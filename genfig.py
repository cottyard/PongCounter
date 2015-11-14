from pylab import *
from scipy.io import wavfile


samp_freq, snd = wavfile.read('output.wav')
time_array = arange(0, float(snd.shape[0]), 1)
time_array /= samp_freq
time_array *= 1000
s1 = snd[:, 0]
plot(time_array, s1, color='k')
savefig('plot.png')
