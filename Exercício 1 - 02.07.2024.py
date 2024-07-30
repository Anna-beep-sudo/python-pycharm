lista = (5, 4, 3)
expoente = (7, 8, 9)
potencia = [pow (lista, expoente) for lista, expoente in zip (lista, expoente)]
print ('As potências são: ', potencia)



