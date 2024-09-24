while True: # type: ignore
    nota1 = float (input("digite a primeira nota: "))
    if 0 <= nota1 <= 10: 
        break
    else: 
        print("nota invalida!")

while  True:
    nota2 = float(input("digite a segunda nota: "))
    if 0<= nota2 <= 10:
        break
    else:
        print("Nota invalida!")

media = (nota1 + nota2) / 2
print("a media semestral é:",media)
