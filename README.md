# Projeto Tech Challenge 1
Este projeto realiza consultas aos dados de vinhos do site http://vitibrasil.cnpuv.embrapa.br/index.php via API, desenvolvido com FastAPI.
## Funcionalidades
- **Consultas**: Permite consultar dados de vinhos diretamente do site da Embrapa ou dos arquivos .csv backups.
- **Web Scrapping**: Extrai dados de página web utilizando BeautifulSoup.
## Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/OliveiraGiulio/Tech-Challenge-1
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Inicialize o Web Server

```bash
cd app
uvicorn main:app --reload
```
O aplicativo estará disponível em `http://127.0.0.1:8000/docs`.

## Consultando dados

Para consultador os dados, selecione um dos métodos GET disponíveis e clique em Try it out:
![image](https://github.com/user-attachments/assets/7a3eac4f-a281-499e-b547-6f40ca562b89)

Repare que cada método tem seu conjunto de parâmetros padrões para consulta:
Digite o ano do dado desejado, escolha as opções no menu dropdown "subcategory" e clique em "Execute
![image](https://github.com/user-attachments/assets/d3facb2c-40ca-400f-8cb2-d59889c7e45f)

Caso o Request seja bem sucedido, o método retornará o URL da solicitação e os dados no formato JSON.
![image](https://github.com/user-attachments/assets/5233350a-9d73-4b11-8062-4ef7662e92c9)
