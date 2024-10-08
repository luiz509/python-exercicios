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
numero = int(input("Digite um número entre 0 e 99: "))
if numero < 0 or numero > 99:
    print("Número inválido. Digite um número entre 0 e 99.")
else:
    unidades = numero % 10
    dezenas = numero // 10
    
    # Unidades
    if unidades == 0:
        unidade_extenso = ""
    elif unidades == 1:
        unidade_extenso = "um"
    elif unidades == 2:
        unidade_extenso = "dois"
    elif unidades == 3:
        unidade_extenso = "três"
    elif unidades == 4:
        unidade_extenso = "quatro"
    elif unidades == 5:
        unidade_extenso = "cinco"
    elif unidades == 6:
        unidade_extenso = "seis"
    elif unidades == 7:
        unidade_extenso = "sete"
    elif unidades == 8:
        unidade_extenso = "oito"
    elif unidades == 9:
        unidade_extenso = "nove"
    
    # Dezenas
    if dezenas == 0:
        dezena_extenso = ""
    elif dezenas == 1:
        if unidades == 0:
            dezena_extenso = "dez"
        elif unidades == 1:
            dezena_extenso = "onze"
        elif unidades == 2:
            dezena_extenso = "doze"
        elif unidades == 3:
            dezena_extenso = "treze"
        elif unidades == 4:
            dezena_extenso = "quatorze"
        elif unidades == 5:
            dezena_extenso = "quinze"
        elif unidades == 6:
            dezena_extenso = "dezesseis"
        elif unidades == 7:
            dezena_extenso = "dezessete"
        elif unidades == 8:
            dezena_extenso = "dezoito"
        elif unidades == 9:
            dezena_extenso = "dezenove"
    elif dezenas == 2:
        dezena_extenso = "vinte"
    elif dezenas == 3:
        dezena_extenso = "trinta"
    elif dezenas == 4:
        dezena_extenso = "quarenta"
    elif dezenas == 5:
        dezena_extenso = "cinquenta"
    elif dezenas == 6:
        dezena_extenso = "sessenta"
    elif dezenas == 7:
        dezena_extenso = "setenta"
    elif dezenas == 8:
        dezena_extenso = "oitenta"
    elif dezenas == 9:
        dezena_extenso = "noventa"
    
    # Impressão do número por extenso
    if dezenas == 1 and unidades != 0:
        print(dezena_extenso)
    else:
        print(f"{dezena_extenso} e {unidade_extenso}")