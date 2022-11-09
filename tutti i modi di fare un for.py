lista1 = ["a","b","c","d"]
lista2 = [1,2,3,4]

# for su lista c style
for i in range(0, len(lista1)):
    print(lista1[i])
print("")
# for su lista python-style
for elemento in lista1:
    print(elemento)
print("")
# for su lista con enumerate
for i,e in enumerate(lista1):
    print(i, e)
print("")
# for su entrambe le liste python style(zip)
for a, b in zip(lista1, lista2):
    print(a, b)
print("")
#for su entrambe le liste con liste in c style
diz = {}

#for su diz usando items()
#for su diz senza items()
for chiave in diz:
    print(chiave)