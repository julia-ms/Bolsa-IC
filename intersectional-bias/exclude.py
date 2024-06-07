import os
import pandas as pd

# Diretório onde está o arquivo Python
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho para a pasta "data"
diretorio_data = os.path.join(diretorio_atual, 'datasets')

# Lista todos os arquivos na pasta "data"
arquivos = os.listdir(diretorio_data)

# Loop pelos arquivos
for arquivo in arquivos:
    # Verifica se o arquivo é um XLSX
    if arquivo.endswith('.xlsx'):
        # Carrega o conjunto de dados
        caminho_arquivo = os.path.join(diretorio_data, arquivo)
        df = pd.read_excel(caminho_arquivo)
        
        # Remove as colunas 'sex', 'race' e 'housing'
        colunas_a_remover = ['Sex', 'Race', 'Housing']
        df = df.drop(columns=colunas_a_remover, errors='ignore')
        
        # Salva o conjunto de dados atualizado no mesmo arquivo
        df.to_excel(caminho_arquivo, index=False)
