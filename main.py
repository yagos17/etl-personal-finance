from scripts.extract_transform import carregar_excel, transformar_dados
from scripts.load_data import carregar_no_mysql

if __name__ == "__main__":
    caminho_arquivo = 'data/dados_financeiros.xlsx'

    try:
        print("Iniciando o processo de ETL...")

        print("-> Etapa de Extração: Carregando dados do Excel...")
        df_original = carregar_excel(caminho_arquivo)

        print("-> Etapa de Transformação: Processando e enriquecendo dados...")
        df_transformado = transformar_dados(df_original)

        print("-> Etapa de Carga: Conectando ao MySQL e carregando dados...")
        carregar_no_mysql(df_transformado)

        print("Processo de ETL concluído com sucesso!")

    except FileNotFoundError:
        print(f"Erro. O arquivo {caminho_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante o processo de ETL: {e}")