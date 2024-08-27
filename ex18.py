# Entrada do usuário: valor do depósito e taxa de juros
deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))

# Cálculo do rendimento
rendimento = deposito * (taxa_juros / 100)

# Cálculo do valor total após o rendimento
valor_total = deposito + rendimento

# Saída dos resultados
print("O valor do rendimento é:", rendimento)
print("O valor total após o rendimento é:", valor_total)