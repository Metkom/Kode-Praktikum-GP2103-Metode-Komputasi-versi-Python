"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

X = [[3, 2, 1], [1, 2, 3], [0, 2, 4]]
Z = [[2, 1, 3], [1, 2, 1], [3, 1, 2]]

print('X + Z = ')
for row in range(0, len(X)):
    for col in range(0, len(X[0])):
        print(X[row][col] + Z[row][col], end=' ')
    print()

print('X - Z = ')
for row in range(0, len(X)):
    for col in range(0, len(X[0])):
        print(X[row][col] - Z[row][col], end=' ')
    print()
