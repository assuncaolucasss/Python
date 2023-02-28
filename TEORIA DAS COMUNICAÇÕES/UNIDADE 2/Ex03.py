import numpy as np
import matplotlib.pyplot as plt

def estimate_pitch(audio, sample_rate):
    
    # Calcula a autocorrelação do sinal de áudio
    autocorr = np.correlate(audio, audio, mode="full")
    # Encontre o primeiro máximo local à direita do centro da autocorrelação
    center = len(autocorr) // 2
    right_half = autocorr[center:]
    max_index = np.argmax(right_half)
    # Estima o pitch como o recíproco do intervalo de tempo correspondente ao máximo local
    pitch_estimate = sample_rate / (center + max_index)
    return pitch_estimate

# Exemplo de uso
sample_rate = 44100
t = np.linspace(0, 1, sample_rate, False)
audio = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)
pitch_estimate = estimate_pitch(audio, sample_rate)

print("Pitch estimado: {:.2f} Hz".format(pitch_estimate))
autocorr = np.correlate(audio, audio, mode="full")
# Plot the audio signal and its autocorrelation
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, audio)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.subplot(2, 1, 2)
plt.plot(autocorr)
plt.xlabel("Atraso")
plt.ylabel("Autocorrelação")
plt.show()