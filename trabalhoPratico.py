import re
from numpy import append

# Ler o arquivo informado pelo usuário e gerar o AFD a partir dele
def gerarAutomato(nomeArquivo):
    try:
        arquivo = open(nomeArquivo + ".txt" , 'r') # Lendo o arquivo informado pelo usuário
        automato = list()
        # Lendo cada linha do meu arquivo
        # Adicionando as informações do AFD a lista
        for linha in arquivo:
            linha = linha.replace("\n", "")
            automato.append(linha)
        arquivo.close()
        return automato
    except:
        return 'ERRO'
    
"""
#Lendo e retornando a primeira linha do automato 
def lerPrimeiraLinha(automato):
    primeiraLinha = re.split(" ", automato[0])
    return primeiraLinha
"""

# Recebendo o AFD, separando seus estados e retornando-os
def separarEstados(automato):
    estados = re.split(" ", automato[1]) # Os estados estão na posição 1 da lista
    return estados

# Recebendo o automato e separando seu alfabeto
def separarAlfabeto(automato):
    alfabeto = re.split(" ", automato[2]) # O alfabeto está na posicao 2 da lista
    alfabeto = set(alfabeto)
    return alfabeto

# Recebendo o AFD e separando seu estado inicial
def separarEstadoInicial(automato):
    estadoInicial = automato[3] # O estado inicial está na a posicao 3 da lista
    return estadoInicial

# Recebendo o AFD e separando seus estados finais
def separarEstadosFinais(automato):
    estadoFinal = re.split(" ", automato[4]) # Os estados finais estão a posicao 4 da lista
    return estadoFinal

# Recebendo o AFD e separando suas transições
def lerRegrasDeTransicao(automato):
	transicoes = {}
	# Percorrendo as informações do AFD a partir da linha 5
	for i in range(5, len(automato)):
		items = automato[i].split(" ") # Lendo a linha do arquivo e adiconando a lista
		index = items[0] + " " + items[2] # Definindo a chave para o dicionário
		transicoes[index] = items[1] # Adicionando as informações ao dicionário
	return transicoes

# Verificando se a palavra informada pelo usuário é reconhecida ou não pelo AFD
def verificarPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra):
    validacao = False # Usada para o retorno do resultado da verificação
    estadoAtual = estadoInicial
    # Percorrendo cada letra da minha palavra
    for letra in palavra:
        # Verificando se a letra está contida no alfabeto
        # Caso esteja, irá atualizar o estado atual do AFD
        # Caso não esteja, irá retornar -1 signifcando que houve um erro
        if letra in alfabeto:
            estadoAtual = transicoes[estadoAtual + " " + letra]
        else:
            return -1
    # Verificando se o estadoAtual existe na lista de estados finais
    # Caso exista, o AFD reconhece a palavra  
    if estadoAtual in estadosFinais:
        validacao = True
    return validacao

def mostrarResultado(resultadoValidacao, palavra):
    print()
    # Se o AFD reconheceu a palavra
    if resultadoValidacao == True:
        print("O automato reconhece a palavra " + palavra)
    # Se o AFD não reconheceu a palavra
    elif resultadoValidacao == False:
        print("O automato não reconhece a palavra " + palavra)
    # Se houve um erro na verificação da palavra
    else: 
        print("ERRO")
        print("Uma letra da palavra não existe no alfabeto")

def main():
    nomeArquivo = input("Informe o nome do arquivo: ")
    automato = gerarAutomato(nomeArquivo)
    if automato!='ERRO':
        #primeiraLinha= lerPrimeiraLinha(automato)
        #estados = separarEstados(automato)
        alfabeto = separarAlfabeto(automato)
        estadoInicial = separarEstadoInicial(automato)
        estadosFinais = separarEstadosFinais(automato)
        transicoes = lerRegrasDeTransicao(automato)
        palavra = input("Informe a palavra: ")
        resultadoValidacao =  verificarPalavra(alfabeto, estadoInicial, estadosFinais, transicoes, palavra)
        mostrarResultado(resultadoValidacao, palavra)
    else:
        print("Por favor, informe um arquivo válido")
    
main()