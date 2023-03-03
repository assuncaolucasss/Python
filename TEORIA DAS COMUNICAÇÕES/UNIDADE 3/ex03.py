import numpy as np
import matplotlib.pyplot as plt
import pyaudio

# Limpar a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definir tempo de gravação e frequência de amostragem
nSeconds = 5
Fs = 44100

# Configurar o objeto PyAudio para gravação de áudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=Fs, input=True, frames_per_buffer=1024)

# Gravar áudio
print("Gravando...")
frames = []
for i in range(0, int(Fs / 1024 * nSeconds)):
    data = stream.read(1024)
    frames.append(data)
print("Gravação concluída.")

# Parar a gravação e fechar o objeto PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Converter os dados de áudio gravados em um array NumPy
data = b''.join(frames)
m = np.frombuffer(data, dtype=np.int16)

# Aplicar Transformada de Fourier em m para obter o espectro de magnitude
M = np.fft.fft(m)

# Plotar o espectro de magnitude
plt.plot(np.fft.fftshift(20*np.log10(np.abs(M))))
plt.grid(True)
plt.show()

"""
Nesta versão do código em Python, usamos a biblioteca PyAudio para configurar o
 objeto de stream de áudio e gravar o áudio em uma lista frames. Em seguida, usamos
   a função np.frombuffer para converter os dados de áudio em um array NumPy m. Finalmente,
     aplicamos a Transformada de Fourier em m para obter o espectro de magnitude M e usamos a 
     função plt.plot para plotar o espectro de magnitude em dB, com o eixo x ajustado para que as
       frequências sejam simétricas. A função plt.grid é usada para adicionar linhas de grade
         ao gráfico, e a função plt.show é usada para exibir o gráfico.
"""