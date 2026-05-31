def jumlah_digit(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return (n % 10) + jumlah_digit(n // 10)

n = int(input('Masukkan bilangan: '))
print('Jumlah digit:', jumlah_digit(n))
