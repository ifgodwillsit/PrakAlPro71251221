n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}
for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    jumlah = int(input(f"Berapa jumlah aplikasi di kategori {nama_kategori}: "))
    aplikasi = []
    for j in range(jumlah):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = set(aplikasi)

daftar_set = list(data_aplikasi.values())

hanya_satu = set()
for i in range(len(daftar_set)):
    gabungan_lain = set()
    for j in range(len(daftar_set)):
        if i != j:
            gabungan_lain = gabungan_lain | daftar_set[j]
    hanya_satu = hanya_satu | (daftar_set[i] - gabungan_lain)
print('Aplikasi yang hanya muncul di satu kategori:', hanya_satu)

if n > 2:
    tepat_dua = set()
    for i in range(len(daftar_set)):
        for j in range(i + 1, len(daftar_set)):
            irisan = daftar_set[i] & daftar_set[j]
            for k in range(len(daftar_set)):
                if k != i and k != j:
                    irisan = irisan - daftar_set[k]
            tepat_dua = tepat_dua | irisan
    print('Aplikasi yang muncul tepat di dua kategori:', tepat_dua)
