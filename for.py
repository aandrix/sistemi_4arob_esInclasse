lista = [1,2,3,4,5,2,3,1,3,2,10,102,392,392]

#modo preferito (pytonico)

for elemento in lista:
    print(elemento, end = "  ")

print()

#modo c-style
for k in range(0, len(lista)):
    print(lista[k],end ="  ")

#calcolo del massimo del minimo valore 
min = lista[0]
max = lista[0]
for elemento in lista:
    if(min > elemento):
        min = elemento
    elif(max < elemento):
        max = elemento

print()
print(f"il massimo è {max} mentre quello minore è{min}")