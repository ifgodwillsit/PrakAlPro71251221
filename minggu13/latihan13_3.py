fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File tidak bisa dibuka:', fname)
    quit()

counts = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    jam = words[5].split(':')[0]
    counts[jam] = counts.get(jam, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((key, val))

lst.sort()

for jam, jumlah in lst:
    print(jam, jumlah)