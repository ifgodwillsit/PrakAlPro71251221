def cek_digit_belakang(a, b, c):
    keterangan = "True" if a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c % 10 else "False"
    return keterangan

a = int(input("Masukkan nilai pertama: "))
b = int(input("Masukkan nilai kedua: "))
c = int(input("Masukkan nilai ketiga: "))
print(cek_digit_belakang(a, b, c))