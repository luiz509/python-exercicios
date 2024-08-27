# Programa para verificar se uma letra é uma vogal ou consoante

# Recebe a letra do usuário
letra = input("Digite uma letra: ").strip().lower()

# Verifica se a letra é uma vogal
if letra in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")