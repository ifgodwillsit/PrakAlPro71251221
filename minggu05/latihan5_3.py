celcius = int(input("Input C = "))
fahrenheit = lambda celcius : (9 / 5) * celcius + 32
reamur = lambda celcius : 0.8 * celcius
print("Output F =", round(fahrenheit(celcius)))
print("Output R =", round(reamur(celcius)))