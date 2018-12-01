"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

fo = open("file4a.txt", "w")
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()

fo = open("file4a.txt", "r+")
str = fo.read(10)
print("Read string is : ", str)
fo.write("Write string again!!\n")
fo.close()