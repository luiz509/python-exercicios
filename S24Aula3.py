 import pandas as pd

# Carrega os dados de vendas
vendas = pd.read_csv('vendas.csv')  # Substitua 'vendas.csv' pelo nome do seu arquivo

# Calcula o total de vendas por produto
total_vendas_produto = vendas.groupby('produto')['valor'].sum()

# Calcula a média de vendas diárias
vendas['data'] = pd.to_datetime(vendas['data'])
media_vendas_diarias = vendas.groupby(vendas['data'].dt.date)['valor'].mean()

# Imprime os resultados
print("Total de vendas por produto:")
print(total_vendas_produto)

print("\nMédia de vendas diárias:")
print(media_vendas_diarias)