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

t = 10
z1 = 50
z2 = 150
x0 = 100
rho = 1
x = np.arange(-500, 500, 20)
G = 6.67 * 10e-11
v = 2 * G * rho * t
g = []
for i in range(0, len(x)):
    g.append(np.pi + (np.arctan((x[i] - x0) / z1)) -
             (np.arctan((x[i] - x0) / z2)))

gg = v*np.array(g)

plt.subplot(311)
plt.plot(x, gg, '*r')
plt.xlim(min(x), max(x))
plt.ylabel('Delta g (mGal)')
plt.title('Modeling Gravity - Patahan')

fig = plt.subplot(313)
x1 = [-500, -500, x0, x0]
y1 = [z2, z2 - t, z2 - t, z2]
fig.fill(x1, y1, 'r')
x2 = [x0, x0, 500, 500]
y2 = [z1, z1 - t, z1 - t, z1]
fig.fill(x2, y2, 'r')
plt.xlim(min(x), max(x))
plt.ylim(0, z2+50)
plt.gca().invert_yaxis()
plt.ylabel('Depth (m)')
plt.xlabel('Position (m)')
plt.show()
