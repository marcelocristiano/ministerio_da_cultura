# Script de Automação para Ministério da Cultura

Este script foi desenvolvido para automatizar o processo de download, transformação e consolidação de dados de incentivo à cultura do Ministério da Cultura do Brasil.

## Requisitos

- Python 3.x
- Bibliotecas Python: Selenium, Pandas

## Configuração

Certifique-se de ter o Python e as bibliotecas mencionadas instaladas em seu ambiente de desenvolvimento. Você também precisa de um driver do Chrome para o Selenium. Este script foi desenvolvido e testado em um ambiente Windows.

## Utilização

1. Clone este repositório em seu ambiente local.
2. Execute o script `download_dados.py` para baixar os dados do Ministério da Cultura.
3. Execute os scripts `transformar_dado_silver.py` e `transformar_dado_gold.py` para transformar os dados em formatos intermediários e consolidados, respectivamente.

### download_dados.py

Este script é responsável por fazer o download dos dados do Ministério da Cultura para o seu computador. Ele faz uso da biblioteca Selenium para automatizar o processo de navegação e download dos arquivos. Você precisa especificar o intervalo de anos e o tipo de pessoa (pessoa física ou jurídica).

Exemplo de uso:

```python
download_arquivo(2018, 2020, "Pessoa Jurídica")
