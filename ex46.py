numero = int(input("Digite um número entre 1 e 10: "))
print(f"TABUADA de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")