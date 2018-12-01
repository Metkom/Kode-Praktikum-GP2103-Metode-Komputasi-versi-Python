"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

# Matriks 1D
a = (1, 2, 3, 4)  # tuple
b = [1, 2, 3, 4]  # list
c = {1, 2, 3, 4}  # set

# Matriks 2D
V = [[1, 2, 1], [2, 1, 2]]
X = [[3, 2, 1], [1, 2, 3], [0, 2, 4]]
Y = [[1, 3], [2, 2], [3, 1]]
Z = [[2, 1, 3], [1, 2, 1], [3, 1, 2]]

print(V)
print(Z[1][1])

for row in X:
    for elem in row:
        print(elem, end=' ')
    print()
