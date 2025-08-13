import pandas as pd

def carregar_excel(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo, sheet_name='dados')
    return df

def transformar_dados(df):
    df = df.copy()

    df['Tipo'] = df['Valor'].apply(lambda x: 'Receita' if x > 0 else 'Despesa')

    return df