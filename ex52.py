n = int(input("Digite o valor de n: "))
divisões = 0
for i in range(2, n + 1):
    primo = True
    for j in range(2, int(i**0.5) + 1):
        divisões += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(f"{i} é um número primo")
print(f"Número total de divisões: {divisões}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")