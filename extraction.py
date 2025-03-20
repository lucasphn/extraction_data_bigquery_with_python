from google.cloud import bigquery
import pandas as pd
import os
from tqdm import tqdm
from datetime import datetime

# caso não rodar as credenciais, rode esse comando:
# gcloud auth application-default login

client = bigquery.Client()  # Usa a autenticação padrão do ambiente

# Query SQL
query = """
 [SEU SCRIPT AQUI ENTRE AS ASPAS]
"""

# Mensagem inicial
print("🔄 Executando a query no BigQuery...")

# Criar barra de progresso para acompanhar a extração dos dados
with tqdm(total=100, desc="🔄 Buscando dados do BigQuery", bar_format="{l_bar}{bar} [tempo: {elapsed}]", ncols=80) as pbar:
    df = client.query(query).to_dataframe(progress_bar_type=None)
    pbar.update(100)  # Concluir barra de progresso

print("✅ Consulta concluída! Dados carregados com sucesso.")

# Amostra e Schema de dados
print(df.info())
print(df.head())

# Criar diretório 'data' se não existir
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Gerar timestamp para nome do arquivo
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Caminho do arquivo de saída com timestamp
output_path = os.path.join(output_dir, f"resultado_bigquery_{timestamp}.xlsx")

# Salvar DataFrame em Excel
print(f"💾 Salvando dados em {output_path} ...")
df.to_excel(output_path, index=False)

print("✅ Arquivo salvo com sucesso!")
print(f"📂 Local do arquivo: {os.path.abspath(output_path)}")