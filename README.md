
# 📊 Análise de Eficiência da Manutenção em Turbinas Eólicas

Este projeto tem como objetivo analisar a eficiência das manutenções realizadas em turbinas eólicas, utilizando dados de tempo parado, custos e tipos de manutenção para gerar insights relevantes.

## 📁 Estrutura dos Dados

O dataset `manutencao_turbinas.csv` contém os seguintes campos:

- `Data`: Data da ocorrência da manutenção
- `Equipamento`: Nome da turbina eólica
- `Tipo`: Tipo da manutenção (Corretiva, Preditiva, Preventiva)
- `Tempo_Parado_Horas`: Tempo total de inatividade
- `Custo`: Custo da intervenção

## 📈 Análises Realizadas

1. **MTTR por Equipamento**
2. **Distribuição de Custo por Tipo de Manutenção**
3. **Evolução Mensal do MTTR**
4. **Top 5 Equipamentos por Custo Total**
5. **Correlação entre Tempo Parado e Custo**

## 🛠 Tecnologias Utilizadas

- Python 3.11
- Pandas
- Matplotlib
- Seaborn
- python-docx

## 📄 Relatório Técnico

Um relatório técnico em `.docx` será gerado automaticamente contendo todas as análises com explicações.

## 📌 Execução

```bash
python analise_manutencao.py
