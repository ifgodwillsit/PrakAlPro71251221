lamaKerja = 5
gajiPerjam = int(input("Gaji perjam yang Budi inginkan: Rp."))
jamKerja = int(input("Jam kerja rata-rata Budi perminggu: "))

gajiKotor = gajiPerjam * jamKerja * lamaKerja
print("Gaji Budi selama libur panas sebelum dipotong pajak: Rp.", gajiKotor)

gajiMinPajak = gajiKotor - (gajiKotor * 14 / 100)
print("Gaji Budi selama libur panas setelah dipotong pajak: Rp.", gajiMinPajak)

clothing = gajiMinPajak * 10 / 100
print("Pengeluaran Budi untuk pakaian dan aksesoris: Rp.", clothing)

stationer = gajiMinPajak * 1 / 100
print("Pengeluaran Budi untuk alat tulis: Rp.", stationer)

gajiMinPengeluaran = gajiMinPajak - clothing - stationer
sedekah = gajiMinPengeluaran * 25 / 100
print("Uang yang Budi sedekahkan: Rp.", sedekah)

yatim = sedekah * 30 / 100
print("Sedekah yang diterima anak yatim: Rp.", yatim)

dhuafa = sedekah * 70 / 100
print("Sedekah yang diterima dhuafa: Rp.", dhuafa)

