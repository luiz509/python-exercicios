import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b**2) - 4 * (a * c)

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print("A equação possui apenas uma raiz real: ", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("As raízes da equação são: ", x1, " e ", x2)

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Valor inválido. Digite uma nota entre 0 e 10.")

numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas > 1:
    print(centenas, "centenas", end="")
elif centenas == 1:
    print(centenas, "centena", end="")

if dezenas > 1:
    if centenas > 0:
        print(", ", end="")
    print(dezenas, "dezenas", end="")
elif dezenas == 1:
    if centenas > 0:
        print(", ", end="")
    print(dezenas, "dezena", end="")

if unidades > 1:
    if centenas > 0 or dezenas > 0:
        print(" e ", end="")
    print(unidades, "unidades")
elif unidades == 1:
    if centenas > 0 or dezenas > 0:
        print(" e ", end="")
    print(unidades, "unidade")
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Valor inválido. Digite uma nota entre 0 e 10.")