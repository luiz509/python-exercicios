n = int(input("Digite o valor de n: "))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo:
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")