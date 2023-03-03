import numpy as np

N = 6

x = np.random.randn(N, 1)

A = np.fft.fft(np.eye(N))

X = np.fft.fft(x, axis=0)
X_mtx = A @ x

x_inv = np.fft.ifft(X, axis=0)
x_inv_mtx = np.linalg.inv(A) @ X_mtx

print(x_inv)
print(x_inv_mtx)

"""
Aqui, np.random.randn é usado para gerar uma matriz de números aleatórios de tamanho (N,1), enquanto np.eye é usado para criar a matriz de transformação discreta de Fourier (DFT) A.

As funções np.fft.fft e np.fft.ifft são usadas para realizar a transformada de Fourier e a transformada inversa de Fourier, respectivamente. A multiplicação de matrizes é realizada usando o operador @, e a função np.linalg.inv é usada para calcular a matriz inversa de A.

"""
