import tkinter as tk

def escolher_profissional():
    # Função para escolher o profissional
    pass

def verificar_disponibilidade():
    # Função para verificar os horários disponíveis na agenda
    pass

def agendar():
    # Função para agendar um horário
    pass

def consultar_agendamentos():
    # Função para consultar os agendamentos do cliente
    pass

def editar_agendamento():
    # Função para editar um agendamento
    pass

def excluir_agendamento():
    # Função para excluir um agendamento
    pass

# Cria a janela principal
root = tk.Tk()
root.title("Área do Cliente")
root.geometry("600x400")  # Define o tamanho da janela
root.configure(bg="#03045e")  # Cor de fundo da janela

# Cria o frame para o conteúdo
frame = tk.Frame(root, bg="#caf0f8")
frame.pack(padx=20, pady=20)

# Define a cor dos botões
button_bg = "#90e0ef"

# Cria os botões para cada funcionalidade
btn_escolher_profissional = tk.Button(frame, text="Escolher Profissional", command=escolher_profissional, bg=button_bg)
btn_escolher_profissional.pack(fill=tk.X, pady=5)
btn_escolher_profissional = tk.Entry(frame, font=("Arial", 10), bg="#00b4d8")
btn_escolher_profissional.pack(pady=5)

btn_verificar_disponibilidade = tk.Button(frame, text="Verificar Disponibilidade", command=verificar_disponibilidade, bg=button_bg)
btn_verificar_disponibilidade.pack(fill=tk.X, pady=5)
btn_verificar_disponibilidade = tk.Entry(frame, font=("Arial", 10), bg="#00b4d8")
btn_verificar_disponibilidade.pack(pady=5)

btn_agendar = tk.Button(frame, text="Agendar", command=agendar, bg=button_bg)
btn_agendar.pack(fill=tk.X, pady=5)

btn_consultar_agendamentos = tk.Button(frame, text="Consultar Agendamentos", command=consultar_agendamentos, bg=button_bg)
btn_consultar_agendamentos.pack(fill=tk.X, pady=5)

btn_editar_agendamento = tk.Button(frame, text="Editar Agendamento", command=editar_agendamento, bg=button_bg)
btn_editar_agendamento.pack(fill=tk.X, pady=5)

btn_excluir_agendamento = tk.Button(frame, text="Excluir Agendamento", command=excluir_agendamento, bg=button_bg)
btn_excluir_agendamento.pack(fill=tk.X, pady=5)

# Executa o loop principal
root.mainloop()
