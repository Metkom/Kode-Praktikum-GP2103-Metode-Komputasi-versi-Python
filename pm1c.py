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
import math as mt

a = 30.56*(np.pi/180)

print('Isi fungsi numpy: ', dir(np))
print('Isi fungsi math: ', dir(mt))

print('sin(a): ', np.sin(a))
print('sin(a): ', mt.sin(a))

print('tan(a): ', mt.tan(a))
print('log(a): ', mt.log(a))
print('exp(a): ', mt.exp(a))
print('sqrt(a): ', mt.sqrt(a))

print('Pembulatan round dari a: ', round(a, 1))
print('Pembulatan floor dari a: ', mt.floor(a))
print('Pembulatan ceil dari a: ', mt.ceil(a))
