"""
    Usando uma linguagem de alto-nível como C/C++/Java, escrever um programa que crie 30 threads e faça com que uma mensagem circule entre os mesmos.
    A mensagem é uma string aleatória de pelo menos 80 caracteres.
    A cada vez que um thread recebe a mensagem ele a imprime, modifica o primeiro caractere minúsculo para maiúsculo, caso exista, dorme por 1 segundo, e repassa a mensagem.
    Quando todos os caracteres forem maiúsculos, o processo repassa a mensagem e então termina.
    Antes de terminar, o processo deve imprimir a mensagem resultante.
"""


import threading
import time
import random
import string

"""ESPAÇO PARA A ORGANIZAÇÃO DO CÓDIGO DA LISTA CIRCULAR"""

class NoDaLista:
	#Classe que recebe um nó da lista encadeada pra organizar o anel 
	def __init__(self, dado):
		self.dado = dado
		self.proximo = None
		
class ListaEncadeada:
        def __init__(self):
            self.cabeca = None
            self.cauda = None
        
def insere_no(lista, novo_dado):
    novo_no = NoDaLista(novo_dado)
    if lista.cabeca == None:
        novo_no.proximo = novo_no
        lista.cauda = novo_no
    else:
        novo_no.proximo = lista.cabeca
        lista.cauda.proximo = novo_no
    lista.cabeca = novo_no

def tamanho_lista(lista):
    if lista.cabeca == None:
        return 0
    if lista.cabeca == lista.cabeca.proximo:
        return 1
    else:
        no = lista.cabeca.proximo
        i = 1
        while no != lista.cabeca:
            i += 1
            no = no.proximo
        return(i)
        
def imprime_lista(lista):
    n = tamanho_lista(lista)
    if n == 0:
        return("Lista vazia")
    else:
        impressao = "[ "
        no = lista.cabeca
        for i in range (n):
            impressao += str(no.dado)
            no = no.proximo
            impressao += " -> "
        impressao += "Volta ao início ]"
    return impressao
    
def trabalho(palavra, anel):
    essa = anel.cabeca
    resposta = palavra
    while True:
        resposta = essa.dado.servico(resposta)
        if resposta != 0:
            essa.proximo.dados = resposta
            essa = essa.proximo
        else:
            return True
    

"""ESPAÇO PARA A ORGANIZAÇÃO DO CÓDIGO DAS THREADS"""
class myThread ():
    def __init__ (self, id):
        self.id = id
        dados = []
     
    def servico(self, palavra):
        resposta = operacao(palavra)
        return resposta
    
        
    
"""ESPAÇO PARA AS OPERAÇÕES COM A STRING"""
def string_aleatoria():
    lista = []
    for i in range (0,80,1):
        l = random.choice(string.ascii_letters)
        lista.append(l)
    palavra = "".join(lista)
    return palavra

def maiuscula_enesima(palavra, n):
    nova = palavra[:n] + palavra[n:n+1].capitalize()
    if n<80:
        nova += palavra[n+1:]
    return nova

def operacao(dado):
    print(dado)
    if dado.isupper():
        return 0
    else:
        return dado_alterado(dado)

def dado_alterado(dado):
    lista = []
    novo_dado = dado
    for i in range(0,80,1):
        if (novo_dado[i].islower()):
            novo_dado = maiuscula_enesima(dado,i)
            break
    return (novo_dado)


    
"""Espaço para a função principal"""

#Criar a lista encadeada circular
lista = ListaEncadeada()

palavra = string_aleatoria() #Criar a mensagem como uma string aleatória com 80 caracteres

#Criar as 30 threads
for i in range(30):
    t = myThread(i)
    insere_no(lista,t) #Colocar cada thread na lista encadeada circular

trabalho(palavra,lista)
