from pylab import *
from scipy.io import wavfile

# samp_freq, snd = wavfile.read('output.wav')
# time_array = arange(0, float(snd.shape[0]), 1)
# time_array /= samp_freq
# time_array *= 1000
# s1 = snd[:, 0]
# plot(time_array, s1, color='k')
# savefig('plot.png')

sample_freq, snd = wavfile.read('output.wav')
snd_arr = snd[:,0]
max_amp = max(snd_arr)
min_amp = min(snd_arr)

def is_big(amp):
  return amp > max_amp / 3 or amp < min_amp / 3
#sampled = [snd_arr[i] for i in range(0, len(snd_arr), sf/1000)]

def big_sounds_timing(snd_arr):
  return [t for t,a in zip(range(0, len(snd_arr)), snd_arr) if is_big(a)]

def count_peaks(t_arr):
  gap = sample_freq / 100
  last_t = -gap - 1
  count = 0
  for t in t_arr:
    if t - last_t > gap:
      count += 1
    else:
      pass
    last_t = t
  return count

timings = big_sounds_timing(snd_arr)
print count_peaks(timings)
