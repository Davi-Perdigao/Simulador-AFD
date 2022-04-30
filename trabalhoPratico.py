import re
from numpy import append

#Lendo o arquivo informado pelo usuário
#Criando o autômato a partir do arquivo
#Retornando uma lista com todos os dados do automato
def gerarAutomato(nomeArquivo):
    arquivo = open(nomeArquivo + ".txt" , 'r')
    automato = list()
    for linha in arquivo:
        linha = linha.replace("\n", "")
        automato.append(linha)
    arquivo.close()
    return automato
"""
#Lendo e retornando a primeira linha do automato 
def lerPrimeiraLinha(automato):
    primeiraLinha = re.split(" ", automato[0])
    return primeiraLinha
"""
#Recebendo o automanto, separando seus estados e retornando-os
def separarEstados(automato):
    estados = []
    estados = re.split(" ", automato[1])
    return estados
"""
#Recebendo o automato e separando seu alfabeto
def separarAlfabeto(automato):
    alfabeto = []
    alfabeto = re.split(" ", automato[2]) #O alfabeto está na linha 2
    return alfabeto
"""
#Recebendo o automato e separando seu estado inicial
def separarEstadoInicial(automato):
    estadoInicial = automato[3] #O estado inicial está na linha 3
    return estadoInicial

#Recebendo o automato e separando seus estados finais
def separarEstadosFinais(automato):
    estadoFinal = []
    estadoFinal = re.split(" ", automato[4]) #Os estados finais estão na linha 4
    return estadoFinal

#Recebendo o automato e separando suas transições
def lerRegrasDeTransicao(automato):
	regras = {} #Criando o dicionário 
	#Percorrendo as informações do afd a partir da linha 5
	#Adicionando as informações ao dicionário
	for i in range(5, len(automato)):
		items = automato[i].split(" ")
		index = items[0] + " " + items[2]
		regras[index] = items[1]
	return regras

def verificarPalavra(estadoInicial, estadosFinais, transicoes, palavra):
    validacao = False
    estadoAtual = estadoInicial
    tamanho = len(palavra)
    try:
        for i in range(tamanho):
            estadoAtual = transicoes[estadoAtual + " " + palavra[i]]
            #print(str((i + 1)) + "° posicao - Estado atual: " + estadoAtual)
    except:
        validacao = -1
    
    if estadoAtual in estadosFinais:
        validacao = True

    #print("Palavra: " + palavra)
    #print("Estado final: " + estadoAtual)      
    #print("Validacao: " + str(validacao))
    return validacao, estadoAtual

def main():
    nomeArquivo = input("Informe o nome do arquivo: ")
    automato = gerarAutomato(nomeArquivo)
    #primeiraLinha= lerPrimeiraLinha(automato)
    estados = separarEstados(automato)
    #alfabeto = separarAlfabeto(automato)
    estadoInicial = separarEstadoInicial(automato)
    estadosFinais = separarEstadosFinais(automato)
    transicoes = lerRegrasDeTransicao(automato)
    palavra = input("Informe a palavra: ")
    validacao, estadoFinal =  verificarPalavra(estadoInicial, estadosFinais, transicoes, palavra)
    print()
    if validacao == True:
        print("Estado Final: " + estadoFinal)
        print("O automato reconhece a palavra " + palavra)
    elif validacao == False:
        print("Estado Final: " + estadoFinal)
        print("O automato não reconhece a palavra " + palavra)
    else: 
        print("ERRO")
        print("Uma letra da palavra não existe no alfabeto")

main()