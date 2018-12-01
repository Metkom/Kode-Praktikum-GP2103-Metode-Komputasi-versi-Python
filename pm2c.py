"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

Y = [[1, 3], [2, 2], [3, 1]]

for row in Y:
    print(row)
print('\n')

rez = [[Y[j][i] for j in range(len(Y))] for i in range(len(Y[0]))]
for row in rez:
    print(row)
