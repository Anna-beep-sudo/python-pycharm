lista = (4, 3, 5)
lista = (2, 2, 2)
potencia = [pow(lista, expoente) for lista, expoente in zip (lista, expoente)]
print('Os resultados são: ', potencia)