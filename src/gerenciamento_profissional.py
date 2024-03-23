import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Função para criar o banco de dados e a tabela de profissionais, se necessário

def criar_banco_dados():
    # Verificar se o arquivo do banco de dados já existe
    if not os.path.exists('profissionais.db'):
        # Se o arquivo não existir, criar o banco de dados e a tabela de usuários
        conn = sqlite3.connect('profissionais.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        crm INTEGER NOT NULL,
                        especialidade TEXT NOT NULL,
                        cpf TEXT NOT NULL,
                        usuario TEXT NOT NULL UNIQUE,
                        senha TEXT NOT NULL)''')
        conn.commit()
        conn.close()
        
criar_banco_dados()

# Função para registrar um novo usuário no banco de dados
def registrar_usuario():
    nome = nome_entry.get()
    crm = crm_entry.get()
    especialidade = especialidade_entry.get()
    cpf = cpf_entry.get()
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('profissionais.db')
    cursor = conn.cursor()
    
    # Verificar se o usuário já existe no banco de dados
    cursor.execute("INSERT INTO usuarios (nome, crm, especialidade, cpf, usuario, senha) VALUES (?, ?, ?, ?, ?, ?)",
                       (nome, crm, especialidade, cpf, usuario, senha))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    root.destroy()  # Fecha a janela de registro
        

# Cria a janela principal
root = tk.Tk()
root.title("Registro")
root.geometry("600x400")  # Define o tamanho da janela
root.configure(bg="#03045e")  # Cor de fundo da janela

# Define as cores e fonte
label_fg = "#0077b6"  # Cor do texto
entry_bg = "#00b4d8"  # Cor de fundo dos campos de entrada
button_bg = "#90e0ef"  # Cor de fundo dos botões
font_label = ("Arial", 12)
font_entry = ("Arial", 10)

# Cria o frame para o conteúdo
frame = tk.Frame(root, bg="#caf0f8")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Cria os widgets
tk.Label(frame, text="Registro de Usuário", font=font_label, bg="#caf0f8", fg=label_fg).pack(pady=10)
tk.Label(frame, text="Nome:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
nome_entry = tk.Entry(frame, font=font_entry, bg=entry_bg)
nome_entry.pack(pady=5)
tk.Label(frame, text="CRM:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
crm_entry = tk.Entry(frame, font=font_entry, bg=entry_bg)
crm_entry.pack(pady=5)
tk.Label(frame, text="Especialidade:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
especialidade_entry = tk.Entry(frame, font=font_entry, bg=entry_bg)
especialidade_entry.pack(pady=5)
tk.Label(frame, text="CPF:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
cpf_entry = tk.Entry(frame, font=font_entry, bg=entry_bg)
cpf_entry.pack(pady=5)
tk.Label(frame, text="Usuário:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
usuario_entry = tk.Entry(frame, font=font_entry, bg=entry_bg)
usuario_entry.pack(pady=5)
tk.Label(frame, text="Senha:", font=font_label, bg="#caf0f8", fg=label_fg).pack()
senha_entry = tk.Entry(frame, font=font_entry, bg=entry_bg, show="*")
senha_entry.pack(pady=5)
tk.Button(frame, text="Registrar", command=registrar_usuario, font=font_label, bg=button_bg).pack(pady=10)

# Executa o loop principal
root.mainloop()
