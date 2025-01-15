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
