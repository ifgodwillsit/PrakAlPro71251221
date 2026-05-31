def is_prima(n, i = 2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prima(n, i + 1)

n = int(input("Masukkan bilangan: "))
if is_prima(n):
    print(n, "adalah bilangan prima")
else:
    print(n, "bukan bilangan prima")