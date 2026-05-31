def deret_ganjil(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + deret_ganjil(n - 1)

n = int(input('Masukkan jumlah suku (n): '))
print('Jumlah deret ganjil:', deret_ganjil(n))
