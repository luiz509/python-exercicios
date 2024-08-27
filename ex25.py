# Entrada do usuário: número positivo maior que zero
numero = float(input("Digite um número positivo maior que zero: "))

# Verificação do número
if numero > 0:
    # Cálculo do quadrado e cubo
    quadrado = numero ** 2
    cubo = numero ** 3
    
    # Saída dos resultados
    print("O número digitado ao quadrado é:", quadrado)
    print("O número digitado ao cubo é:", cubo)
else:
    print("Número inválido. Digite um número positivo maior que zero.")
