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
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, np.pi / 100)
y1 = np.sin(x)
y2 = np.sin(x + np.pi)
plt.plot(x, y1, '--r', label='sin(x)')
plt.plot(x, y2, '+b', label='sin(x+pi)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot Data')
plt.grid()
plt.legend()
plt.tick_params(axis='both', labelcolor='tab:orange')
plt.show()
