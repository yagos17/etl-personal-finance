# 📊 Personal Finance ETL com Python, MySQL e Dashboard BI

Projeto completo de ETL para automatizar o controle de finanças pessoais, integrando planilhas Excel, banco de dados MySQL e visualizações em dashboard. O objetivo é transformar dados brutos de transações em insights claros sobre receitas, despesas e saldo acumulado.

## 🚀 Funcionalidades

- Extração de dados financeiros a partir de planilhas `.xlsx`
- Transformação e limpeza dos dados com Python
- Carga dos dados no banco de dados MySQL
- Dashboard BI com visualização interativa:
  - Saldo acumulado ao longo do tempo
  - Despesas e receitas por categoria e tipo de pagamento
  - Tabela de transações recentes
  - Filtros personalizáveis (cartão, data, etc.)

## 🖥️ Tecnologias Utilizadas
- Python 
- MySQL
- Excel 
- Power BI

## 📦 Como executar
1. Clone este repositório:
```
git clone https://github.com/seu-usuario/etl-financeiro.git
cd etl-financeiro
```
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Crie o banco com script:
```
mysql -u root -p < sql/create_tables.sql
```
4. Execute o pipeline ETL:
```
python main.py
```
