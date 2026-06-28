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

# Usuário informa o nome
nome = str(input("Qual seu nome? "))
print(f"Seja bem vindo {nome} ao São João da Diversidade")
# Explicação das regras
print("O jogo de Verdadeiro ou Falso começou. O jogo tem 12 peguntas objetivas, sendo 4 fáceis, 4 Médias e 4 Difíceis.")
print("Responda com (1) ou (V) para Verdadeiro ou (2) ou (F) para Falso.")
# PERGUNTAS (Verdadeiro ou Falso)

while True:
# PERGUNTAS FÁCEIS

    print("A quadrilha é uma dança típica das festas juninas?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 2
    else:
        pontos = pontos - 1
        
        print("✅ Verdadeiro")
        print("Explicação: A quadrilha é uma das principais atrações das festas juninas.")

    print("O São João é comemorado tradicionalmente no mes de junho?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 2
    else:
        pontos = pontos - 1

        print("✅ Verdadeiro")
        print("Explicação: O São João faz parte das festas juninas realizadas em junho.")

    print("A fogueira junina surgiu originalmente para iluminar apresentações de quadrilha?")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 2
    else:
        pontos = pontos - 1

        print("❌ Falso")
        print("Explicação: A tradição da fogueira está ligada a celebrações religiosas.")

    print("O milho é usado em várias comidas típicas do São João?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 2
    else:
        pontos = pontos - 1

        print("✅ Verdadeiro")
        print("Explicação: Pamonha, canjica e bolo de milho são exemplos.")

# PERGUNTAS MÉDIAS
    print("A Festa Junina brasileira teve origem exclusivamente no Brasil?")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 4
    else:
        pontos = pontos - 2

        print("❌ Falso")
        print("Explicação: A tradição veio da Europa, especialmente de Portugal, e foi adaptada com elementos da cultura brasileira.")
    
    print("A canjica recebe o mesmo nome em todas as regiões do Brasil?")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 4
    else:
        pontos = pontos - 2

        print("❌ Falso")
        print("Explicação: Dependendo da região, ela pode ser chamada de canjica ou mungunzá.")
    
    print("No Nordeste, é comum que as festas juninas sejam consideradas tão importantes quanto o Carnaval em algumas cidades?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 4
    else:
        pontos = pontos - 2

        print("✅ Verdadeiro")
        print("Explicação: Em muitas cidades nordestinas, como Caruaru e Campina Grande, o São João é a maior festa do ano.")

    print("Respeitar diferentes culturas e tradições contribui para uma convivência melhor entre as pessoas?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 4
    else:
        pontos = pontos - 2

        print("✅ Verdadeiro")
        print("Explicação: Valorizar a diversidade torna a sociedade mais acolhedora.")

# PERGUNTAS DIFÍCEIS

    print("As festas juninas no Brasil têm influências indígenas, africanas e europeias?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 6
    else:
        pontos = pontos - 3

        print("✅ Verdadeiro")
        print("Explicação: A cultura brasileira é resultado da mistura dessas influências.")
    
    print("A quadrilha junina surgiu originalmente como uma dança criada no Nordeste brasileiro?")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 6
    else:
        pontos = pontos - 3
        
        print("❌ Falso ")
        print("Explicação: Ela teve origem em danças de salão europeias e foi adaptada no Brasil.")

    print("A tradição de acender fogueiras nas festas juninas está relacionada ao anúncio do nascimento de São João Batista?")
    resposta = input()
    if resposta == "V" or resposta == "1":
        pontos = pontos + 6
    else:
        pontos = pontos - 3

        print("✅ Verdadeiro")
        print("Explicação: Segundo a tradição cristã, Isabel teria acendido uma fogueira para avisar Maria sobre o nascimento de João Batista.")

    print("Respeitar a diversidade significa concordar com todas as opiniões das outras pessoas?")
    resposta = input()
    if resposta == "F" or resposta == "2":
        pontos = pontos + 6
    else:
        pontos = pontos - 3

        print("❌ Falso ")
        print("Explicação: Respeitar a diversidade significa tratar as pessoas com dignidade, mesmo quando existem opiniões diferentes.")
    
    print(f"Parabéns! Sua pontuação foi de:{pontos}")
    jogar_novamente = input("Quer ir de novo? ")
    if jogar_novamente == "Não" or jogar_novamente == "não" or jogar_novamente == "nao" or jogar_novamente == "Nao" or jogar_novamente == "n":
        break
