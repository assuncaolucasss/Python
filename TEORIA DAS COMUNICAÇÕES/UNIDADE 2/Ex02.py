import numpy as np
pilot_length = 3
def remove_pilot(signal, pilot_length):
    
    # Estime o piloto usando autocorrelação
    pilot_estimate = np.correlate(signal, signal, mode="same")/pilot_length
    # Normaliza o piloto estimado
    pilot_estimate /= np.max(pilot_estimate)
    # Remove o piloto estimado do sinal
    signal_without_pilot = signal - pilot_estimate
    return signal_without_pilot

# Exemplo de uso
signal = np.array([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2])
pilot_length = 3
signal_without_pilot = remove_pilot(signal, pilot_length)

print("Sinal com Piloto: ", signal)
print("Sinal sem Piloto: ", signal_without_pilot)