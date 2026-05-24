def baca_kata(nama_file):
    kata_set = set()
    try:
        with open(nama_file, 'r') as f:
            for baris in f:
                kata_kata = baris.lower().split()
                for kata in kata_kata:
                    kata_bersih = kata.strip('.,!?;:"-()[]')
                    if kata_bersih:
                        kata_set.add(kata_bersih)
        return kata_set
    except FileNotFoundError:
        print(f'Error: File "{nama_file}" tidak ditemukan.')
        return None

file1 = input('Masukkan nama file pertama: ')
file2 = input('Masukkan nama file kedua: ')

set1 = baca_kata(file1)
set2 = baca_kata(file2)

if set1 is not None and set2 is not None:
    kata_bersama = set1 & set2
    print(f'\nKata-kata yang muncul pada kedua file:')
    for kata in sorted(kata_bersama):
        print(kata)
    print(f'\nTotal: {len(kata_bersama)} kata')
