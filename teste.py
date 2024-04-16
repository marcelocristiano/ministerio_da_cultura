from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

msg = ""

prefs = {
    "download.name":"teste",
    "download.default_directory" : r"C:\Projetos-Python\ministerio_da_cultura\repository\bronze\ministerio da cultura\{}".format(tipo_pessoa)
    }
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
#options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

url = "http://sistemas.cultura.gov.br/salicnet/ctrIncentivadorMecenatoPorRegiaoUF/ctrIncentivadorMecenatoPorRegiaoUF.php"

for ano in range(2024, 2024 + 1):
    msg = "Download ano " + str(ano)

    driver.get(url=url)

    time.sleep(2)
    ano_element = driver.find_element(By.NAME, "ano")
    select_ano = Select(ano_element)
    select_ano.select_by_visible_text(str(ano))

    tipo_pessoa_element = driver.find_element(By.NAME, "tipopessoa")
    select_tipo_pessoa = Select(tipo_pessoa_element)
    select_tipo_pessoa.select_by_visible_text(tipo_pessoa)

    btn_ok = driver.find_element(By.NAME, "sub_form").click()

    time.sleep(1)

    btn_xls = driver.find_element(By.NAME, "sc_b_xls").click()

    btn_download = driver.find_element(By.XPATH, '/html/body/font/a/font/b').click()

    time.sleep(3)


driver.quit()
