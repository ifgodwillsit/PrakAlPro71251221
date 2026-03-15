def ganjil(bawah, atas):
    if bawah <= atas:
        start = bawah if bawah % 2 != 0 else bawah + 1
        for i in range(start, atas + 1, 2):
            print(i, end=" ")
    else:
        start = bawah if bawah % 2 != 0 else bawah - 1
        for i in range(start, atas - 1, -2):
            print(i, end=" ")
    
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)