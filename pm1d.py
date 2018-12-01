"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

import sys

a = (1, 2, 3)  # tuples
b = (3, 4, 5)  # tuples

c = [1, 2, 3]  # list
d = [3, 4, 5]  # list

print('size a: ', sys.getsizeof(a))  # tuples
print('size c: ', sys.getsizeof(c))  # list

print('a[0]: ', a[0])  # memunculkan nilai urutan dari depan
print('c[-1]: ', c[-1])  # memunculkan nilai urutan dari belakang
print('a[1:3]: ', a[1:3])  # mengambil nilai urutan 1-2
print('c[1:3]: ', c[1:3])  # mengambil nilai urutan 1-2
print('c[1], c[-1]: ', c[1], c[-1])  # mengambil nilai lompatan
