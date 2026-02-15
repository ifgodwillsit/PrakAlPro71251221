def hitung_bb(bmi, tinggi) -> float:
    return(bmi * tinggi**2)

bmi = float(input("Masukkan bmi: "))
tinggi = float(input("Masukkan tinggi badan dalam m: "))

beratBadan = hitung_bb(bmi, tinggi)
print(f"Berat badan anda adalah: {beratBadan:.1f} kg")

