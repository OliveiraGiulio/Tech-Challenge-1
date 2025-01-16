from app.webscrapping.dados_embrapa import DadosEmbrapa

def extrair_dados(ano: int, category: str, subcategory: str = None) -> dict:
    try:
        response = DadosEmbrapa.conecta_site(ano, category, subcategory)
        dados    = DadosEmbrapa.extrai_tabelas(response)
        return dados
    except Exception as error:
        return {"error": str(error)}