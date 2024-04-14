from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import requests

def download_arquivo(ano_ini, ano_final, tipo_pessoa):
    # Configurações para o download do arquivo
    prefs = {
        "download.name": "teste",
        "download.default_directory": r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura\{}".format(tipo_pessoa)
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=options)

    # URL do site
    url = "http://sistemas.cultura.gov.br/salicnet/ctrIncentivadorMecenatoPorRegiaoUF/ctrIncentivadorMecenatoPorRegiaoUF.php"

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
        diretorio_base = r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura"
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
