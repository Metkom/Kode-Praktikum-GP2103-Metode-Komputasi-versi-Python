"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""


# fungsi pendukung
def fmin(val):
    min = val[0]
    for i in range(1, len(val)):
        if val[i] < min:
            min = val[i]
    return min


# fungsi utama
nilai = [5, 9, 4, 2, 9, 7, 1, 8, 10, 5]
minimum = fmin(nilai)
print(minimum)
