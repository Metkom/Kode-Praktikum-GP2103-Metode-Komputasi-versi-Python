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
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
data = np.genfromtxt('gravity.txt')
x = data[:, 0]
y = data[:, 1]
cba = data[:, 2]

xm, ym = np.meshgrid(x, y)
cbam = griddata((x, y), cba, (xm, ym), method='linear')
CS = plt.contourf(xm, ym, cbam)
plt.colorbar()
plt.scatter(x, y, marker='o', s=5, zorder=10)
plt.title('Plot Data Gravity')
plt.xlabel('Easting (km)')
plt.ylabel('Northing (km)')
plt.xlim(0, max(x))
plt.ylim(0, max(y))
plt.show()
