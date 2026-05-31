def is_palindrom(kalimat):
    kalimat = kalimat.replace(' ', '').lower()
    if len(kalimat) <= 1:
        return True
    if kalimat[0] != kalimat[-1]:
        return False
    return is_palindrom(kalimat[1:-1])

kalimat = input('Masukkan kalimat: ')
if is_palindrom(kalimat):
    print('"' + kalimat + '" adalah palindrom')
else:
    print('"' + kalimat + '" bukan palindrom')
