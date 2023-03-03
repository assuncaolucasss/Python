import numpy as np
import matplotlib.pyplot as plt

n = 100
s = np.random.randn(n, 1)
h = np.ones((64, 1))
x = np.convolve(s.ravel(), h.ravel(), mode='full')
X = np.fft.fft(x)

plt.figure(figsize=(8, 6))
plt.subplot(311)
plt.plot(np.abs(X))
plt.title('Espectro de magnitude linear')
plt.subplot(312)
plt.plot(20 * np.log10(np.abs(X)))
plt.title('Espectro de magnitude em dB')
plt.subplot(313)
plt.plot(20 * np.log10(np.fft.fftshift(np.abs(X))))
plt.title('Espectro de magnitude simétrico em dB')
plt.tight_layout()
plt.show()

"""
Aqui, usamos as funções np.random.randn para gerar a sequência aleatória s e np.ones para gerar o filtro h. 
Em seguida, usamos a função np.convolve para realizar a convolução entre s e h e armazenar o resultado em x.
 A função np.fft.fft é usada para calcular a Transformada de Fourier de x, que é armazenada em X.

Para plotar os espectros de magnitude, usamos a biblioteca matplotlib e as funções plt.plot e plt.subplot para criar três subplots em uma figura.
A função plt.tight_layout é usada para ajustar o layout dos subplots para que eles fiquem bem espaçados. 
Finalmente, usamos a função plt.show para exibir a figura.
"""