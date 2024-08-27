# Entrada do usuário: salário-base do funcionário
salario_base = float(input("Digite o salário-base do funcionário: "))

# Cálculo da gratificação de 5%
gratificacao = salario_base * 0.05

# Cálculo do imposto de 7%
imposto = salario_base * 0.07

# Cálculo do salário a receber
salario_receber = salario_base + gratificacao - imposto

# Saída do resultado
print("O salário a receber é:", salario_receber)