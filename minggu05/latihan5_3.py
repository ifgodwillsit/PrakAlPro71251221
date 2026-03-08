celcius = int(input("Input C = "))
fahrenheit = lambda celcius : (9 / 5) * celcius + 32
reamur = lambda celcius : 0.8 * celcius
keterangan = input("Mau diubah ke mana (Fahrenheit atau Reamur): ")
if keterangan == "Fahrenheit":
    print("Output F =", round(fahrenheit(celcius)))
elif keterangan == "Reamur":
    print("Output R =", round(reamur(celcius)))
else:
    print("Maaf, ketik Fahrenheit atau Reamur")
