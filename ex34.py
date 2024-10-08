def calcular_peso_ideal(h, sexo):
  """
  Calcula o peso ideal de uma pessoa com base na altura e sexo.

  Args:
    h: Altura da pessoa em metros.
    sexo: Sexo da pessoa ('H' para homem, 'M' para mulher).

  Returns:
    O peso ideal da pessoa em kg.
  """
  if sexo == 'H':
    return (72.7 * h) - 58
  elif sexo == 'M':
    return (62.1 * h) - 44.7
  else:
    return "Sexo inválido."