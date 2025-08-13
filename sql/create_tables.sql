-- Cria o banco de dados se ainda não existir
CREATE DATABASE IF NOT EXISTS financas_pessoais;

-- Seleciona o banco de dados para usar
USE financas_pessoais;

-- Cria a tabela transacoes
CREATE TABLE IF NOT EXISTS transacoes (
    Data DATE,
    Descricao VARCHAR(255),
    Categoria VARCHAR(100),
    Valor DECIMAL(10, 2),
    Instituicao_Financeira VARCHAR(100),
    Tipo VARCHAR(10)
);