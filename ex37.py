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