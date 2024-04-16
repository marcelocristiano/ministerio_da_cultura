from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import requests
<<<<<<< HEAD
import pandas as pd
=======

def download_arquivo(ano_ini, ano_final, tipo_pessoa):
    # Configurações para o download do arquivo
    prefs = {
        "download.name": "teste",
        "download.default_directory": r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura\{}".format(tipo_pessoa)
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
>>>>>>> refs/remotes/origin/main

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=options)

<<<<<<< HEAD
def download_arquivo(ano_ini, ano_final, tipo_pessoa):
    # Configurações para o download do arquivo
    prefs = {
        "download.name": "teste",
        "download.default_directory": r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura\{}".format(tipo_pessoa)
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    #options.add_argument('--headless')

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=options)

    # URL do site
    url = "http://sistemas.cultura.gov.br/salicnet/ctrIncentivadorMecenatoPorRegiaoUF/ctrIncentivadorMecenatoPorRegiaoUF.php"

=======
    # URL do site
    url = "http://sistemas.cultura.gov.br/salicnet/ctrIncentivadorMecenatoPorRegiaoUF/ctrIncentivadorMecenatoPorRegiaoUF.php"

>>>>>>> refs/remotes/origin/main
    # Iterando sobre os anos especificados
    for ano in range(ano_ini, ano_final + 1):
        msg = "Download ano " + str(ano)

        # Abrindo a página no navegador
        driver.get(url=url)
        time.sleep(2)

        # Selecionando o ano e o tipo de pessoa nos dropdowns
        ano_element = driver.find_element(By.NAME, "ano")
        select_ano = Select(ano_element)
        select_ano.select_by_visible_text(str(ano))

        tipo_pessoa_element = driver.find_element(By.NAME, "tipopessoa")
        select_tipo_pessoa = Select(tipo_pessoa_element)
        select_tipo_pessoa.select_by_visible_text(tipo_pessoa)

        # Clicando no botão "OK"
        btn_ok = driver.find_element(By.NAME, "sub_form").click()
        time.sleep(1)

        # Clicando no botão para baixar o arquivo XLS
        btn_xls = driver.find_element(By.NAME, "sc_b_xls").click()

        # Obtendo o link de download do arquivo
        link_download = driver.find_element(By.XPATH, '/html/body/font/a/font/b').text
        url_dowload = "http://sistemas.cultura.gov.br{}".format(link_download)

        # Diretório base para salvar o arquivo
<<<<<<< HEAD
        diretorio_base = r"C:\Users\DW8R\OneDrive - PETROBRAS\Documentos\projetos_python\ministerio_da_cultura\repository\bronze\ministerio da cultura"
=======
        diretorio_base = r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura"
>>>>>>> refs/remotes/origin/main
        nome_pasta = tipo_pessoa

        # Caminho da pasta para o tipo de pessoa
        path_pessoa_juridica = os.path.join(diretorio_base, nome_pasta)

        # Verificando e criando a pasta se ela não existir
        if not os.path.exists(path_pessoa_juridica):
            os.makedirs(path_pessoa_juridica)

        # Caminho completo do arquivo
        caminho_arquivo = os.path.join(path_pessoa_juridica, str(ano) + '.xls')

        # Baixando e salvando o arquivo
        resp = requests.get(url_dowload)
        with open(caminho_arquivo, 'wb') as arq:
            arq.write(resp.content)
        time.sleep(3)

        # Retornando mensagem
        yield msg

    # Fechando o driver do Chrome
    driver.quit()
<<<<<<< HEAD


def transformar_dado_silver(tipo_pessoa):
    diretorio_bronze = r"C:\Users\DW8R\OneDrive - PETROBRAS\Documentos\projetos_python\ministerio_da_cultura\repository\bronze\ministerio da cultura\{}".format(tipo_pessoa)
    diretorio_silver = r"C:\Users\DW8R\OneDrive - PETROBRAS\Documentos\projetos_python\ministerio_da_cultura\repository\silver\ministerio da cultura\{}".format(tipo_pessoa)

    # Lista todos os arquivos no diretório Excel
    arquivos = os.listdir(diretorio_bronze)

    for arquivo in arquivos:
        msg = 'Transformando ano', arquivo.split('.')[0]
        yield msg
        # Lê o arquivo Excel
        df = pd.read_excel(os.path.join(diretorio_bronze, arquivo))
        # Altera nomes de colunas
        df = df.rename(columns={
            'CNPJ/CPF': 'CNPJ_CPF',
            'Incentivador': 'INCENTIVADOR',
            'NÂº Projeto': 'NUMERO_PROJETO',
            'Nome do Projeto': 'NOME_PROJETO',
            'UF do Projeto': 'UF_PROJETO',
            'Vl. Incentivo R$': 'VALOR'
        })

        df['ANO'] = arquivo.split('.')[0]

        arquivo_parquet = arquivo.split('.')[0] + '.parquet'

        # Salva o DataFrame como arquivo Parquet
        df.to_parquet(os.path.join(diretorio_silver, arquivo_parquet))


def transformar_dado_gold(tipo_pessoa):
    diretorio_silver = r"C:\Users\DW8R\OneDrive - PETROBRAS\Documentos\projetos_python\ministerio_da_cultura\repository\silver\ministerio da cultura\{}".format(tipo_pessoa)
    diretorio_gold = r"C:\Users\DW8R\OneDrive - PETROBRAS\Documentos\projetos_python\ministerio_da_cultura\repository\gold\ministerio da cultura\{}".format(tipo_pessoa)

    # Lista todos os arquivos no diretório Excel
    arquivos = os.listdir(diretorio_silver)

    arquivo_parquet = 'consolidado' + '.parquet'

    dfs = []

    for arquivo in arquivos:
        # Ler o arquivo Parquet em um DataFrame
        df = pd.read_parquet(os.path.join(diretorio_silver, arquivo))
        # Adicionar o DataFrame à lista
        dfs.append(df)

        # Concatenar os DataFrames em um único DataFrame
        df = pd.concat(dfs, ignore_index=True)
        # Salva o DataFrame como arquivo Parquet
        df.to_parquet(os.path.join(diretorio_gold, arquivo_parquet))
=======
>>>>>>> refs/remotes/origin/main
