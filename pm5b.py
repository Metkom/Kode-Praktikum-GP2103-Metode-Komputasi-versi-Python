"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

a = int(input("Masukan angka : "))
b = int(input("Banyak kelipatan : "))
print("Kelipatan dari %d adalah" % a)
i = 1
while i <= b:
    print(i * a)
    if i % 10 == 0:
        print("\n")
    i = i + 1
