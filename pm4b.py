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

X = np.genfromtxt('prak4a.txt')
Y = np.genfromtxt('prak4b.txt')
print(type(X))
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for row in X:
    for elem in row:
        print("%.2f" % elem, end=' ')
    print()
print(20 * '=')

np.savetxt('prak4oa.txt', result, fmt='%.0d %.2f %.3f')
