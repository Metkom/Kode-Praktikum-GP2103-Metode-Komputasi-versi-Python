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
# Read data
data = np.genfromtxt('prak4c.txt')
Ld = len(data)
Log = data[1:Ld, 0]
Lat = data[1:Ld, 1]
Elev = data[1:Ld, 2]
Rawgrav = data[1:Ld, 3]
# Operate data
PG = ((Rawgrav - 1500) + 1530.844) * 1.00043726
KUB = 0.03068 * Elev
RE = sum(Elev) / len(Elev)
SDRE = Elev - RE
# Save data
LL = len(Log)
data_final = [Log, Lat, Elev, Rawgrav, PG, KUB, SDRE]
data_final = np.transpose(data_final)
print(data_final)
np.savetxt('prak4ob.txt', data_final, fmt='%.2f')
