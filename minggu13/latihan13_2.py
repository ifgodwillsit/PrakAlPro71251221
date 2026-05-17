data = eval(input("Masukkan tuple (nama, nim, alamat): "))

nama, nim, alamat = data

print("Data  :", data)
print("NIM   :", nim)
print("NAMA  :", nama)
print("ALAMAT:", alamat)

nim_tuple = tuple(nim)
print("NIM          :", nim_tuple)

nama_depan = tuple(nama.split()[0])
print("NAMA DEPAN   :", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)