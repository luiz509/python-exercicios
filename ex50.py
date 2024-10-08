n = int(input("Digite o valor de n: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")