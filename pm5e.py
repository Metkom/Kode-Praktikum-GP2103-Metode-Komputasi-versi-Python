"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

a = 1
y = " "
while a <= 10:
    print("Kesempatan ke-", a)
    for b in range(0, 10):
        y = input("\tApakah anda ingin skip ? (y/t) ")
        if y == "y":
            break
        print("\tPermainan ke-", b)
    else:
        print("Else FOR")

    a += 1
    y = input("Apakah anda ingin keluar ? (y/t) ")
    if y == "y":
        break
else:
    print("Else WHILE")
