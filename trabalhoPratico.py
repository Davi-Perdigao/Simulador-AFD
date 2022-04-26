import re
from numpy import append

#Lendo o arquivo informado pelo usuário
#Criando o autômato a partir do arquivo
#Retornando uma lista com todos os dados do automato
def lerArquivo():
    arquivo = open('arquivo.txt', 'r')
    afd = list()
    for linha in arquivo:
        linha = linha.replace("\n", "")
        afd.append(linha)
    arquivo.close()
    return afd

#Lendo e retornando a primeira linha do automato 
def lerPrimeiraLinha():
    primeiraLinha = re.split(" ", automato[0])
    return primeiraLinha

#Recebendo o automanto, separando seus estados e retornando-os
def separarEstados(afd):
    estados = []
    estados = re.split(" ", afd[1])
    return estados

#Recebendo o automato e separando seu alfabeto
def separarAlfabeto(afd):
    alfabeto = []
    alfabeto = re.split(" ", afd[2]) #O alfabeto está na linha 2
    return alfabeto

#Recebendo o automato e separando seu estado inicial
def separarEstadoInicial(afd):
    estadoInicial = afd[3] #O estado inicial está na linha 3
    return estadoInicial

#Recebendo o automato e separando seus estados finais
def separarEstadosFinais(afd):
    estadoFinal = []
    estadoFinal = re.split(" ", afd[4]) #Os estados finais estão na linha 4
    return estadoFinal

#Recebendo o automato e separando suas transições
def lerRegrasDeTransicao(afd):
	regras = {} #Criando o dicionário 
	#Percorrendo as informações do afd a partir da linha 5
	#Adicionando as informações ao dicionário
	for i in range(5, len(afd)):
		items = automato[i].split(" ")
		index = items[0] + " " + items[2]
		regras[index] = items[1]
	return regras

def verificarPalavra(estadoInicial, estadoFinal, transicoes, palavra):
    validacao = False
    estadoAtual = estadoInicial
    tamanho = len(palavra)
    for i in range(tamanho):
        estadoAtual = transicoes[estadoAtual + " " + palavra[i]]
        if estadoAtual in estadoFinal and palavra=="":
            validacao = True
            

    return estadoAtual

def main():
    palavra = input("Informe a palavra: ")
    
    

automato = lerArquivo()
primeiraLinha = []
primeiraLinha = lerPrimeiraLinha()
estados = separarEstados(automato)
alfabeto = separarAlfabeto(automato)
estadoInicial = separarEstadoInicial(automato)
estadoFinal = separarEstadosFinais(automato)
transicoes = lerRegrasDeTransicao(automato)

print("Autômato = ", automato)
print("\nPrimeira Linha = ", primeiraLinha)
print("\nEstados = ", estados)
print("\nAlfabeto = ", alfabeto)
print("\nEstado Inicial = ", estadoInicial)
print("\nEstado Final = ", estadoFinal)
print("\nTransições = ", transicoes)
print(verificarPalavra(estadoInicial, estadoFinal, transicoes, '0000000'))