fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except FileNotFoundError:
    print("File tidak bisa dibuka :", fname)
    exit()

counts = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)