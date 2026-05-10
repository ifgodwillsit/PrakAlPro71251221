lista = input("Masukkan List A: ").split(',')
listb = input("Masukkan List B: ").split(',')

lista = [x.strip() for x in lista]
listb = [x.strip() for x in listb]

dictionary = dict(zip(lista, listb))

print("\nDictionary :", dictionary)
