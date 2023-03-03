import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Limpa a janela de console
plt.clf()

# Configuração do sinal
nSeconds = 5
Fs = 44100
Ts = 1/Fs
t = np.arange(0, nSeconds, Ts)
f0 = 5000

# Grava o áudio
m = sd.rec(int(nSeconds*Fs), samplerate=Fs, channels=1)
sd.wait()

# Converte o áudio em um array NumPy unidimensional
m = m.ravel()

# Modulação em frequência
x = m * np.cos(2*np.pi*f0*t)

# Transformada de Fourier
X = np.fft.fft(x)

# Plotagem do espectro de frequência
plt.plot(np.fft.fftshift(20*np.log10(np.abs(X))))
plt.grid()
plt.show()

"""
Este código grava um sinal de áudio por 5 segundos e realiza
a modulação em frequência com uma portadora de 5 kHz. Em seguida,
é calculada a Transformada de Fourier do sinal modulado e o espectro 
de frequência é plotado.
"""