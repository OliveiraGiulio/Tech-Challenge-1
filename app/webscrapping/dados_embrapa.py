import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from pathlib import Path

current_dir = Path(__file__).resolve().parent
file_path = current_dir.parent.parent / 'db_embrapa_bkp'
gh_url = 'https://raw.githubusercontent.com/OliveiraGiulio/Tech-Challenge-1/refs/heads/main/db_embrapa_bkp'

dict_dados = {
     'Producao'       :'opt_02'
    ,'Processamento'  :'opt_03'
    ,'Comercializacao':'opt_04'
    ,'Importacao'     :'opt_05'
    ,'Exportacao'     :'opt_06'
}

dict_dados_processamento = {
     'Viniferas'            :'subopt_01'
    ,'Americanas_e_hibridas':'subopt_02'
    ,'Uvas_de_mesa'         :'subopt_03'
    ,'Sem_classificacao'    :'subopt_04'
}

dict_dados_importacao = {
     'Vinhos_de_Mesa'            :'subopt_01'
    ,'Espumantes'                :'subopt_02'
    ,'Uvas_Frescas'              :'subopt_03'
    ,'Uvas_passas'               :'subopt_04'
    ,'Suco_de_uva'               :'subopt_05'
}

dict_dados_exportacao = {
     'Vinhos_de_Mesa'            :'subopt_01'
    ,'Espumantes'                :'subopt_02'
    ,'Uvas_Frescas'              :'subopt_03'
    ,'Suco_de_uva'               :'subopt_04'
}

dicionario = {
    'Processamento': dict_dados_processamento
    ,'Importacao': dict_dados_importacao
    ,'Exportacao': dict_dados_exportacao
}

dict_opts = {
    'Processamento':{
        'Viniferas'             :'subopt_01'
        ,'Americanas_e_hibridas':'subopt_02'
        ,'Uvas_de_mesa'         :'subopt_03'
        ,'Sem_classificacao'    :'subopt_04'
    }
    ,'Importacao':{
        'Vinhos_de_Mesa':'subopt_01'
        ,'Espumantes'   :'subopt_02'
        ,'Uvas_Frescas' :'subopt_03'
        ,'Uvas_passas'  :'subopt_04'
        ,'Suco_de_uva'  :'subopt_05'
    }
    ,'Exportacao':{
        'Vinhos_de_Mesa':'subopt_01'
        ,'Espumantes'   :'subopt_02'
        ,'Uvas_Frescas' :'subopt_03'
        ,'Suco_de_uva'  :'subopt_04'
    }
}


class DadosEmbrapa():
    def conecta_site(ano: int, tabela: str, subopcao: str=None) -> requests.Response:
            url = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
            if tabela in ('Processamento', 'Importacao', 'Exportacao'):
                 params = {"ano": ano
                           ,"opcao": {dict_dados[tabela]}
                           ,"subopcao":{dict_opts[tabela][subopcao]}
                        }   
            else:
                params = {"ano": ano
                          ,"opcao": {dict_dados[tabela]}
                        }
            try:
                response = requests.get(url, params, timeout=5)
                response.raise_for_status()
                print(f'Conexão com site da Embrapa bem sucedida!')
                return response
            except requests.exceptions.RequestException:
                if subopcao is None:
                    
                    try:
                        print(f'Recorrendo ao arquivo backup...')
                        response = pd.read_csv(rf'{gh_url}/{tabela}.csv', sep=';')
                        #response = pd.read_csv(rf'{file_path}\{tabela}.csv', sep=';')
                        response = response[(response['Year'] == ano)].reset_index(drop=True)
                        response.drop(columns={'Year', 'Category'}, inplace=True)
                        return response
                    except:
                        raise RuntimeError('Erro ao tentar extrair os dados da Embrapa e do arquivo csv backup')
                else:
                    try:
                        print(f'Recorrendo ao arquivo backup...')
                        response = pd.read_csv(rf'{gh_url}/{tabela}.csv', sep=';')
                        #response = pd.read_csv(rf'{file_path}\{tabela}.csv', sep=';')
                        response = response[(response['Year'] == ano) & (response['Subcategory'] == subopcao)].reset_index(drop=True)
                        response.drop(columns={'Year', 'Category', 'Subcategory'}, inplace=True)
                        return response
                    except:
                        raise RuntimeError('Erro ao tentar extrair os dados da Embrapa e do arquivo csv backup')

    def extrai_tabelas(response: str = None) -> dict:
        if response is not None and isinstance(response, requests.Response):
            soup   = BeautifulSoup(response.text, 'html.parser')
            tabela = soup.find('table', {'class': 'tb_base tb_dados'})

            colunas = [header.text.strip() for header in tabela.find_all('th')]
        
            rows = tabela.find_all('tr')[1:]  # Skip the header row
            table_data = []
            for row in rows:
                cells = row.find_all('td')
                cell_data = [cell.text.strip() for cell in cells]
                table_data.append(cell_data)
            df = pd.DataFrame(table_data, columns=colunas)
            return df.to_dict(orient='records')
        else:
            return response.to_dict(orient='records')