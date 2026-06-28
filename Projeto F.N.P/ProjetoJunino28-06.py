# Início
# Ideias de Variáveis: num1,Win,cont,num2
cont = 0
cont_tentativas = 0
pontos = 0
pontos2 = 0
diferenca = 0
pergunta = str  # CUIDADOOOO AQUI, OLHA DEPOIS
ultima_resposta = False
cont_respostas_corretas = 0

import os
import tkinter as tk
from tkinter import messagebox




#VERIRIFICAR SE O PYGAME ESTÁ INSTALADO
import pygame

# ==========================
# Inicializa o pygame
# ==========================

try:
    pygame.mixer.init()
except Exception as erro:
    print("Erro ao iniciar o áudio:", erro)

musica_ligada = True


# ==========================
# Música
# ==========================

def iniciar_musica():
    caminho_musica = "musicasaojoao.mp3"

    if os.path.exists(caminho_musica):
        try:
            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.play(-1)
        except Exception as erro:
            print("Erro ao carregar a música:", erro)
    else:
        print(f"Arquivo '{caminho_musica}' não encontrado.")


# ==========================
# Botão Começar
# ==========================

def comecar_festa():
    messagebox.showinfo(
        "Viva São João!",
        "Olha a chuva!... É mentira! 🎉\nA festa começou!"
    )


# ==========================
# Botão Mutar
# ==========================

def mutar_musica():
    global musica_ligada

    if musica_ligada:
        pygame.mixer.music.pause()
        botao_mutar.config(text="🔈 Música")
    else:
        pygame.mixer.music.unpause()
        botao_mutar.config(text="🔇 Música")

    musica_ligada = not musica_ligada


# ==========================
# Fechar janela
# ==========================

def fechar():
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass

    janela.destroy()


# ==========================
# Janela
# ==========================

janela = tk.Tk()
janela.title("Arraiá do Python 🎉")
janela.geometry("700x500")
janela.configure(bg="#1a2a6c")
janela.resizable(False, False)

# Centralizar janela
largura = 700
altura = 500

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{x}+{y}")

janela.protocol("WM_DELETE_WINDOW", fechar)

# ==========================
# Bandeirinhas
# ==========================

frame_bandeirinhas = tk.Frame(
    janela,
    bg="#1a2a6c"
)
frame_bandeirinhas.pack(fill="x", pady=15)

cores = [
    "#ff4b1f",
    "#ffb300",
    "#00b0ff",
    "#00e676",
    "#ff4081",
    "#9c27b0",
    "#ff5722"
]

for cor in cores * 4:
    tk.Label(
        frame_bandeirinhas,
        text="▲",
        font=("Arial", 22),
        fg=cor,
        bg="#1a2a6c"
    ).pack(side="left", expand=True)

# ==========================
# Título
# ==========================

titulo = tk.Label(
    janela,
    text="🔥 GRANDE ARRAIÁ 🔥",
    font=("Helvetica", 28, "bold"),
    fg="#fdbb2d",
    bg="#1a2a6c"
)
titulo.pack(pady=25)

subtitulo = tk.Label(
    janela,
    text="Seja bem-vindo ao melhor Arraiá do Python!",
    font=("Courier New", 13, "italic"),
    fg="white",
    bg="#1a2a6c"
)
subtitulo.pack()

# ==========================
# Botão Começar
# ==========================

botao_comecar = tk.Button(
    janela,
    text="🎉 ENTRAR NA FESTA 🎉",
    font=("Arial", 14, "bold"),
    bg="#ff4b1f",
    fg="white",
    activebackground="#fdbb2d",
    activeforeground="black",
    padx=20,
    pady=10,
    command=comecar_festa,
    cursor="hand2"
)

botao_comecar.pack(pady=40)

# ==========================
# Botão Música
# ==========================

botao_mutar = tk.Button(
    janela,
    text="🔇 Música",
    font=("Arial", 11, "bold"),
    bg="#00b0ff",
    fg="white",
    padx=15,
    pady=5,
    command=mutar_musica,
    cursor="hand2"
)

botao_mutar.pack()

# ==========================
# Rodapé
# ==========================

rodape = tk.Label(
    janela,
    text="🌽 Pamonha • Canjica • Milho • Quentão 🌽",
    font=("Arial", 11),
    fg="#ffb300",
    bg="#1a2a6c"
)

rodape.pack(side="bottom", pady=15)

# ==========================
# Inicia Música
# ==========================

iniciar_musica()

# ==========================
# Executa
# ==========================

janela.mainloop()

# Usuário informa o nome
nome = str(input("Qual seu nome? "))
print(f"Seja bem vindo {nome} ao São João da Diversidade")
# Explicação das regras
print("O jogo de Verdadeiro ou Falso começou. O jogo tem 12 peguntas objetivas, sendo 4 fáceis, 4 Médias e 4 Difíceis.")
# Perguntas(Verdadeiro ou Falso)
print("")

# Sistema Verifica a resposta

while True:

    print("O Sao João é a festa da colheita do milho? 1 - Verdadeiro 2 - Falso")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 1

    print("O são João é comemorado tradicionalmente no mes de junho? 1 - Verdadeiro 2 - Falso")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 1
    
    print("O Carnaval é uma festa tipica do São João")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 1
    
    print("O Carnaval é uma festa tipica do São João")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 1
    
    print("Parabens sua pontuação foi de: ", pontos)
    jogar_novamente = input("Quer ir de novo? ")
    if jogar_novamente == "Não" or jogar_novamente == "não" or jogar_novamente == "nao" or jogar_novamente == "Nao":
        break


# Mostra explicação da resposta

# Atualiza pontuação

# Resultado Final

# Fim (Parabéns Usuário)