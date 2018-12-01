"""
Modul Praktikum GP2103 Metode Komputasi,
Program Studi Teknik Geofisika, Universitas Pertamina
Oleh: Mohammad Heriyanto
Website: https://osf.io/h6d5w/
Link Kode: https://github.com/Metkom/Kode-Praktikum-GP2103-Metode-Komputasi-versi-Python
DOI: 10.17605/OSF.IO/H6D5W
@ Desember 2018
"""

kata = input("Masukkan kata Anda: ")
vokal = []
konsonan = []
index = 0
nvok = 0
nkon = 0
nspace = 0

while index < len(kata):
    if kata[index] == 'a' or kata[index] == 'A' \
            or kata[index] == 'I' or kata[index] == 'i' \
            or kata[index] == 'u' or kata[index] == 'U' \
            or kata[index] == 'E' or kata[index] == 'e' \
            or kata[index] == 'O' or kata[index] == 'o':
        vokal = vokal + [kata[index]]
        nvok = nvok + 1
    elif kata[index] == ' ':
        nspace = nspace + 1
    else:
        konsonan = konsonan + [kata[index]]
        nkon = nkon + 1
    index = index + 1
print('Vokal: ' + str(vokal))
print('Jumlah Vokal: ', nvok)
print('Konsonan :' + str(konsonan))
print('Jumlah Konsonan: ', nkon)
print('Jumlah Spasi: ', nspace)
