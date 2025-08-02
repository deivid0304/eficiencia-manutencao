
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('../data/manutencao_turbinas.csv', parse_dates=['Data'])

# Criar colunas adicionais
df['AnoMes'] = df['Data'].dt.to_period('M')

# MTTR por equipamento
mttr = df.groupby('Equipamento')['Tempo_Parado_Horas'].mean().sort_values()
print("MTTR por Equipamento:\n", mttr)

# Custo total por tipo
custo_tipo = df.groupby('Tipo')['Custo'].sum()

# Gráfico MTTR
plt.figure(figsize=(8, 4))
mttr.plot(kind='bar', title='MTTR por Equipamento')
plt.ylabel('Horas')
plt.tight_layout()
plt.savefig('../images/grafico_mttr.png')
plt.close()

# Gráfico de custo por tipo de manutenção
plt.figure(figsize=(6, 4))
custo_tipo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Custo por Tipo de Manutenção')
plt.ylabel('')
plt.tight_layout()
plt.savefig('../images/grafico_custo.png')
plt.close()
