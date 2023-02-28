import pyaudio
import numpy as np

# Define o tamanho do bloco, taxa de amostragem e número de canais
chunk = 1024
sample_rate = 44100
channels = 1

# Inicializa o objeto Pyaudio
p = pyaudio.PyAudio()

# Abre um fluxo para gravar áudio
stream = p.open(format=pyaudio.paInt16,
                channels=channels,
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk)

# Inicia a gravação de áudio
print("\n\tGravando áudio...")
frames = []
for i in range(0, int(sample_rate / chunk * 5)):
    data = stream.read(chunk)
    frames.append(np.frombuffer(data, dtype=np.int16))

# Para a gravação de áudio
stream.stop_stream()
stream.close()
p.terminate()

# Converte o áudio gravado em uma matriz Numpy
audio = np.concatenate(frames)

# Processando o áudio gravado
# Salva o áudio em um arquivo
np.save("rec.npy", audio)

print("\n\tGravação de áudio concluída.")