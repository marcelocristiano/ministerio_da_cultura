import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
import datetime

app = ttk.Window(themename='flatly')
app.resizable(width=False, height=False)
app.iconbitmap('img/brasil.ico')
app.title('Ministerio da Cultura')
app.geometry('800x500')

def busca_dado():
    ano_ini = c_ano_ini.get()
    ano_fim = c_ano_fim.get()
    tipo_pessoa = (0 if c_tipo_pessoa.get() == 'Jurídica' else 1)

    print(ano_ini, ano_fim, tipo_pessoa)

# Carrega a imagem
image = PhotoImage(file='img/logo-govbr.png')  # Substitua com o caminho correto da sua imagem

# Cria um Label para exibir a imagem
image_label = ttk.Label(app, image=image)
image_label.pack(padx=10, pady=20)

# Criando um frame dentro da aplicação principal com borda 1
f_ano = ttk.Frame(app, border=1)
f_ano.pack()

# Criando um rótulo para "Ano Início" dentro do frame, alinhado à esquerda
l_ano_ini = ttk.Label(f_ano, text='Ano Inicio:', font=("Arial", 10))
l_ano_ini.grid(column=1, row=0, sticky='w')

# Obtendo o ano atual
ano_atual = datetime.datetime.now().year

list_ano = [x for x in range(1993, ano_atual + 1)]

# Criando uma caixa de combinação para selecionar o ano de início, alinhada à esquerda
c_ano_ini = ttk.Combobox(f_ano, width=5, values=list_ano)
c_ano_ini.grid(column=2, row=0, padx=5, pady=5, sticky='w')

# Criando um rótulo para "Ano Fim" dentro do frame, alinhado à esquerda
l_ano_fim = ttk.Label(f_ano, text='Ano Fim:', font=("Arial", 10))
l_ano_fim.grid(column=1, row=1, sticky='w')

# Criando uma caixa de combinação para selecionar o ano de fim, alinhada à esquerda
c_ano_fim = ttk.Combobox(f_ano, width=5, values=list_ano)
c_ano_fim.grid(column=2, row=1, padx=5, pady=5, sticky='w')

# Criando um rótulo para "Tipo de Pessoa" dentro do frame, alinhado à esquerda
l_tipo_pessoa = ttk.Label(f_ano, text='Tipo de Pessoa:', font=("Arial", 10))
l_tipo_pessoa.grid(column=1, row=2, sticky='w')

l_tipo_pessoa = ['Física', 'Jurídica']
# Criando uma caixa de combinação para selecionar o tipo de pessoa, alinhada à esquerda
c_tipo_pessoa = ttk.Combobox(f_ano, width=7, values=l_tipo_pessoa)
c_tipo_pessoa.grid(column=2, row=2, padx=5, pady=5, sticky='w')

# Criando um botão "Buscar" com estilo 'info' e largura 20 na aplicação principal
b1 = ttk.Button(app, text="Buscar", style='info', width=20, command=busca_dado)
b1.pack(padx=10, pady=20)

# Executando o loop principal da aplicação
if __name__ == '__main__':
    app.mainloop()
