import tkinter as tk
from tkinter import messagebox

# ==========================
# Perguntas
# ==========================

perguntas = [
    # Fácil
    ("A quadrilha é uma dança típica das festas juninas?", True,
     "A quadrilha é uma das principais atrações das festas juninas.", 2, -1),

    ("O São João é comemorado tradicionalmente no mês de junho?", True,
     "O São João faz parte das festas juninas realizadas em junho.", 2, -1),

    ("A fogueira junina surgiu originalmente para iluminar apresentações de quadrilha?", False,
     "A tradição da fogueira está ligada a celebrações religiosas.", 2, -1),

    ("O milho é usado em várias comidas típicas do São João?", True,
     "Pamonha, canjica e bolo de milho são exemplos.", 2, -1),

    # Média
    ("A Festa Junina brasileira teve origem exclusivamente no Brasil?", False,
     "A tradição veio da Europa, especialmente de Portugal.", 4, -2),

    ("A canjica recebe o mesmo nome em todas as regiões do Brasil?", False,
     "Dependendo da região, pode ser chamada de mungunzá.", 4, -2),

    ("No Nordeste, as festas juninas são tão importantes quanto o Carnaval em algumas cidades?", True,
     "Em cidades como Campina Grande e Caruaru, o São João é a maior festa do ano.", 4, -2),

    ("Respeitar diferentes culturas contribui para uma convivência melhor?", True,
     "Valorizar a diversidade torna a sociedade mais acolhedora.", 4, -2),

    # Difícil
    ("As festas juninas têm influências indígenas, africanas e europeias?", True,
     "A cultura brasileira é resultado dessa mistura.", 6, -3),

    ("A quadrilha surgiu originalmente no Nordeste brasileiro?", False,
     "Ela surgiu na Europa e foi adaptada no Brasil.", 6, -3),

    ("A tradição da fogueira está relacionada ao nascimento de São João Batista?", True,
     "Segundo a tradição cristã, Isabel acendeu uma fogueira para avisar Maria.", 6, -3),

    ("Respeitar a diversidade significa concordar com todas as opiniões?", False,
     "Respeitar é tratar as pessoas com dignidade mesmo com opiniões diferentes.", 6, -3),
]

indice = 0
pontos = 0

# ==========================
# Funções
# ==========================


def responder(resposta):
    global indice, pontos

    pergunta, correta, explicacao, ganho, perda = perguntas[indice]

    if resposta == correta:
        pontos += ganho
        resultado = "✅ Correto!"
    else:
        pontos += perda
        resultado = "❌ Errado!"

    messagebox.showinfo(resultado, explicacao)

    indice += 1

    if indice < len(perguntas):
        atualizar_pergunta()
    else:
        fim_jogo()


def atualizar_pergunta():
    lbl_pergunta.config(
        text=f"Pergunta {indice+1}/{len(perguntas)}\n\n{perguntas[indice][0]}"
    )
    lbl_pontos.config(text=f"Pontos: {pontos}")


def fim_jogo():
    lbl_pergunta.config(text=f"Fim do jogo!\n\nPontuação: {pontos}")
    lbl_pontos.config(text=f"Pontos finais: {pontos}")

    btn_v.config(state="disabled")
    btn_f.config(state="disabled")

    if messagebox.askyesno("Jogar novamente?", "Deseja jogar novamente?"):
        reiniciar()


def reiniciar():
    global indice, pontos

    indice = 0
    pontos = 0

    btn_v.config(state="normal")
    btn_f.config(state="normal")

    atualizar_pergunta()

# ==========================
# Nome do jogador
# ==========================


def iniciar():
    nome = entrada_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite seu nome.")
        return

    tela_nome.destroy()

    global janela, lbl_pergunta, lbl_pontos, btn_v, btn_f

    janela = tk.Tk()
    janela.title("São João da Diversidade")
    janela.geometry("700x450")
    janela.configure(bg="#FFF8DC")

    tk.Label(
        janela,
        text=f"Bem-vindo(a), {nome}!",
        font=("Arial", 18, "bold"),
        bg="#FFF8DC"
    ).pack(pady=10)

    lbl_pergunta = tk.Label(
        janela,
        text="",
        font=("Arial", 15),
        wraplength=650,
        bg="#FFF8DC"
    )
    lbl_pergunta.pack(pady=20)

    lbl_pontos = tk.Label(
        janela,
        text="Pontos: 0",
        font=("Arial", 14),
        bg="#FFF8DC"
    )
    lbl_pontos.pack()

    frame = tk.Frame(janela, bg="#FFF8DC")
    frame.pack(pady=20)

    btn_v = tk.Button(
        frame,
        text="✅ Verdadeiro",
        font=("Arial", 14),
        bg="green",
        fg="white",
        width=15,
        command=lambda: responder(True)
    )
    btn_v.grid(row=0, column=0, padx=20)

    btn_f = tk.Button(
        frame,
        text="❌ Falso",
        font=("Arial", 14),
        bg="red",
        fg="white",
        width=15,
        command=lambda: responder(False)
    )
    btn_f.grid(row=0, column=1, padx=20)

    atualizar_pergunta()

    janela.mainloop()

# ==========================
# Tela inicial
# ==========================


tela_nome = tk.Tk()
tela_nome.title("São João da Diversidade")
tela_nome.geometry("450x250")
tela_nome.configure(bg="#FFF8DC")

tk.Label(
    tela_nome,
    text="São João da Diversidade",
    font=("Arial", 18, "bold"),
    bg="#FFF8DC"
).pack(pady=15)

tk.Label(
    tela_nome,
    text="Digite seu nome:",
    font=("Arial", 12),
    bg="#FFF8DC"
).pack()

entrada_nome = tk.Entry(tela_nome, font=("Arial", 12))
entrada_nome.pack(pady=10)

tk.Button(
    tela_nome,
    text="Iniciar Jogo",
    font=("Arial", 12),
    bg="orange",
    command=iniciar
).pack(pady=15)

tela_nome.mainloop()
