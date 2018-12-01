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

orand1 = np.genfromtxt('orand1.txt')
orand2 = np.genfromtxt('orand2.txt')
result = []
m = 0
print('No\tOrand1\tNo\tOrand2')
for i in range(len(orand1)):
    for j in range(len(orand2)):
        cek = int(orand1[i, 1]) - int(orand2[j, 1])
        if cek == 0:
            result.append([orand1[i, 0], orand1[i, 1],
                           orand2[j, 0], orand2[j, 1]])
            print(orand1[i, 0], '\t', orand1[i, 1], '\t',
                  orand2[j, 0], '\t', orand2[j, 1])
            m = m + 1
np.savetxt('ofileCompare.txt', result, fmt='%d')
print('Data yang sama sebanyak: ',m)
