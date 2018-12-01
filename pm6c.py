"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

import math as mt


# fungsi pendukung
def v(r):
    vol = 4.0 / 3.0 * mt.pi * r ** 3
    return vol


# fungsi utama
volume = v(2)
print(volume)
