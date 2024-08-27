# Programa para uma calculadora simples

# Recebe os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Recebe o tipo de operação desejada
operacao = input("Digite a operação desejada (soma/subtracao): ").strip().lower()

# Realiza o cálculo com base na operação escolhida
if operacao == 'soma':
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == 'subtracao':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
else:
    print("Operação inválida. Por favor, escolha 'soma' ou 'subtracao'.")