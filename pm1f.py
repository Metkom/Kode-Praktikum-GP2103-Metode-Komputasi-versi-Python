"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = int(input("x: "))

y1 = a*x**3
y2 = b*x**2
y3 = c*x
y = y1 + y2 + y3
print('y : ', y)
