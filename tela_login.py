import tkinter as tk
from tkinter import messagebox
import os
import sqlite3


# Função para abrir a tela de registro
def abrir_tela_registro():
    os.system('python registro.py')

# Função para fazer login
def fazer_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Verificar se o usuário e a senha correspondem aos registros no banco de dados
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        os.system('python area_cliente.py')
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")
    conn.close()

# Cria a janela principal
root = tk.Tk()
root.title("Login")
root.geometry("600x400")  # Define o tamanho da janela
root.configure(bg="#03045e")  # Cor de fundo da janela

# Cria o frame para o conteúdo
frame = tk.Frame(root, bg="#caf0f8")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Cria os widgets
tk.Label(frame, text="Login", font=("Arial", 20), bg="#caf0f8", fg="#0077b6").pack(pady=10)
tk.Label(frame, text="Usuário:", font=("Arial", 12), bg="#caf0f8", fg="#0077b6").pack()
usuario_entry = tk.Entry(frame, font=("Arial", 10), bg="#00b4d8")
usuario_entry.pack(pady=5)
tk.Label(frame, text="Senha:", font=("Arial", 12), bg="#caf0f8", fg="#0077b6").pack()
senha_entry = tk.Entry(frame, font=("Arial", 10), bg="#00b4d8", show="*")
senha_entry.pack(pady=5)
tk.Button(frame, text="Login", command=fazer_login, font=("Arial", 12), bg="#90e0ef").pack(pady=10)
tk.Button(frame, text="Registrar", command=abrir_tela_registro, font=("Arial", 12), bg="#90e0ef").pack(pady=10)

# Executa o loop principal
root.mainloop()
