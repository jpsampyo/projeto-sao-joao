
import tkinter as tk
from tkinter import messagebox

# Pergunta e resposta correta
pergunta = "O Sol é uma estrela?"
resposta_correta = True

def verificar_resposta(resposta_usuario):
    if resposta_usuario == resposta_correta:
        messagebox.showinfo("Resultado", "Correto!")
    else:
        messagebox.showerror("Resultado", "Errado!")

# Janela principal
janela = tk.Tk()
janela.title("Jogo de Verdadeiro ou Falso")
janela.geometry("400x200")

# Título
titulo = tk.Label(
    janela,
    text="Jogo de Verdadeiro ou Falso",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Pergunta
label_pergunta = tk.Label(
    janela,
    text=pergunta,
    font=("Arial", 12)
)
label_pergunta.pack(pady=20)

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

botao_verdadeiro = tk.Button(
    frame_botoes,
    text="Verdadeiro",
    width=15,
    bg="lightgreen",
    command=lambda: verificar_resposta(True)
)
botao_verdadeiro.grid(row=0, column=0, padx=10)

botao_falso = tk.Button(
    frame_botoes,
    text="Falso",
    width=15,
    bg="salmon",
    command=lambda: verificar_resposta(False)
)
botao_falso.grid(row=0, column=1, padx=10)

janela.mainloop()
