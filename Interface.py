import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Adicione aqui sua função de busca de mais leads (pesquisas adicionais)

# Dados iniciais
data = {
    "Nome da Loja": [
        "Alana Roupas e Acessórios",
        "Roupas para Compor",
        "Nilmar Sao José",
        "Amor de Peça",
        "Loja de Roupas",
        "Nova São Paulo",
        "Projeto Gaveta",
        "Loja Divino Morro"
    ],
    "E-mail": [
        "gmail.com",
        "bossabasics@gmail.com",
        "shopnow@gmail.com",
        "amordepeca@gmail.com",
        "estark_modas@gmail.com",
        "N/A",
        "projetogaveta@gmail.com",
        "lojadivinomorro@gmail.com"
    ],
    "Telefone": [
        "(88) 996380528",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A",
        "N/A"
    ]
}

# Criação do DataFrame inicial
df = pd.DataFrame(data)

# Função para salvar o DataFrame em um arquivo Excel
def salvar_planilha():
    global df
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    df.to_excel(file_path, index=False)
    print("Planilha criada com sucesso!")

# Função para atualizar o DataFrame com novos dados conforme selecionado
def atualizar_dataframe():
    global df
    nicho = entry_nicho.get()
    plataformas = []

    if var_linkedin.get():
        plataformas.append('LinkedIn')
    if var_facebook.get():
        plataformas.append('Facebook')
    if var_twitter.get():
        plataformas.append('Twitter')
    if var_whatsapp.get():
        plataformas.append('WhatsApp')

    # Atualize o DataFrame com novos dados encontrados com base nas seleções (simulação)
    novos_dados = {
        "Nome da Loja": [f"Loja Teste {nicho}"],
        "E-mail": [f"loja.teste.{nicho}@gmail.com"],
        "Telefone": ["(00) 0000-0000"]
    }
    
    # Simulando a adição de novos dados ao DataFrame
    df_novos = pd.DataFrame(novos_dados)
    df = pd.concat([df, df_novos], ignore_index=True)

    print("Dados atualizados com sucesso!")

# Criação da interface gráfica
root = tk.Tk()
root.title("Gerador de Leads")

# Criação dos widgets da interface
label_nicho = tk.Label(root, text="Escolha o Nicho:")
label_nicho.pack()

entry_nicho = tk.Entry(root)
entry_nicho.pack()

label_plataformas = tk.Label(root, text="Escolha as Plataformas:")
label_plataformas.pack()

var_linkedin = tk.IntVar()
var_facebook = tk.IntVar()
var_twitter = tk.IntVar()
var_whatsapp = tk.IntVar()

checkbox_linkedin = tk.Checkbutton(root, text="LinkedIn", variable=var_linkedin)
checkbox_facebook = tk.Checkbutton(root, text="Facebook", variable=var_facebook)
checkbox_twitter = tk.Checkbutton(root, text="Twitter", variable=var_twitter)
checkbox_whatsapp = tk.Checkbutton(root, text="WhatsApp", variable=var_whatsapp)

checkbox_linkedin.pack()
checkbox_facebook.pack()
checkbox_twitter.pack()
checkbox_whatsapp.pack()

botao_atualizar = tk.Button(root, text="Atualizar Dados", command=atualizar_dataframe)
botao_atualizar.pack()

botao_salvar = tk.Button(root, text="Salvar Planilha", command=salvar_planilha)
botao_salvar.pack()

# Iniciar a interface gráfica
root.mainloop()
