"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

V = [[1, 2, 1], [2, 1, 2]]
Z = [[2, 1, 3], [1, 2, 1], [3, 1, 2]]

VxZ = [[0, 0, 0], [0, 0, 0]]

for i in range(len(V)):
    for j in range(len(Z[0])):
        for k in range(len(Z)):
            VxZ[i][j] += V[i][k] * Z[k][j]

for r in VxZ:
    print(r)
