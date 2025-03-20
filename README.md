# README - Execução do Script de Extração do BigQuery

Este repositório contém um script em Python que executa uma query no BigQuery e salva os resultados em um arquivo Excel. Abaixo estão as instruções para configurar o ambiente e rodar o código corretamente.

---

## 1. **Configurar o Ambiente Virtual**

1. Abra o terminal e navegue até a pasta do projeto:
   ```sh
   cd /caminho/do/projeto
   ```

2. Crie um ambiente virtual (caso ainda não tenha):
   ```sh
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   ```sh
   source venv/bin/activate  # Para macOS/Linux
   ````

4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

---

## 2. **Instalação do Google Cloud SDK e Autenticação**

O script utiliza o SDK do Google Cloud para acessar o BigQuery. Para instalá-lo no macOS, siga os passos:

1. **Baixar e instalar o Google Cloud SDK:**
   ```sh
   brew install --cask google-cloud-sdk
   ```

2. **Reinicie o terminal e inicialize o SDK:**
   ```sh
   gcloud init
   ```

3. **Autenticar e configurar credenciais:**
   ```sh
   gcloud auth application-default login
   ```

4. **Verifique se a autenticação foi configurada corretamente:**
   ```sh
   gcloud auth list
   ```

5. **Caso precise definir um projeto padrão:**
   ```sh
   gcloud config set project [SEU_PROJECT_ID]
   ```

---

## 3. **Executando o Script**

Com o ambiente virtual ativado e as credenciais configuradas, execute o script:
```sh
python extraction.py
```

Durante a execução, o terminal exibirá informações sobre o progresso e, ao final, o arquivo Excel será salvo na pasta `data/` com um timestamp para identificá-lo.

Exemplo de arquivo gerado:
```
data/resultado_bigquery_20240317_153045.xlsx
```

---

## 4. **Saída Esperada**

- O terminal mostrará mensagens de progresso durante a execução.
- O arquivo de saída estará salvo no diretório `data/`.
- O script gera logs informando os detalhes do processo.

---

## 5. **Solução de Problemas**

- **Erro de autenticação?**
  - Rode novamente:
    ```sh
    gcloud auth application-default login
    ```
- **Comando `gcloud` não encontrado?**
  - Certifique-se de que o SDK foi instalado corretamente e execute:
    ```sh
    source ~/.zshrc  # Para usuários de zsh
    source ~/.bashrc  # Para usuários de bash
    ```
- **Erro de dependência no Python?**
  - Reinstale os pacotes:
    ```sh
    pip install --upgrade -r requirements.txt
    ```

---

## 6. **Manutenção e Atualização**

- Para atualizar as dependências do projeto:
  ```sh
  pip freeze > requirements.txt
  ```
- Para atualizar o Google Cloud SDK:
  ```sh
  gcloud components update
  ```


---

**Autor:** Lucas Almeida 

# extraction_data_bigquery_with_python
