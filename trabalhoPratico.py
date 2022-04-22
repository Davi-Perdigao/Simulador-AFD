import re
from numpy import append

def lerArquivo():
    arquivo = open('arquivo.txt', 'r')
    afd = list()
    #afd = arquivo.readlines()
    for linha in arquivo:
        linha = linha.replace("\n", "")
        afd.append(linha)
    arquivo.close()
    return afd

def lerPrimeiraLinha():
    primeiraLinha = re.split(" ", automato[0])
    return primeiraLinha

def separarEstados(afd):
    estados = []
    estados = re.split(" ", afd[1])
    return estados

def separarAlfabeto(afd):
    alfabeto = []
    alfabeto = re.split(" ", afd[2])
    return alfabeto

def separarEstadoInicial(afd):
    estadoInicial = afd[3]
    return estadoInicial

def separarEstadosFinais(afd):
    estadoFinal = []
    estadoFinal = re.split(" ", afd[4])
    return estadoFinal
"""
def separarTransicoes(afd):
    #qtdEstados = len(separarEstados(afd))
    #qtdAlfabeto = len(separarAlfabeto(afd))
    transicoes = []
    posicao = 5     
    while True:
        if afd[posicao] == " ":
            return transicoes
        else:
            transicoes.append(afd[posicao])
            posicao +=1 
"""

automato = lerArquivo()
primeiraLinha = []
primeiraLinha = lerPrimeiraLinha()
estados = separarEstados(automato)
alfabeto = separarAlfabeto(automato)
estadoInicial = separarEstadoInicial(automato)
estadoFinal = separarEstadosFinais(automato)
#transicoes = separarTransicoes(automato)
print(automato)
print(primeiraLinha)
print(estados)
print(alfabeto)
print(estadoInicial)
print(estadoFinal)
#print(transicoes)




