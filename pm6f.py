"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares as ls

# Input origin data
data = np.genfromtxt('data6.txt')
x = data[:, 0]
y = data[:, 1]

# Plotting origin data
plt.plot(x, y, 'r*')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Mentah')
plt.show()


# Inverse Levenberg-Marquardt (LM)
def fungsi(m, x):
    return (m[0] - m[1] * x * x) / m[1] * m[1]


def pers(m, x, y):
    return fungsi(m, x) - y


# Initial model
a = 0.1
b = 0.1
m0 = np.array([a, b])
result = ls(pers, m0, method='lm', args=(x, y))

# Result
a = result.x[0]
b = result.x[1]
print('Nilai a: %f dan b: %f' % (a, b))
print('Error: %f' % result.optimality)

# Ploting result
m = np.array([a, b])
ynew = fungsi(m, x)
plt.plot(x, y, 'r*', label='Obs')
plt.plot(x, ynew, 'b', label='Cal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Data Mentah Vs Hasil Inversi')
plt.show()
