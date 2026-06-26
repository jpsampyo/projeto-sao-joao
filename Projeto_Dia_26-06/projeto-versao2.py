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
    
    
    print("Parabens sua pontuação foi de: ", pontos)
    jogar_novamente = input("Quer ir de novo? ")
    if jogar_novamente == "Não" or jogar_novamente == "não" or jogar_novamente == "nao" or jogar_novamente == "Nao":
        break

# Mostra explicação da resposta

# Atualiza pontuação

# Resultado Final

# Fim (Parabéns Usuário)
