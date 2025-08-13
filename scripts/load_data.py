import mysql.connector
from mysql.connector import Error
import pandas as pd

def carregar_no_mysql(df):
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            database = 'financas_pessoais',
            user = 'root',
            password = '1234'
        )
        if conexao.is_connected():
            cursor = conexao.cursor()

            cursor.execute("TRUNCATE TABLE transacoes")

            for i, linha in df.iterrows():
                query = "INSERT INTO transacoes (Data, Descricao, Categoria, Valor, Instituicao_Financeira, Tipo) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (
                    linha['Data'],
                    linha['Descrição'],
                    linha['Categoria'],
                    linha['Valor'],
                    linha['Instituição Financeira'],
                    linha['Tipo']
                )
                cursor.execute(query, valores)

            conexao.commit()
            print("Dados carregados com sucesso!")
    except Error as e:
        print(f"Erro ao carregar dados: {e}")
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()