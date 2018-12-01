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
from numpy import random as rd

Z1 = []
for i in range(10):
    Z1.append([i+1, rd.randint(1, 10)])
np.savetxt('orand1.txt', Z1, fmt='%d')

Z2 = []
for j in range(10):
    Z2.append([j+1, rd.randint(1, 10)])
np.savetxt('orand2.txt', Z2, fmt='%d')