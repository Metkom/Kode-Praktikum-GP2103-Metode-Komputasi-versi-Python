"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

a = int(input("Mulai angka : "))
b = int(input("Akhir angka : "))
if a % 2 == 0:
    a = a + 1
for i in range(a, b + 1):
    print(a)
    a = a + 2
    if a >= b:
        break
