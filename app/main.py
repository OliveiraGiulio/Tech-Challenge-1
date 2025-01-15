from fastapi import FastAPI, Path
from typing import Literal
from webscrapping import DadosEmbrapa

app = FastAPI()

def extrair_dados(ano: int, category: str, subcategory: str = None) -> dict:
    try:
        response = DadosEmbrapa.conecta_site(ano, category, subcategory)
        dados    = DadosEmbrapa.extrai_tabelas(response)
        return dados
    except Exception as error:
        return {"error": str(error)}

@app.get('/Producao/{ano}')
def dados_producao(ano: int = Path(..., ge=1970, le=2023)):
    """
    Realiza a extração dos dados da tabela de Produção do site da Embrapa ou do WebArchive.
    """
    return extrair_dados(ano, 'Producao')


@app.get('/Processamento/{subcategory}/{ano}')
def dados_processamento(ano: int = Path(..., ge=1970, le=2023), subcategory: Literal['Viniferas', 'Americanas_e_hibridas', 'Uvas_de_mesa', 'Sem_classificacao'] = None):
    """
    Realiza a extração dos dados da tabela de Processamento do site da Embrapa.
    É necessário passar o tipo de uva como parâmetro para essa consulta.
    """
    return extrair_dados(ano, 'Processamento', subcategory)

@app.get('/Comercializacao/{ano}')
def dados_comercializacao(ano: int = Path(..., ge=1970, le=2023)):
    """
    Realiza a extração dos dados da tabela de Comercialização do site da Embrapa ou do WebArchive.
    """
    return extrair_dados(ano, 'Comercializacao')

@app.get('/Importacao/{subcategory}/{ano}')
def dados_importacao(ano: int = Path(..., ge=1970, le=2023), subcategory: Literal['Vinhos_de_Mesa', 'Espumantes', 'Uvas_Frescas', 'Uvas_passas', 'Suco_de_uva'] = None):
    """
    Realiza a extração dos dados da tabela de Importação do site da Embrapa ou do WebArchive.
    """
    return extrair_dados(ano, 'Importacao', subcategory)

@app.get('/Exportacao/{subcategory}/{ano}')
def dados_exportacao(ano: int = Path(..., ge=1970, le=2023), subcategory: Literal['Vinhos_de_Mesa', 'Espumantes', 'Uvas_Frescas' , 'Suco_de_uva'] = None):
    """
    Realiza a extração dos dados da tabela de Exportação do site da Embrapa ou do WebArchive.
    """
    return extrair_dados(ano, 'Exportacao', subcategory)