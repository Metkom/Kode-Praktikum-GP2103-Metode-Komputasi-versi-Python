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
X = [[3, 2, 1], [1, 2, 3], [0, 2, 4]]
Z = [[2, 1, 3], [1, 2, 1], [3, 1, 2]]
XpZ = np.mat(X) + np.mat(Z)
print(XpZ)
print(20 * '=')
XmZ = np.mat(X) - np.mat(Z)
print(XmZ)
print(20 * '=')
XxZ = np.mat(X) * np.mat(Z)
print(XxZ)
