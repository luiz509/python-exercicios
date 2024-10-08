n = int(input("Digite o número total de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
for i in range(1, n + 1):
    voto = int(input(f"Eleitor {i}, digite o número do candidato (1, 2 ou 3): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Voto inválido!")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")