#Atividade 1
# import tkinter as tk
# from tkinter import messagebox, ttk

# def bemvindo():
#     operador_nome= nome_operador.get()
#     turno_operador = operador_turno.get()

#     if operador_nome == "" or turno_operador == "":
#         messagebox.showwarning(
#             "Aviso",
#             "Por favor digite seu turno e nome de operador!"
#         )
#     else:
#         messagebox.showinfo(
#             "Boa jornada",
#             f"Operador: {operador_nome}!\n"
#             f"Registrado no turno: {turno_operador} anos\n"
#             )
        
# janela_bemvindo = tk.Tk()
# janela_bemvindo.title("Saudações do Operador")
# janela_bemvindo.geometry("500x500")

# lbl_mensagem_usuario = tk.Label(
#     janela_bemvindo,
#     text="Digite o nome do Operador:"
# )
# lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

# nome_operador = tk.Entry(
#     janela_bemvindo,
#     font=("Arial", 12),
#     width=20
# )
# nome_operador.grid(row=0, column=1, pady=10, padx=10)

# lbl_mensagem_idade = tk.Label(
#     janela_bemvindo,
#     text="Digite o seu turno:"
# )
# lbl_mensagem_idade.grid(row=1, column=0, pady=10, padx=10)

# operador_turno = tk.Entry(
#     janela_bemvindo,
#     font=("Arial", 12),
#     width=20
# )
# operador_turno.grid(row=1, column=1, pady=10, padx=10)
# btn_enviar_mensagem = tk.Button(
#     janela_bemvindo,
#     text="Enviar Mensagem",
#     command=bemvindo
# )
# btn_enviar_mensagem.grid(row=3, column=0, pady=10, padx=10)

# btn_fechar_janela = tk.Button(
#     janela_bemvindo,
#     text="Fechar Janela",
#     command=janela_bemvindo.destroy
# )
# btn_fechar_janela.grid(row=4, column=0, columnspan=2, pady=10)

# janela_bemvindo.mainloop()

#Atividade 2
# import tkinter as tk
# from tkinter import messagebox

# def calcular():
#     pecas = int(entry_pecas.get())
#     total = pecas * 8

#     messagebox.showinfo(
#         "Resultado",
#         f"Em 8 horas serão produzidas {total} peças."
#     )

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("300x150")

# tk.Label(janela, text="Peças produzidas por hora:").pack()
# entry_pecas = tk.Entry(janela)
# entry_pecas.pack()

# tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

# janela.mainloop()

#Atividade 3
# import tkinter as tk
# from tkinter import messagebox

# def converter():
#     bar = float(coloque_bar.get())
#     psi = bar * 14.5

#     messagebox.showinfo(
#         "Resultado",
#         f"Pressão: {psi:.2f} PSI"
#     )

# janela = tk.Tk()
# janela.title("Conversor de Unidade")
# janela.geometry("300x150")

# tk.Label(janela, text="Pressão em Bar:").pack()
# coloque_bar = tk.Entry(janela)
# coloque_bar.pack()

# tk.Button(janela, text="Converter", command=converter).pack(pady=10)

# janela.mainloop()

#Atividade 4
# import tkinter as tk
# from tkinter import messagebox

# def calcular():
#     n1 = float(peca_n1.get())
#     n2 = float(peca_n2.get())
#     n3 = float(peca_n3.get())

#     media = (n1 + n2 + n3) / 3

#     messagebox.showinfo(
#         "Média",
#         f"Média = {media:.2f}"
#     )

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("300x250")

# tk.Label(janela, text="Nota 1").pack()
# peca_n1 = tk.Entry(janela)
# peca_n1.pack()

# tk.Label(janela, text="Nota 2").pack()
# peca_n2 = tk.Entry(janela)
# peca_n2.pack()

# tk.Label(janela, text="Nota 3").pack()
# peca_n3 = tk.Entry(janela)
# peca_n3.pack()

# tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

# janela.mainloop()

#Atividade 5
# import tkinter as tk
# from tkinter import messagebox, ttk

# def verificar():
#     temp = float(coloque_tempo.get())

#     if temp < 40:
#         resultado = "Baixa carga"
#     elif temp <= 70:
#         resultado = "Normal"
#     else:
#         resultado = "ALERTA: Resfriamento Ativado!"

#     messagebox.showinfo("Resultado", resultado)

# janela = tk.Tk()
# janela.title("Termostato")
# janela.geometry("300x150")

# tk.Label(janela, text="Temperatura do motor").pack()
# coloque_tempo = tk.Entry(janela)
# coloque_tempo.pack()

# tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

# janela.mainloop()

#Atividade 6
# import tkinter as tk
# from tkinter import messagebox, ttk

# def classificar():
#     codigo = entry_codigo.get()

#     if codigo.startswith("A"):
#         resultado = "Alimentos"
#     elif codigo.startswith("E"):
#         resultado = "Eletrônicos"
#     else:
#         resultado = "Desconhecido"

#     messagebox.showinfo("Resultado", resultado)

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("300x150")

# tk.Label(janela, text="Código do produto").pack()
# entry_codigo = tk.Entry(janela)
# entry_codigo.pack()

# tk.Button(janela, text="Classificar", command=classificar).pack(pady=10)

# janela.mainloop()

#Atividade 7
# import tkinter as tk
# from tkinter import messagebox

# def verificar():
#     porta = inserir_porta.get()
#     emergencia = inserir_emergencia.get()

#     if porta == "Fechada" and emergencia == "desligado":
#         resultado = "A Máquina pode iniciar."
#     else:
#         resultado = "A Máquina não pode iniciar."

#     messagebox.showinfo("Resultado", resultado)

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("300x200")

# tk.Label(janela, text="Porta (Fechada/Aberta)").pack()
# inserir_porta = tk.Entry(janela)
# inserir_porta.pack()

# tk.Label(janela, text="Emergência (ligado/desligado)").pack()
# inserir_emergencia = tk.Entry(janela)
# inserir_emergencia.pack()

# tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

# janela.mainloop()

#Atividade 8
# import tkinter as tk
# from tkinter import messagebox, ttk

# def verificar():
#     total = int(tudo_total.get())
#     defeituosas = int(pecas_defeituosas.get())

#     porcentagem = (defeituosas / total) * 100

#     if porcentagem > 5:
#         resultado = "Revisar Processo"
#     else:
#         resultado = "Processo Otimizado"

#     messagebox.showinfo("Resultado", resultado)

# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("300x200")

# tk.Label(janela, text="Total de peças").pack()
# tudo_total = tk.Entry(janela)
# tudo_total.pack()

# tk.Label(janela, text="Peças defeituosas").pack()
# pecas_defeituosas = tk.Entry(janela)
# pecas_defeituosas.pack()

# tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

# janela.mainloop()

#Atividade 9
import tkinter as tk
from tkinter import messagebox, ttk

def 