# Entrada do usuário
letra = input("Digite uma letra (F ou M): ").upper()

# Verificação e saída do resultado
if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo Inválido")