"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

import matplotlib.pyplot as plt
from obspy import read

kompE = read("Komponen_E.miniseed")
kompN = read("Komponen_N.miniseed")
kompZ = read("Komponen_Z.miniseed")

dataE = kompE[0].data
t = range(1, len(dataE) + 1)
dataN = kompN[0].data
dataZ = kompZ[0].data

fig = plt.figure()
sp1 = plt.subplot(311)
sp1.plot(t, dataE)
sp1.set_xlim([0, len(dataE) + 1])

sp2 = plt.subplot(312)
sp2.plot(t, dataN)
sp2.set_xlim([0, len(dataN) + 1])
plt.ylabel('Amplitude')

sp3 = plt.subplot(313)
sp3.plot(t, dataZ)
sp3.set_xlim([0, len(dataZ) + 1])

fig.suptitle('Plot Data Seismogram')
plt.xlabel('Time')
plt.show()
