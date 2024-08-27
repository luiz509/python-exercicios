# Entrada do usuário: três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Colocando os números em uma lista
numeros = [num1, num2, num3]

# Ordenando a lista em ordem decrescente
numeros.sort(reverse=True)

# Saída dos resultados
print("Os números em ordem decrescente são:", numeros)
