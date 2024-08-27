# Entrada do usuário: salário atual e percentual de aumento
salario = float(input("Digite o salário atual do funcionário: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

# Cálculo do valor do aumento
aumento = salario * (percentual_aumento / 100)

# Cálculo do novo salário
novo_salario = salario + aumento

# Saída dos resultados
print("O valor do aumento é:", aumento)
print("O novo salário é:", novo_salario)