pares = 0
impares = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")