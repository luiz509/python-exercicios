n = int(input("Digite o valor de n: "))
a = 1
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")