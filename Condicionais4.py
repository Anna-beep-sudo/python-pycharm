numero = int(input("Digite um número para conferir sua tabuada: "))
print("Tabuada do {numero}:")
for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} x {n} = {resultado}")

