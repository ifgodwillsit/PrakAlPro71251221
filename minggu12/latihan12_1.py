dictionary = {}

n = int(input("Masukkan jumlah data: "))
for i in range(n):
    key = int(input(f"  Key ke-{i+1}   : "))
    value = int(input(f"  Value ke-{i+1} : "))
    dictionary[key] = value

print("\nDictionary :", dictionary)
print()
print(f"{'key':<10} {'value':<10} {'item':<10}")

item_num = 1
for key, value in dictionary.items():
    print(f"{key:<10} {value:<10} {item_num:<10}")
    item_num += 1