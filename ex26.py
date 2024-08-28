base = float(input("digite a base (maior que zero): "))
expoente = int(input("digite o expoente(maior q zero no maximo 10): "))

if base <=0 :
     print(" a base deve ser maior q zero.")
elif expoente <= 0:
    print("o expoente deve ser maior q zero.")
elif expoente > 10:
 print("o expoente tem que ser no maxmo 10.")
else:

    resultado = base ** expoente

    print (f"o resultado é {base} elevado a {expoente} é: {resultado }")