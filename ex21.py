import math

# Entrada dos coeficientes
a = float(input("Digite o valor de a (a ≠ 0): "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se é uma equação do 2º grau
if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    # Calcula o discriminante (delta)
    delta = b**2 - 4 * a * c
    
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui uma raiz real:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais:", x1, "e", x2)
    
    # Classificação da equação
    if b != 0 and c != 0:
        print("A equação é completa.")
    else:
        print("A equação é incompleta.")
