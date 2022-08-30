import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as manimation
import wave

from matplotlib.ticker import FuncFormatter
from scipy.io import wavfile

#FilePath = '220708 STW to TW to STW/'
FileName = 'CKT to STW'
FileFormat = '.wav'

samplerate, data = wavfile.read( FileName + FileFormat)

print("The sample rate is: " + str(samplerate) + " samples per second. ")
print("There are " + str(len(data)) + " samples. ")
print("Then the audio should last: " + str(len(data) / samplerate) + " seconds. ")

plt.plot(data)
plt.show()
#def kilo(x, pos):
#    return '%1.fk' % (x*1e-3)
dt = 0.0005
t = np.arange(0,10,dt)
s1 = np.sin(2 * np.pi * 500 * t)
s2 = np.cos(2 * np.pi * 700 * t)

s2[t <= 2] = s2[6 <= t] = 0

nse = 0.01 * np.random.random(size=len(t))

#x = s1 + s2 + nse
#NFFT = 512
#Fs = 


