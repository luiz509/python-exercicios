# Programa para verificar se um valor é positivo ou negativo

# Recebe um valor do usuário
valor = float(input("Digite um valor: "))

# Verifica se o valor é positivo, negativo ou zero
if valor > 0:
    print(f"O valor {valor} é positivo.")
elif valor < 0:
    print(f"O valor {valor} é negativo.")
else:
    print(f"O valor {valor} é zero.")