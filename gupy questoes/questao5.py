string = input("Digite uma string: ")


lista = list(string)

for i in range(len(lista) // 2):
    j = len(lista) - i - 1
    lista[i], lista[j] = lista[j], lista[i]

string_invertida = ''.join(lista)
print("String invertida:", string_invertida)
