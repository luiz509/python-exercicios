def calcular_tintas(area):
  """
  Calcula a quantidade de latas de tinta necessárias e o preço total.

  Args:
    area: Área a ser pintada em metros quadrados.

  Returns:
    Uma tupla com a quantidade de latas e o preço total.
  """
  litros_necessarios = area / 3
  latas_necessarias = int(litros_necessarios / 18) + 1
  preco_total = latas_necessarias * 80
  return latas_necessarias, preco_total

if __name__ == "__main__":
  area = float(input("Digite a área a ser pintada (em m²): "))
  latas, preco = calcular_tintas(area)
  print(f"Quantidade de latas necessárias: {latas}")
  print(f"Preço total: R$ {preco:.2f}")