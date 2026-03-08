def cek_parameter(a, b, c):
    print("True" if a != b != c or a + b == c or a + c == b or b + c == a else "False")

a = int(input("Masukkan nilai pertama: "))
b = int(input("Masukkan nilai kedua: "))
c = int(input("Masukkan nilai ketiga: "))
cek_parameter(a, b, c)