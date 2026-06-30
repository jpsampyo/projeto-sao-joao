import tkinter as tk
from tkinter import messagebox

# ==========================
# Perguntas
# ==========================

perguntas = [
    # Fácil (Total: 8 pontos)
    ("A quadrilha é uma dança típica das festas juninas?", True,
     "A quadrilha é uma das principais atrações das festas juninas.", 2, -1),

    ("O São João é comemorado tradicionalmente no mês de junho?", True,
     "O São João faz parte das festas juninas realizadas em junho.", 2, -1),

    ("A fogueira junina surgiu originalmente para iluminar apresentações de quadrilha?", False,
     "A tradição da fogueira está ligada a celebrações religiosas.", 2, -1),

    ("O milho é usado em várias comidas típicas do São João?", True,
     "Pamonha, canjica e bolo de milho são exemplos.", 2, -1),

    # Média (Total: 16 pontos)
    ("A Festa Junina brasileira teve origem exclusivamente no Brasil?", False,
     "A tradição veio da Europa, especialmente de Portugal.", 4, -2),

    ("A canjica recebe o mesmo nome em todas as regiões do Brasil?", False,
     "Dependendo da região, pode ser chamada de mungunzá.", 4, -2),

    ("No Nordeste, as festas juninas são tão importantes quanto o Carnaval em algumas cidades?", True,
     "Em cidades como Campina Grande e Caruaru, o São João é a maior festa do ano.", 4, -2),

    ("Respeitar diferentes culturas contribui para uma convivência melhor?", True,
     "Valorizar a diversidade torna a sociedade mais acolhedora.", 4, -2),

    # Difícil (Total: 24 pontos)
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
# Funções de Fluxo e Design
# ==========================

def mostrar_feedback_customizado(correto, explicacao, pontos_ganhos):
    """Cria uma janela de feedback bonita e centralizada."""
    btn_v.config(state="disabled")
    btn_f.config(state="disabled")

    popup = tk.Toplevel(janela)
    popup.title("Resultado")
    popup.geometry("500x350")
    popup.configure(bg="#FFF8DC")
    
    popup.transient(janela)
    popup.grab_set()
    
    popup.update_idletasks()
    largura = popup.winfo_width()
    altura = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (largura // 2)
    y = (popup.winfo_screenheight() // 2) - (altura // 2)
    popup.geometry(f"+{x}+{y}")

    cor_topo = "#2E7D32" if correto else "#C62828"
    texto_titulo = "✨ CORRETO! ✨" if correto else "❌ ERRADO! ❌"
    texto_pontos = f"+{pontos_ganhos} pontos!" if correto else f"{pontos_ganhos} pontos"

    header = tk.Frame(popup, bg=cor_topo, height=70)
    header.pack(fill="x")
    header.pack_propagate(False)
    
    tk.Label(
        header, 
        text=texto_titulo, 
        font=("Arial", 18, "bold"), 
        fg="white", 
        bg=cor_topo
    ).pack(pady=15)

    tk.Label(
        popup, 
        text=texto_pontos, 
        font=("Arial", 16, "bold"), 
        fg=cor_topo, 
        bg="#FFF8DC"
    ).pack(pady=15)

    tk.Label(
        popup, 
        text=explicacao, 
        font=("Arial", 14, "italic"), 
        fg="#3E2723", 
        bg="#FFF8DC", 
        wraplength=450,
        justify="center"
    ).pack(pady=15, padx=20)

    def proxima_pergunta():
        popup.destroy()
        btn_v.config(state="normal")
        btn_f.config(state="normal")
        
        global indice
        indice += 1
        if indice < len(perguntas):
            atualizar_pergunta()
        else:
            fim_jogo()

    btn_continuar = tk.Button(
        popup, 
        text="Continuar ➔", 
        font=("Arial", 12, "bold"), 
        bg="#FF9800", 
        fg="white", 
        activebackground="#F57C00",
        activeforeground="white",
        bd=0,
        padx=25,
        pady=8,
        command=proxima_pergunta
    )
    btn_continuar.pack(side="bottom", pady=25)


def responder(resposta):
    global pontos

    pergunta, correta, explicacao, ganho, perda = perguntas[indice]

    if resposta == correta:
        pontos += ganho
        mostrar_feedback_customizado(True, explicacao, ganho)
    else:
        pontos += perda
        mostrar_feedback_customizado(False, explicacao, perda)


def atualizar_pergunta():
    lbl_pergunta.config(
        text=f"Pergunta {indice+1}/{len(perguntas)}\n\n{perguntas[indice][0]}"
    )
    lbl_pontos.config(text=f"Pontos: {pontos}")


def fim_jogo():
    """Finaliza a partida exibindo o status de conquista e o botão de retorno."""
    btn_v.pack_forget()  # Esconde o botão verdadeiro
    btn_f.pack_forget()  # Esconde o botão falso
    
    # Meta definida pelo usuário
    meta_pontos = 25
    total_maximo = sum(p[3] for p in perguntas) # Soma dinâmica do ganho máximo (36 pts)
    
    # Determina se o jogador bateu a meta
    if pontos >= meta_pontos:
        cor_status = "#2E7D32"  # Verde
        status_texto = f"🎉 PARABÉNS! Você conseguiu!\nBateu a meta de {meta_pontos} pontos."
    else:
        cor_status = "#D32F2F"  # Vermelho
        status_texto = f"🔥 Quase lá! Você não atingiu os {meta_pontos} pontos necessários.\nTente novamente!"

    # Atualiza a tela principal com o painel de resultado final
    lbl_pergunta.config(
        text=f"Fim do jogo!\n\nSua Pontuação: {pontos} / {total_maximo} pontos possíveis.",
        font=("Arial", 22, "bold"),
        fg="#3E2723"
    )
    
    lbl_pontos.config(
        text=status_texto,
        font=("Arial", 18, "bold"),
        fg=cor_status
    )

    # Cria o botão temático para voltar ao menu (substituindo os de Verdadeiro/Falso)
    btn_voltar = tk.Button(
        frame_botoes,
        text="↩ Voltar ao Menu Principal",
        font=("Arial", 14, "bold"),
        bg="#FF9800",
        fg="white",
        activebackground="#F57C00",
        activeforeground="white",
        padx=20,
        pady=10,
        bd=0,
        command=voltar_ao_menu
    )
    btn_voltar.pack(pady=20)


def voltar_ao_menu():
    """Fecha a janela do jogo e reabre o menu inicial."""
    janela.destroy()
    criar_menu_principal()


def iniciar():
    nome = entrada_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite seu nome.")
        return

    tela_nome.destroy()

    global janela, lbl_pergunta, lbl_pontos, btn_v, btn_f, frame_botoes, indice, pontos

    indice = 0
    pontos = 0

    janela = tk.Tk()
    janela.title("São João da Diversidade")
    janela.configure(bg="#FFF8DC")
    janela.state('zoomed') 

    container = tk.Frame(janela, bg="#FFF8DC")
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        container,
        text=f"Bem-vindo(a), {nome}!",
        font=("Arial", 24, "bold"),
        bg="#FFF8DC",
        fg="#3E2723"
    ).pack(pady=20)

    lbl_pergunta = tk.Label(
        container,
        text="",
        font=("Arial", 20),
        wraplength=800, 
        bg="#FFF8DC",
        fg="#3E2723",
        justify="center"
    )
    lbl_pergunta.pack(pady=40)

    lbl_pontos = tk.Label(
        container,
        text="Pontos: 0",
        font=("Arial", 18, "bold"),
        bg="#FFF8DC",
        fg="#E65100"
    )
    lbl_pontos.pack()

    frame_botoes = tk.Frame(container, bg="#FFF8DC")
    frame_botoes.pack(pady=40)

    btn_v = tk.Button(
        frame_botoes,
        text="✅ Verdadeiro",
        font=("Arial", 16, "bold"),
        bg="#4CAF50",
        fg="white",
        width=18,
        height=2,
        bd=2,
        relief="groove",
        command=lambda: responder(True)
    )
    btn_v.pack(side="left", padx=30)

    btn_f = tk.Button(
        frame_botoes,
        text="❌ Falso",
        font=("Arial", 16, "bold"),
        bg="#F44336",
        fg="white",
        width=18,
        height=2,
        bd=2,
        relief="groove",
        command=lambda: responder(False)
    )
    btn_f.pack(side="left", padx=30)

    atualizar_pergunta()
    janela.mainloop()


def criar_menu_principal():
    global tela_nome, entrada_nome
    
    tela_nome = tk.Tk()
    tela_nome.title("São João da Diversidade")
    tela_nome.configure(bg="#FFF8DC")
    tela_nome.state('zoomed')

    container_menu = tk.Frame(tela_nome, bg="#FFF8DC")
    container_menu.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        container_menu,
        text="São João da Diversidade",
        font=("Arial", 32, "bold"),
        bg="#FFF8DC",
        fg="#E65100"
    ).pack(pady=30)

    tk.Label(
        container_menu,
        text="Digite seu nome para começar:",
        font=("Arial", 16),
        bg="#FFF8DC",
        fg="#3E2723"
    ).pack(pady=10)

    entrada_nome = tk.Entry(container_menu, font=("Arial", 18), justify="center", width=25)
    entrada_nome.pack(pady=15)

    tk.Button(
        container_menu,
        text="Iniciar Jogo ➔",
        font=("Arial", 14, "bold"),
        bg="#FF9800",
        fg="white",
        activebackground="#F57C00",
        activeforeground="white",
        bd=0,
        padx=30,
        pady=10,
        command=iniciar
    ).pack(pady=25)

    tela_nome.mainloop()


# ==========================
# Inicialização do Programa
# ==========================
if __name__ == "__main__":
    criar_menu_principal()