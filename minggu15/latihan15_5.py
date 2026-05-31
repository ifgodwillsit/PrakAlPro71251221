def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return faktorial(n - 1) * n

def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

n = int(input('Masukkan nilai n: '))
r = int(input('Masukkan nilai r: '))
print('C(' + str(n) + ',' + str(r) + ') =', kombinasi(n, r))
