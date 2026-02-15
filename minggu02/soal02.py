def fx(x) -> float:
    return 2 * x**3 + 2 * x + 15/x

x = int(input("Input nilai x: "))
hasil = fx(x)
print(f"Hasil formula f({x})= 2x^3 + 2x + 15/x adalah: {hasil:.1f}")

