"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

a = float(input('Masukkan nilai a: '))
if a % 2 == 0:
    print('a adalah bilangan genap')
elif a % 2 == 1:
    print('a adalah bilangan ganjil')
else:
    print('a adalah bilangan desimal')
