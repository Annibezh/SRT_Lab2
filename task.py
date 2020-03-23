import numpy as np
import random
from math import sin
import matplotlib.pyplot as plt
import time

# count = 10
# autocor = 0
# cov = 0
# time_rxx = 0
# time_rxy = 0


n = 10  # harmonics
w = 900 # max frequency
N = 1000  # number of discrete signals

# for cc in range(count):
temp = w / (n - 1)
# Frequency
def W(n, w):
    return w - n * temp
# Expected value
def Mx(signal, N):
    return sum(signal) / N
# Dispersion
def Dx(signal, mx, N):
    return sum((signal - mx) ** 2) / N
def Rxx(x, mx, N):
    R = np.zeros(int(N/2) - 1)
    for T in range(int(N/2) - 1):
        for t in range(int(N/2) - 1):
            R[T] = ((x[t] - mx) * (x[t + T] - mx))
    return np.sum(R)/(N-1)
w_val = [W(n, w) for n in range(n)]
harmonics = np.empty(N)
# Harmonics generating
for n in range(n):
    A = random.randint(-10, 10)
    phi = random.randint(-360, 360)
    for t in range(N):
        harmonics[t] += A * sin(w_val[n] * t + phi)
plt.figure(figsize=(10, 5))
plt.plot(harmonics, 'g')
plt.grid(True)
plt.show()
mx = Mx(harmonics, N)
start = time.perf_counter()
autocor = Rxx(harmonics, mx, N)

time_rxx = time.perf_counter() - start

# Signal Y
y = np.empty(N)
for n in range(n):
    A = random.randint(-10, 10)
    phi = random.randint(-360, 360)
    for t in range(N):
        y[t] += A * sin(w_val[n] * t + phi)
plt.figure(figsize=(10, 5))
plt.plot(y)
plt.grid(True)
plt.show()
Rxy = np.zeros(int(N/2) - 1)
for T in range(int(N/2) - 1):
    for t in range(int(N/2) - 1):
        Rxy[T] = ((harmonics[t] - mx) * (y[t + T] - Mx(y, N))) / (N-1)
plt.figure(figsize=(10, 5))
plt.plot(Rxy, 'r')
plt.grid(True)
plt.show()
def Rxy(x, y, N):
    R = np.zeros(int(N/2) - 1)
    for T in range(int(N/2) - 1):
        for t in range(int(N/2) - 1):
            R[T] = ((x[t] - Mx(x, N)) * (y[t + T] - Mx(y, N)))
    return np.sum(R)/(N-1)
start = time.perf_counter()
cov = Rxy(harmonics, y, N)

time_rxy = time.perf_counter() - start

f = open(r"result_1000.txt", "w")
f.write(f"Rxx = {str(autocor)}\n")
f.write(f"Rxy = {str(cov)}\n")
f.write(f"Time Rxx = {str(time_rxx)}\n")
f.write(f"Time Rxy = {str(time_rxy)}\n")