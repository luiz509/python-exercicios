ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

idade_em_2019 = 2019 - ano_nascimento

print(f"A idade da pessoa em anos: {idade_anos}")
print(f"A idade da pessoa em meses: {idade_meses}")
print(f"A idade da pessoa em dias: {idade_dias}")
print(f"A idade da pessoa em semanas: {idade_semanas}")
print(f"A idade da pessoa em 2019: {idade_em_2019}")