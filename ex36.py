if __name__ == "__main__":
  dia_semana = int(input("Digite um número de 1 a 7 para o dia da semana: "))
  if dia_semana == 1:
    print("Domingo")
  elif dia_semana == 2:
    print("Segunda-feira")
  elif dia_semana == 3:
    print("Terça-feira")
  elif dia_semana == 4:
    print("Quarta-feira")
  elif dia_semana == 5:
    print("Quinta-feira")
  elif dia_semana == 6:
    print("Sexta-feira")
  elif dia_semana == 7:
    print("Sábado")
  else:
    print("Valor inválido.")
  area = float(input("Digite a área a ser pintada (em m²): "))
  latas, preco = calcular_tintas(area)
  print(f"Quantidade de latas necessárias: {latas}")
  print(f"Preço total: R$ {preco:.2f}")