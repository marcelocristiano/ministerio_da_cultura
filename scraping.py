import requests
from bs4 import BeautifulSoup

payload = {
'nmgp_parms': 'ano?#?1994?@?tipopessoa?#?2?@?NM_btn_insert?#?S?@?NM_btn_update?#?S?@?NM_btn_delete?#?S?@?NM_btn_navega?#?S?@?',
'nmgp_url_saida': '/salicnet/ctrIncentivadorMecenatoPorRegiaoUF/ctrIncentivadorMecenatoPorRegiaoUF.php',
'script_case_init': 1
}


url= 'http://sistemas.cultura.gov.br/salicnet/conIncentivadorMecenatoPorRegiaoUF/conIncentivadorMecenatoPorRegiaoUF.php'

res = requests.get(url=url, params=payload)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)