n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    if n2 == 0:
        print("Erro: Divisão por zero!")
    else:
        resultado = n1 / n2
else:
    print("Operação inválida!")

if operacao in ("+", "-", "*", "/"):
    print(f"O resultado da operação é: {resultado}")