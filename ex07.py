# Programa para calcular a média de uma disciplina e verificar a condição do aluno

# Recebe o nome da disciplina
disciplina = input("Digite o nome da disciplina: ")

# Recebe as 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Determina a condição do aluno
if media >= 7:
    condicao = "Aprovado"
else:
    condicao = "Reprovado"

# Imprime os resultados
print(f"Disciplina: {disciplina}")
print(f"Média: {media:.2f}")
print(f"Condição do aluno: {condicao}")