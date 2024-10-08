n = 0
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while n >= 0:
    n = int(input("Digite um número positivo (ou um número negativo para sair): "))
    if n >= 0:
        if 0 <= n <= 25:
            intervalo1 += 1
        elif 26 <= n <= 50:
            intervalo2 += 1
        elif 51 <= n <= 75:
            intervalo3 += 1
        elif 76 <= n <= 100:
            intervalo4 += 1
print(f"Números no intervalo [0-25]: {intervalo1}")
print(f"Números no intervalo [26-50]: {intervalo2}")
print(f"Números no intervalo [51-75]: {intervalo3}")
print(f"Números no intervalo [76-100]: {intervalo4}")
texto = input("Digite uma sequência de caracteres: ")
texto = texto.lower().replace(" ", "")
texto_invertido = texto[::-1]
if texto == texto_invertido:
    print(f"A sequência '{texto}' é um palíndromo.")
else:
    print(f"A sequência '{texto}' não é um palíndromo.")