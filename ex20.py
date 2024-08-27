# Entrada do usuário: turno de estudo
turno = input("Digite o turno em que você estuda (M-matutino, V-Vespertino, N-Noturno): ").upper()

# Verificação do turno e saída da mensagem correspondente
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")