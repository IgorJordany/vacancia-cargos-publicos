import pandas as pd
import os

caminho_dados = "dados"

lista_dataframes = []

for arquivo in os.listdir(caminho_dados):
    caminho_arquivo = os.path.join(caminho_dados, arquivo)
    
    if arquivo.endswith('.ods'):
        df = pd.read_excel(caminho_arquivo, engine='odf')
        print(f"{arquivo} carregado como ODS.")
    elif arquivo.endswith('.xlsx'):
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        print(f"{arquivo} carregado como XLSX.")
    else:
        print(f"Formato não suportado: {arquivo}")
        continue
    
    lista_dataframes.append(df)

df_unificado = pd.concat(lista_dataframes, ignore_index=True)

print("Unificação concluída. Exibindo as primeiras linhas:")
print(df_unificado.head())

df_unificado.to_excel("dados_unificados_2024.xlsx", index=False)
print("Arquivo unificado salvo como 'dados_unificados_2024.xlsx'.")
