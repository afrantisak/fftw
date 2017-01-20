import pdb
import numpy
from scipy.fftpack import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt

fs, data = wavfile.read('test.wav')

def split(data, denominator):
    length = len(data)
    div, rem = divmod(length, denominator)
    data = data[:-rem]
    return numpy.split(data, denominator)

windows = split(data, 8)
print len(data)
for w in windows:
    print len(w)


a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)
plt.plot(abs(c[:(d-1)]),'r') 
plt.show()
